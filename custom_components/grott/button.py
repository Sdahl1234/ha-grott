"""Support for Adano lawnmower."""

from __future__ import annotations

import logging

from homeassistant.components.button import ButtonEntity
from homeassistant.core import HomeAssistant

from . import GrottDataCoordinator, grott_coordinators
from .entity import GrottEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry, async_add_entities) -> None:
    """Do setup entry."""

    async_add_entities(
        [
            GrottButton(coordinator, "Set datalogger", "grott_set_datalogger")
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_entities(
        [
            GrottButton(coordinator, "Set inverter", "grott_set_inverter")
            for coordinator in grott_coordinators(hass, entry)
        ]
    )


class GrottButton(GrottEntity, ButtonEntity):
    """Grott buttons."""

    def __init__(
        self,
        coordinator: GrottDataCoordinator,
        name: str,
        translationkey: str,
    ) -> None:
        """Init."""
        super().__init__(coordinator)
        self.data_coordinator = coordinator
        self._data_handler = self.data_coordinator.data_handler
        self._name = name
        self._attr_has_entity_name = True
        self.key = translationkey
        self._attr_unique_id = self.key
        self._sn = self.coordinator._devicesn

    @property
    def name(self):
        """Name."""
        return self._name

    async def async_press(self) -> None:
        """Handle the button press."""
        if self.key == "grott_set_datalogger":
            await self.hass.async_add_executor_job(
                self._data_handler.set_datalogger,
                self._data_handler.datalogger_register,
                str(self._data_handler.datalogger_value).replace(",", "."),
                self._data_handler.datalogger_serial,
            )
        elif self.key == "grott_set_inverter":
            val = str(int(self._data_handler.inverter_value))
            if len(val) == 1:
                val = "0" + val
            await self.hass.async_add_executor_job(
                self._data_handler.set_inverter,
                self._data_handler.inverter_register,
                val,
                self._data_handler.inverter_serial,
            )
