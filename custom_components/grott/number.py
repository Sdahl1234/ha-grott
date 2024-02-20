"""Support for grott number."""

from __future__ import annotations

import logging

from homeassistant.components.number import NumberEntity
from homeassistant.core import HomeAssistant

from . import GrottDataCoordinator, grott_coordinators
from .entity import GrottEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry, async_add_entities) -> None:
    """Do setup entry."""

    async_add_entities(
        [
            GrottNumber(coordinator, "Datalogger register", "grott_datalogger_register")
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_entities(
        [
            GrottNumber(coordinator, "Datalogger value", "grott_datalogger_value")
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_entities(
        [
            GrottNumber(coordinator, "Inverter register", "grott_inverter_register")
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_entities(
        [
            GrottNumber(coordinator, "Inverter value", "grott_inverter_value")
            for coordinator in grott_coordinators(hass, entry)
        ]
    )

    async_add_entities(
        [
            GrottNumber(coordinator, "Datalogger update interval", "grott_dui")
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_entities(
        [
            GrottNumber(coordinator, "Inverter update interval", "grott_iui")
            for coordinator in grott_coordinators(hass, entry)
        ]
    )


class GrottNumber(GrottEntity, NumberEntity):
    """grott number."""

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
        self.native_max_value = 2000
        self.native_min_value = 0
        if translationkey in ("grott_dui", "grott_iui"):
            self.native_step = 1
            self.native_unit_of_measurement = "sek"
        else:
            self.native_step = 0.1
            self.native_unit_of_measurement = ""
        self._attr_has_entity_name = True
        self.key = translationkey
        self._attr_unique_id = self.key
        self._sn = self.coordinator._devicesn
        self.icon = ""

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""
        if self.key == "grott_datalogger_register":
            self._data_handler.datalogger_register = int(value)
        elif self.key == "grott_datalogger_value":
            self._data_handler.datalogger_value = value
        elif self.key == "grott_inverter_register":
            self._data_handler.inverter_register = int(value)
        elif self.key == "grott_inverter_value":
            self._data_handler.inverter_value = value
        elif self.key == "grott_dui":
            self._data_handler.datalogger_update_interval = int(value)
        elif self.key == "grott_iui":
            self._data_handler.inverter_update_interval = int(value)

    @property
    def name(self):
        """Name."""
        return self._name

    @property
    def native_value(self):
        """Return value."""
        if self.key == "grott_datalogger_register":
            return self._data_handler.datalogger_register
        if self.key == "grott_datalogger_value":
            return self._data_handler.datalogger_value
        if self.key == "grott_inverter_register":
            return self._data_handler.inverter_register
        if self.key == "grott_inverter_value":
            return self._data_handler.inverter_value
        if self.key == "grott_dui":
            return self._data_handler.datalogger_update_interval
        if self.key == "grott_iui":
            return self._data_handler.inverter_update_interval
