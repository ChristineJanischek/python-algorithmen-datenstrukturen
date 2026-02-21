from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from fastapi import Depends, Header

from .errors import ForbiddenError


@dataclass(frozen=True)
class ActorContext:
    user_id: str
    role: str


def get_actor_context(
    x_user_id: str | None = Header(default=None, alias="X-User-Id"),
    x_role: str | None = Header(default=None, alias="X-Role"),
) -> ActorContext:
    user_id = (x_user_id or "unbekannt").strip()
    role = (x_role or "").strip().lower()
    if not role:
        raise ForbiddenError("Rolle fehlt. Bitte Header X-Role setzen.")
    return ActorContext(user_id=user_id, role=role)


def require_roles(*allowed_roles: str) -> Callable:
    normalized = {role.strip().lower() for role in allowed_roles}

    def dependency(actor: ActorContext = Depends(get_actor_context)) -> ActorContext:
        if actor.role not in normalized:
            rollen = ", ".join(sorted(normalized))
            raise ForbiddenError(f"Zugriff verweigert. Erlaubte Rollen: {rollen}")
        return actor

    return dependency