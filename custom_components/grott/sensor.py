"""Sensor."""
# import logging
import json

# import time
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.const import (
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfEnergy,
    UnitOfFrequency,
    UnitOfPower,
    UnitOfTemperature,
)
from homeassistant.core import HomeAssistant

from . import GrottDataCoordinator, grott_coordinators
from .entity import GrottEntity


async def async_setup_entry(hass: HomeAssistant, entry, async_add_devices):
    """Async Setup entry."""

    async_add_devices(
        [
            GrottSensor(
                coordinator,
                None,  # deviceclass
                "Datalogger serial number",
                None,  # unit
                "datalogserial",  # Valuepair
                "mdi:select-inverse",  # icon
                "growatt_datalogger_serial",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                None,  # deviceclass
                "Serial number",
                None,  # unit
                "device",  # Valuepair
                "mdi:select-inverse",  # icon
                "growatt_serial",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                None,  # deviceclass
                "Date",
                None,  # unit
                "time",  # Valuepair
                "mdi:calendar",  # icon
                "growatt_date",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                None,  # deviceclass
                "Time",
                None,  # unit
                "time",  # Valuepair
                "mdi:calendar",  # icon
                "growatt_time",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                None,  # deviceclass
                "State",
                None,  # unit
                "pvstatus",  # Valuepair
                "mdi:power-settings",  # icon
                "growatt_status",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.POWER,  # deviceclass
                "String 1 (kiloWatt)ph",
                UnitOfPower.KILO_WATT,  # unit
                "pv1watt",  # Valuepair
                "mdi:solar-power",  # icon
                "growatt_string1_watt",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.VOLTAGE,  # deviceclass
                "String 1 (Voltage)",
                UnitOfElectricPotential.VOLT,  # unit
                "pv1voltage",  # Valuepair
                "mdi:solar-power",  # icon
                "growatt_string1_voltage",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.CURRENT,  # deviceclass
                "String 1 (Current)",
                UnitOfElectricCurrent.AMPERE,  # unit
                "pv1current",  # Valuepair
                "",  # icon
                "growatt_string1_current",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.POWER,  # deviceclass
                "String 2 (kiloWatt)",
                UnitOfPower.KILO_WATT,  # unit
                "pv2watt",  # Valuepair
                "mdi:solar-power",  # icon
                "growatt_string2_watt",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.VOLTAGE,  # deviceclass
                "String 2 (Voltage)",
                UnitOfElectricPotential.VOLT,  # unit
                "pv2voltage",  # Valuepair
                "mdi:solar-power",  # icon
                "growatt_string2_voltage",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.CURRENT,  # deviceclass
                "String 2 (Current)",
                UnitOfElectricCurrent.AMPERE,  # unit
                "pv2current",  # Valuepair
                "",  # icon
                "growatt_string2_current",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.POWER,  # deviceclass
                "String 1+2 (kilowatt)",
                UnitOfPower.KILO_WATT,  # unit
                "pv1watt+pv2watt",  # Valuepair
                "mdi:solar-power",  # icon
                "growatt_string1_2_watt",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.POWER,  # deviceclass
                "Input kiloWatt (Actual)",
                UnitOfPower.KILO_WATT,  # unit
                "pvpowerin",  # Valuepair
                "mdi:solar-power",  # icon
                "growatt_actual_input_power",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.POWER,  # deviceclass
                "Output kiloWatt (Actual)",
                UnitOfPower.KILO_WATT,  # unit
                "pvpowerout",  # Valuepair
                "mdi:solar-power",  # icon
                "growatt_actual_output_power",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.FREQUENCY,  # deviceclass
                "Grid frequency",
                UnitOfFrequency.HERTZ,  # unit
                "pvfrequentie",  # Valuepair
                "mdi:waveform",  # icon
                "growatt_grid_frequency",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.VOLTAGE,  # deviceclass
                "Grid Phase voltage",
                UnitOfElectricPotential.VOLT,  # unit
                "pvgridvoltage",  # Valuepair
                "",  # icon
                "growatt_phase_voltage",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.CURRENT,  # deviceclass
                "Grid Phase current",
                UnitOfElectricCurrent.AMPERE,  # unit
                "pvgridcurrent",  # Valuepair
                "",  # icon
                "growatt_phase_current",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.POWER,  # deviceclass
                "Grid Phase power",
                UnitOfPower.KILO_WATT,  # unit
                "pvgridpower",  # Valuepair
                "",  # icon
                "growatt_phase_power",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Generated energy (Today)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "eactoday",  # Valuepair
                "mdi:solar-power",  # icon
                "growatt_generated_energy_today",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Generated solar energy (Today)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "pvenergytoday",  # Valuepair
                "mdi:solar-power",  # icon
                "growatt_generated_solar_energy_today",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Generated solar energy (epv1) (Today)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "epv1today",  # Valuepair
                "mdi:solar-power",  # icon
                "growatt_generated_solar_energy_epv1_today",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Generated solar energy (epv2) (Today)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "epv2today",  # Valuepair
                "mdi:solar-power",  # icon
                "growatt_generated_solar_energy_epv2_today",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Generated solar energy (epv1+2) (Today)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "epv1today+epv2today",  # Valuepair
                "mdi:solar-power",  # icon
                "growatt_generated_solar_energy_epv1_2_today",  # uniqueid and transkey
                SensorStateClass.TOTAL_INCREASING,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Generated energy (Total)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "eactotal",  # Valuepair
                "mdi:solar-power",  # icon
                "growatt_generated_energy_total",  # uniqueid and transkey
                SensorStateClass.TOTAL_INCREASING,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Generated solar energy (Total)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "epvtotal",  # Valuepair
                "mdi:solar-power",  # icon
                "growatt_generated_solar_energy_total",  # uniqueid and transkey
                SensorStateClass.TOTAL_INCREASING,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.TEMPERATURE,  # deviceclass
                "Inverter temperature",
                UnitOfTemperature.CELSIUS,  # unit
                "pvtemperature",  # Valuepair
                "mdi:thermometer",  # icon
                "growatt_inverer_temperature",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.TEMPERATURE,  # deviceclass
                "IPM temperature",
                UnitOfTemperature.CELSIUS,  # unit
                "pvipmtemperature",  # Valuepair
                "mdi:thermometer",  # icon
                "growatt_ipm_temperature",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    # battery
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                None,  # deviceclass
                "Battery System workmode",
                None,  # unit
                "uwsysworkmode",  # Valuepair
                "mdi:power-settings",  # icon
                "growatt_battery_sysworkmode",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.TEMPERATURE,  # deviceclass
                "Battery temperature",
                UnitOfTemperature.CELSIUS,  # unit
                "#battemp",  # Valuepair
                "mdi:thermometer",  # icon
                "growatt_battery_temperature",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Battery ac charged (Today)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "eacharge_today",  # Valuepair
                "mdi:battery-arrow-up",  # icon
                "growatt_battery_ac_harged_today",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Battery ac charged (Total)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "eacharge_total",  # Valuepair
                "mdi:battery-arrow-up",  # icon
                "growatt_battery_ac_charged_total",  # uniqueid and transkey
                SensorStateClass.TOTAL_INCREASING,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.POWER,  # deviceclass
                "Battery charging (actual)",
                UnitOfPower.KILO_WATT,  # unit
                "p1charge1",  # Valuepair
                "mdi:battery-arrow-up",  # icon
                "growatt_battery_charge",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Battery charged (today)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "eharge1_tod",  # Valuepair
                "mdi:battery-arrow-up",  # icon
                "growatt_battery_charged_today",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Battery charged (total)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "eharge1_tot",  # Valuepair
                "mdi:battery-arrow-up",  # icon
                "growatt_battery_charged_total",  # uniqueid and transkey
                SensorStateClass.TOTAL_INCREASING,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.POWER,  # deviceclass
                "Battery discharging (actual)",
                UnitOfPower.KILO_WATT,  # unit
                "pdischarge1",  # Valuepair
                "mdi:battery-arrow-down-outline",  # icon
                "growatt_battery_discharge",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Battery discharged (today)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "edischarge1_tod",  # Valuepair
                "mdi:battery-arrow-down-outline",  # icon
                "growatt_battery_discharged_today",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Battery discharged (total)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "edischarge1_tot",  # Valuepair
                "mdi:battery-arrow-down-outline",  # icon
                "growatt_battery_discharged_total",  # uniqueid and transkey
                SensorStateClass.TOTAL_INCREASING,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.BATTERY,  # deviceclass
                "Battery State Of Charge",
                "%",  # unit
                "SOC",  # Valuepair
                "mdi:battery-charging-60",  # icon
                "growatt_battery_soc",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Local load consumption (today)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "elocalload_tod",  # Valuepair
                "mdi:power-plug",  # icon
                "growatt_local_load_today",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Local load consumption (total)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "elocalload_tot",  # Valuepair
                "mdi:power-plug",  # icon
                "growatt_local_load_total",  # uniqueid and transkey
                SensorStateClass.TOTAL_INCREASING,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.POWER,  # deviceclass
                "Local load consumption (actual)",
                UnitOfPower.KILO_WATT,  # unit
                "plocaloadr",  # Valuepair
                "mdi:power-plug",  # icon
                "growatt_local_load",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    # Import from grid
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.POWER,  # deviceclass
                "Import from grid (actual)",
                UnitOfPower.KILO_WATT,  # unit
                "pactouserr",  # Valuepair
                "mdi:transmission-tower-export",  # icon
                "growatt_import_from_grid",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Import from grid (today)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "etouser_tod",  # Valuepair
                "mdi:transmission-tower-export",  # icon
                "growatt_import_from_grid_today",  # uniqueid and transkey
                SensorStateClass.TOTAL_INCREASING,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Import from grid (total)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "etouser_tot",  # Valuepair
                "mdi:transmission-tower-export",  # icon
                "growatt_import_from_grid_total",  # uniqueid and transkey
                SensorStateClass.TOTAL_INCREASING,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    # Export to grid
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.POWER,  # deviceclass
                "Export to grid (actual)",
                UnitOfPower.KILO_WATT,  # unit
                "pactogridr",  # Valuepair
                "mdi:transmission-tower-import",  # icon
                "growatt_export_to_grid",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Export to grid (today)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "etogrid_tod",  # Valuepair
                "mdi:transmission-tower-import",  # icon
                "growatt_export_to_grid_today",  # uniqueid and transkey
                SensorStateClass.TOTAL_INCREASING,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                SensorDeviceClass.ENERGY,  # deviceclass
                "Export to grid (total)",
                UnitOfEnergy.KILO_WATT_HOUR,  # unit
                "etogrid_tot",  # Valuepair
                "mdi:transmission-tower-import",  # icon
                "growatt_export_to_grid_total",  # uniqueid and transkey
                SensorStateClass.TOTAL_INCREASING,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                None,  # deviceclass
                "Datalogger update interval",
                "sek",  # unit
                "datalogger_interval",  # Valuepair
                "",  # icon
                "growatt_datalogger_interval",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                None,  # deviceclass
                "Inverter work mode",
                None,  # unit
                "inverter_workmode",  # Valuepair
                "",  # icon
                "growatt_inverter_workmode",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )
    async_add_devices(
        [
            GrottSensor(
                coordinator,
                None,  # deviceclass
                "Discharge stop",
                "%",  # unit
                "discharge_stop",  # Valuepair
                "",  # icon
                "growatt_discharge_stop",  # uniqueid and transkey
                None,
            )
            for coordinator in grott_coordinators(hass, entry)
        ]
    )


class GrottSensor(GrottEntity, SensorEntity):
    """Grott sensor."""

    def __init__(
        self,
        coordinator: GrottDataCoordinator,
        device_class: SensorDeviceClass,
        name: str,
        unit: str,
        valuepair: str,
        icon: str,
        translationkey: str,
        state_class: str,
    ) -> None:
        """Init."""
        super().__init__(coordinator)
        self.data_coordinator = coordinator
        self._data_handler = self.data_coordinator.data_handler
        self._name = name
        self._attr_device_class = device_class
        self._attr_native_unit_of_measurement = unit
        self._attr_state_class = state_class
        self._valuepair = valuepair
        self._icon = icon
        self.key = translationkey
        self._attr_has_entity_name = True
        self._attr_unique_id = self.key
        self._sn = self.coordinator._devicesn

    # This property is important to let HA know if this entity is online or not.
    # If an entity is offline (return False), the UI will reflect this.
    @property
    def available(self) -> bool:
        """Return True if roller and hub is available."""
        return True

    @property
    def name(self):
        """Return name."""
        return self._name

    @property
    def state(self):  # noqa: C901
        """State."""
        # Hent data fra data_handler her
        data = json.loads(self._data_handler.mqttdata)
        if self._valuepair == "device":
            val = data.get(self._valuepair)
        elif self.key == "growatt_time":
            ss = str(data.get(self._valuepair))
            val = ss[11:19]
        elif self.key == "growatt_date":
            ss = str(data.get(self._valuepair))
            year = ss[0:4]
            month = ss[5:7]
            day = ss[8:10]
            val = f"{day}-{month}-{year}"
        elif self._valuepair == "pvstatus":
            val2 = data.get("values").get(self._valuepair)
            if val2 == 0:
                val = "Waiting"
            elif val2 == 1:
                val = "Normal"
            elif val2 == 2:
                val = "Fault"
            elif val2 in (3, 4, 5):
                val = "Normal"
            elif val2 == 6:
                val = "Waiting"
            else:
                val = "Unknown"
        elif self._valuepair in (
            "pv1voltage",
            "pv1current",
            "pv2voltage",
            "pv2current",
            "pvgridvoltage",
            "pvgridcurrent",
            "eactoday",
            "pvenergytoday",
            "epv1today",
            "epv2today",
            "eactotal",
            "epvtotal",
            "pvtemperature",
            "pvipmtemperature",
            "eacharge_today",
            "eacharge_total",
            "eharge1_tod",
            "eharge1_tot",
            "edischarge1_tod",
            "edischarge1_tot",
            "elocalload_tod",
            "elocalload_tot",
            "etouser_tod",
            "etouser_tot",
            "etogrid_tod",
            "etogrid_tot",
        ):
            val = round(data.get("values").get(self._valuepair) / 10, 4)
        elif self.key == "growatt_string1_2_watt":
            val = round(data.get("values").get("pv1watt") / 10000, 4) + round(
                data.get("values").get("pv1watt") / 10000, 4
            )
        elif self._valuepair in (
            "pv1watt",
            "pv2watt",
            "pvpowerin",
            "pvpowerout",
            "pvgridpower",
            "p1charge1",
            "pdischarge1",
            "plocaloadr",
            "pactouserr",
            "pactogridr",
        ):
            val = round(data.get("values").get(self._valuepair) / 10000, 4)
        elif self._valuepair in ("pvfrequentie"):
            val = round(data.get("values").get(self._valuepair) / 100, 4)
        elif self.key == "growatt_generated_solar_energy_epv1_2_today":
            val = round(data.get("values").get("epv1today") / 10, 4) + round(
                data.get("values").get("epv2today") / 10, 4
            )
        elif self._valuepair == "uwsysworkmode":
            val2 = data.get("values").get(self._valuepair)
            if val2 == 0:
                val = "Waiting"
            elif val2 == 1:
                val = "Selftest"
            elif val2 == 2:
                val = "Reserved"
            elif val2 == 3:
                val = "System fault"
            elif val2 == 4:
                val = "Flash"
            elif val2 == 5:
                val = "PVBATOnline"
            elif val2 == 6:
                val = "Battery online"
            elif val2 == 7:
                val = "PVOfflineMod"
            elif val2 == 8:
                val = "Battery offline"
            else:
                val = "Unknown"
        elif self._valuepair == "#battemp":
            val = round(data.get("values").get(self._valuepair), 4)
        elif self._valuepair == "SOC":
            val = data.get("values").get(self._valuepair)
        elif self._valuepair == "datalogger_interval":
            val = self._data_handler.data_logger_update_interval
        elif self._valuepair == "inverter_workmode":
            val = self._data_handler.inverter_mode
        elif self._valuepair == "discharge_stop":
            val = self._data_handler.discharge_stop
        elif "values" in data:
            val = data.get("values").get(self._valuepair)
        return val

    @property
    def icon(self):
        """Icon."""
        return self._icon
