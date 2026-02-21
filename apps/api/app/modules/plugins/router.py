from __future__ import annotations

from fastapi import APIRouter, Depends, Query, Request

from ...core import (
    ActorContext,
    ErrorResponse,
    NotFoundError,
    PluginRegistry,
    append_audit_event,
    require_roles,
)
from .schemas import PluginActivationRequest, PluginResponse

router = APIRouter()
registry = PluginRegistry()

ERROR_RESPONSES = {
    403: {"model": ErrorResponse, "description": "Zugriff verweigert"},
    404: {"model": ErrorResponse, "description": "Plugin nicht gefunden"},
    500: {"model": ErrorResponse, "description": "Interner Serverfehler"},
}


def _trace_id(request: Request) -> str:
    return getattr(request.state, "trace_id", "unbekannt")


@router.get("", response_model=list[PluginResponse], responses=ERROR_RESPONSES)
def list_plugins(
    request: Request,
    enabled: bool | None = Query(default=None, description="Filter nach aktiviert/deaktiviert"),
    actor: ActorContext = Depends(require_roles("autor", "review", "freigabe", "admin")),
) -> list[PluginResponse]:
    plugins = [PluginResponse.model_validate(item) for item in registry.list_plugins(enabled=enabled)]
    append_audit_event(
        action="plugins.list",
        resource_type="plugin",
        resource_id="*",
        actor_user_id=actor.user_id,
        actor_role=actor.role,
        trace_id=_trace_id(request),
        metadata={"count": len(plugins)},
    )
    return plugins


@router.get("/{plugin_id}", response_model=PluginResponse, responses=ERROR_RESPONSES)
def get_plugin(
    plugin_id: str,
    request: Request,
    actor: ActorContext = Depends(require_roles("autor", "review", "freigabe", "admin")),
) -> PluginResponse:
    plugin = registry.get_plugin(plugin_id)
    if not plugin:
        raise NotFoundError("Plugin nicht gefunden")
    append_audit_event(
        action="plugins.read",
        resource_type="plugin",
        resource_id=plugin_id,
        actor_user_id=actor.user_id,
        actor_role=actor.role,
        trace_id=_trace_id(request),
        metadata={},
    )
    return PluginResponse.model_validate(plugin)


@router.patch("/{plugin_id}/activation", response_model=PluginResponse, responses=ERROR_RESPONSES)
def set_plugin_activation(
    plugin_id: str,
    payload: PluginActivationRequest,
    request: Request,
    actor: ActorContext = Depends(require_roles("admin")),
) -> PluginResponse:
    updated = registry.set_plugin_enabled(plugin_id, payload.enabled)
    if not updated:
        raise NotFoundError("Plugin nicht gefunden")

    append_audit_event(
        action="plugins.activation.update",
        resource_type="plugin",
        resource_id=plugin_id,
        actor_user_id=actor.user_id,
        actor_role=actor.role,
        trace_id=_trace_id(request),
        metadata={"enabled": payload.enabled, "status": updated.get("status")},
    )
    return PluginResponse.model_validate(updated)