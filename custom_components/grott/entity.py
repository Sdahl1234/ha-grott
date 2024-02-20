"""Base Grott entity."""

from __future__ import annotations

from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import GrottDataCoordinator


class GrottEntity(CoordinatorEntity[GrottDataCoordinator]):
    """Base Grott entity."""

    coordinator = GrottDataCoordinator

    def __init__(
        self,
        coordinator: GrottDataCoordinator,
    ) -> None:
        """Init."""
        super().__init__(coordinator)
        self._attr_device_info = coordinator.device_info
        self._attr_unique_id = f"{self.__class__._attr_unique_id}"
