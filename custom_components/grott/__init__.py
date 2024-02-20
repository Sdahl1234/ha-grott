"""Grott integration."""
import asyncio
from datetime import timedelta
import json
import logging
import time

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_IP_ADDRESS, CONF_PASSWORD, CONF_USERNAME, Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DH, DOMAIN, INVS
from .grott import grott

PLATFORMS = [
    Platform.SENSOR,
    Platform.NUMBER,
    Platform.BUTTON,
]

_LOGGER = logging.getLogger(__name__)


def grott_coordinators(hass: HomeAssistant, entry: ConfigEntry):
    """Help with entity setup."""
    coordinators: list[GrottDataCoordinator] = hass.data[DOMAIN][entry.entry_id][INVS]
    yield from coordinators


async def async_setup(hass: HomeAssistant, config):  # noqa: D103
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Groot."""
    ip = entry.data.get(CONF_IP_ADDRESS)
    username = entry.data.get(CONF_USERNAME)
    password = entry.data.get(CONF_PASSWORD)

    data_handler = grott(username, password, ip)
    await hass.async_add_executor_job(data_handler.on_load)
    # wait for first incomming mqtt to get the serianlnumber
    timeout = time.time() + 10
    while data_handler.mqttdata is None:
        if time.time() > timeout:
            _LOGGER.warning("Timeout getting mqtt data")
            return False
        await asyncio.sleep(0.1)
    mqtt_data = json.loads(data_handler.mqttdata)
    data_handler.inverter_serial = mqtt_data.get("device")
    data_handler.datalogger_serial = mqtt_data.get("values").get("datalogserial")

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {DH: data_handler}

    inverters = [mqtt_data.get("device")]
    inv = [GrottDataCoordinator(hass, data_handler, devicesn) for devicesn in inverters]

    await asyncio.gather(
        *[coordinator.async_config_entry_first_refresh() for coordinator in inv]
    )

    hass.data[DOMAIN][entry.entry_id][INVS] = inv

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    entry.async_on_unload(entry.add_update_listener(async_update_entry))

    return True


async def async_update_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Update options."""
    await hass.config_entries.async_reload(entry.entry_id)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


class GrottDataCoordinator(DataUpdateCoordinator):  # noqa: D101
    config_entry: ConfigEntry

    def __init__(self, hass: HomeAssistant, data_handler: grott, devicesn) -> None:
        """Initialize my coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            # Name of the data. For logging purposes.
            name=DOMAIN,
            # Polling interval. Will only be polled if there are subscribers.
            update_interval=timedelta(seconds=5),
        )
        self.data_handler = data_handler
        self._devicesn = devicesn

    @property
    def dsn(self):
        """DeviceSerialNumber."""
        return self._devicesn

    @property
    def device_info(self) -> DeviceInfo:
        """Return device info."""
        return DeviceInfo(
            identifiers={
                (DOMAIN, self.unique_id),
            },
            model="SPH-3600",
            manufacturer="Growatt",
            serial_number=self._devicesn,
            name="Growatt",
        )

    @property
    def unique_id(self) -> str:
        """Return the system descriptor."""
        return f"{DOMAIN}-{self._devicesn}"

    def update_device(self):
        """Update device."""
        self.data_handler.update_devices(self._devicesn)

    async def _async_update_data(self):
        try:
            await self.hass.async_add_executor_job(self.data_handler.update)
            return self.data_handler
        except Exception as ex:  # pylint: disable=broad-except
            _LOGGER.debug(f"update failed: {ex}")  # noqa: G004
