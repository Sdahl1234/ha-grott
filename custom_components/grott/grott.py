"""GrottPy."""
import logging
from threading import Timer
import time
import uuid

import paho.mqtt.client as mqtt
import requests

_LOGGER = logging.getLogger(__name__)


class grott:
    """Grott class."""

    def __init__(self, useername, password, ip) -> None:
        """Init function."""

        self._dataupdated = None
        self.inverter_serial: str = None
        self.datalogger_serial: str = None
        self.ip = ip
        self.username = useername
        self.password = password
        self.mqttdata = None
        self.client_id = str(uuid.uuid4())
        self.mqtt_client = None
        self.inverter_timer: Timer = None
        self.datalogger_timer: Timer = None
        self.datalogger_update_interval: int = 600
        self.inverter_update_interval: int = 600
        self.data_logger_update_interval = None
        self.inverter_mode = None
        self.discharge_stop = None
        self.datalogger_register: int = None
        self.datalogger_value: float = None
        self.inverter_register: int = None
        self.inverter_value: float = None

    def set_inverter(self, register: int, value: str, inverter: str) -> str:
        """Set inverter data."""
        try:
            url = f"http://192.168.86.57:5782/inverter?command=register&register={register}&inverter={inverter}&value={value}"
            _LOGGER.debug(url)
            response = requests.put(url, timeout=60)
            if response.status_code == 200:
                return True
            return False
        except Exception as error:  # pylint: disable=broad-except
            _LOGGER.debug(error)
            return False

    def set_datalogger(self, register: int, value: str, datalogger: str) -> str:
        """Set data_logger data."""
        try:
            url = f"http://192.168.86.57:5782/datalogger?command=register&register={register}&datalogger={datalogger}&value={value}"
            _LOGGER.debug(url)
            response = requests.put(url, timeout=60)
            if response.status_code == 200:
                return True
            return False
        except Exception as error:  # pylint: disable=broad-except
            _LOGGER.debug(error)
            return False

    def get_inverter(self, register: int, inverter: str) -> str:
        """Get data_logger data."""
        try:
            url = f"http://192.168.86.57:5782/inverter?command=register&register={register}&inverter={inverter}"
            _LOGGER.debug(url)
            response = requests.get(url, timeout=60)
            if response.status_code == 200:
                response_data = response.json()
                if self._dataupdated is not None:
                    self._dataupdated()
                return response_data.get("value")
            return None
        except Exception as error:  # pylint: disable=broad-except
            _LOGGER.debug(error)
            return None

    def get_datalogger(self, register: int, datalogger: str) -> str:
        """Get data_logger data."""
        try:
            url = f"http://192.168.86.57:5782/datalogger?command=register&register={register}&datalogger={datalogger}"
            _LOGGER.debug(url)
            response = requests.get(url, timeout=60)
            if response.status_code == 200:
                response_data = response.json()
                if self._dataupdated is not None:
                    self._dataupdated()
                return response_data.get("value")
            return None
        except Exception as error:  # pylint: disable=broad-except
            _LOGGER.debug(error)
            return None

    def update(self):
        """Force HA to update sensors."""

    def GetDataloggerValues(self):
        """Update datalooger update interval."""
        while self.datalogger_timer:
            val = self.get_datalogger(4, self.datalogger_serial)
            if val is not None:
                self.data_logger_update_interval = float(val) * 60
            time.sleep(self.datalogger_update_interval)

    def GetInverterValues(self):
        """Update datalooger update interval."""
        while self.inverter_timer:
            val = self.get_inverter(1044, self.inverter_serial)
            if val is not None:
                if val == 0:
                    self.inverter_mode = "Load først"
                if val == 1:
                    self.inverter_mode = "Batteri først"
                if val == 2:
                    self.inverter_mode = "Grid først"
            val = self.get_inverter(1071, self.inverter_serial)
            if val is not None and val < 101:
                self.discharge_stop = val
            time.sleep(self.inverter_update_interval)

    def on_load(self):
        """Init the mqtt client."""
        if not self.username or not self.password or not self.ip:
            _LOGGER.debug(
                "Please set username, password and IP in the instance settings"
            )
            return

        self.connect_mqtt()
        self.datalogger_timer = Timer(5, self.GetDataloggerValues)
        self.datalogger_timer.start()
        self.inverter_timer = Timer(10, self.GetInverterValues)
        self.inverter_timer.start()

    def connect_mqtt(self):
        """Connect mgtt."""
        if self.mqtt_client:
            self.mqtt_client.disconnect()

        self.mqtt_client = mqtt.Client(client_id=self.client_id)
        self.mqtt_client.on_connect = self.on_mqtt_connect
        self.mqtt_client.on_message = self.on_mqtt_message
        self.mqtt_client.on_disconnect = self.on_mqtt_disconnect
        self.mqtt_client.on_error = self.on_mqtt_error
        self.mqtt_client.on_close = self.on_mqtt_close
        self.mqtt_client.username_pw_set(self.username, self.password)
        try:
            self.mqtt_client.connect(
                host=self.ip,
                keepalive=60,
            )
            _LOGGER.debug("MQTT starting loop")
            self.mqtt_client.loop_start()
        except Exception as error:  # pylint: disable=broad-except
            _LOGGER.warning("MQTT connect error: " + str(error))  # noqa: G003

    def on_mqtt_disconnect(self, client, userdata, rc):
        """On mqtt disconnect."""
        _LOGGER.debug("MQTT disconnected")

    def on_mqtt_connect(self, client, userdata, flags, rc):
        """On mqtt connect."""
        _LOGGER.debug("MQTT connected event")
        _LOGGER.debug(
            "MQTT subscribe to: " + "/energy/grott"  # noqa: G003
        )
        self.mqtt_client.subscribe("energy/grott/#", qos=0)
        _LOGGER.debug("MQTT subscribe ok")

    def on_mqtt_message(self, client, userdata, message):  # noqa: C901
        """On mqtt message."""
        _LOGGER.debug("MQTT message: " + message.topic + " " + message.payload.decode())  # noqa: G003
        try:
            self.mqttdata = message.payload.decode()
            if self._dataupdated is not None:
                self._dataupdated()

        except Exception as error:  # pylint: disable=broad-except
            _LOGGER.debug("MQTT message error: " + str(error))  # noqa: G003
            _LOGGER.debug("MQTT message: " + message.payload.decode())  # noqa: G003

    def on_mqtt_error(self, client, userdata, error):
        """On mqtt error."""
        _LOGGER.debug("MQTT error: " + str(error))  # noqa: G003

    def on_mqtt_close(self, client, userdata, rc):
        """On mqtt close."""
        _LOGGER.debug("MQTT closed")
