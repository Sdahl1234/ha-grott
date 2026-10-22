"""Adds config flow for grott integration."""

import probatio

from homeassistant import config_entries, core, exceptions
from homeassistant.const import CONF_IP_ADDRESS, CONF_PASSWORD, CONF_USERNAME
from homeassistant.core import callback

from .const import DOMAIN

# _LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = probatio.Schema(
    {
        probatio.Required(CONF_IP_ADDRESS): str,
        probatio.Required(CONF_USERNAME): str,
        probatio.Required(CONF_PASSWORD): str,
    }
)


async def validate_input(hass: core.HomeAssistant, ip, username, password):
    """Validate the user input allows us to connect."""

    # Pre-validation for missing mandatory fields
    if not ip:
        raise MissingIPValue("The 'Ip address' field is required.")
    if not username:
        raise MissingUsernameValue("The 'username' field is required.")
    if not password:
        raise MissingPasswordValue("The 'password' field is required.")

    for entry in hass.config_entries.async_entries(DOMAIN):
        if any(
            [
                entry.data[CONF_IP_ADDRESS] == ip,
                entry.data[CONF_USERNAME] == username,
                entry.data[CONF_PASSWORD] == password,
            ]
        ):
            raise AlreadyConfigured("An entry with the given details already exists.")

    # Additional validations (if any) go here...


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for grott integration."""

    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> OptionsFlowHandler:
        """Create the options flow."""
        return OptionsFlowHandler()

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            try:
                ip = user_input[CONF_IP_ADDRESS]
                username = user_input[CONF_USERNAME]
                password = user_input[CONF_PASSWORD].replace(" ", "")
                await validate_input(self.hass, ip, username, password)
                unique_id = "grott"
                await self.async_set_unique_id(unique_id)
                self._abort_if_unique_id_configured()
                return self.async_create_entry(
                    title=unique_id,
                    data={
                        CONF_IP_ADDRESS: ip,
                        CONF_USERNAME: username,
                        CONF_PASSWORD: password,
                    },
                )

            except AlreadyConfigured:
                return self.async_abort(reason="already_configured")
            except CannotConnect:
                errors["base"] = "connection_error"
            except MissingIPValue:
                errors["base"] = "missing_ip"
            except MissingUsernameValue:
                errors["base"] = "missing_username"
            except MissingPasswordValue:
                errors["base"] = "missing_password"

        return self.async_show_form(
            step_id="user",
            data_schema=DATA_SCHEMA,
            errors=errors,
        )

    async def async_step_reconfigure(self, user_input=None):
        """Handle reconfiguration of an existing entry."""
        entry = self._get_reconfigure_entry()
        current_password = entry.options.get(
            CONF_PASSWORD, entry.data.get(CONF_PASSWORD)
        )
        errors = {}

        if user_input is not None:
            ip = user_input[CONF_IP_ADDRESS].strip()
            username = user_input[CONF_USERNAME].strip()
            password = user_input.get(CONF_PASSWORD, "").replace(" ", "")
            if not password:
                password = current_password

            if not ip:
                errors["base"] = "missing_ip"
            elif not username:
                errors["base"] = "missing_username"
            elif not password:
                errors["base"] = "missing_password"
            else:
                return self.async_update_reload_and_abort(
                    entry,
                    data_updates={
                        CONF_IP_ADDRESS: ip,
                        CONF_USERNAME: username,
                        CONF_PASSWORD: password,
                    },
                    options={},
                )

        return self.async_show_form(
            step_id="reconfigure",
            data_schema=self.add_suggested_values_to_schema(
                probatio.Schema(
                    {
                        probatio.Required(CONF_IP_ADDRESS): str,
                        probatio.Required(CONF_USERNAME): str,
                        probatio.Optional(CONF_PASSWORD): str,
                    }
                ),
                user_input
                or {
                    CONF_IP_ADDRESS: entry.data.get(CONF_IP_ADDRESS),
                    CONF_USERNAME: entry.data.get(CONF_USERNAME),
                },
            ),
            errors=errors,
        )

    # async def async_step_select_mower(self):


class OptionsFlowHandler(config_entries.OptionsFlow):
    """Flowhandler."""

    async def async_step_init(self, user_input=None):
        """Step init."""
        if user_input is not None:
            password = user_input.get(CONF_PASSWORD, "").replace(" ", "")
            if not password:
                return self.async_create_entry(data={})
            return self.async_create_entry(data={CONF_PASSWORD: password})

        return self.async_show_form(
            step_id="init",
            data_schema=probatio.Schema(
                {
                    probatio.Optional(CONF_PASSWORD): str,
                }
            ),
        )


class CannotConnect(exceptions.HomeAssistantError):
    """Error to indicate we cannot connect."""


class AlreadyConfigured(exceptions.HomeAssistantError):
    """Error to indicate host is already configured."""


class MissingIPValue(exceptions.HomeAssistantError):
    """Error to indicate name is missing."""


class MissingUsernameValue(exceptions.HomeAssistantError):
    """Error to indicate name is missing."""


class MissingPasswordValue(exceptions.HomeAssistantError):
    """Error to indicate name is missing."""
