"""Optional JSON Schema validation for generated telemetry."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping

_SDK_ROOT = Path(__file__).resolve().parents[3]
_SCHEMA_PATH = _SDK_ROOT / "schemas" / "v1" / "telemetry-payload.schema.json"
_RESIDUAL_SCHEMA_PATH = _SDK_ROOT / "schemas" / "v1" / "residual-score-response.schema.json"
_SCHEMAS_ROOT = _SDK_ROOT / "schemas"


@lru_cache(maxsize=1)
def telemetry_validator():
    """Return a cached Draft 2020-12 validator for TelemetryPayload."""
    try:
        from jsonschema import Draft202012Validator
        from referencing import Registry, Resource
        from referencing.jsonschema import DRAFT202012
    except ImportError as exc:
        raise ImportError(
            "jsonschema and referencing are required for schema validation. "
            "Install with: pip install 'jsonschema[format]>=4.23.0' referencing"
        ) from exc

    resources = []
    for schema_path in sorted(_SCHEMAS_ROOT.rglob("*.schema.json")):
        with schema_path.open(encoding="utf-8") as handle:
            contents = json.load(handle)
        schema_id = contents.get("$id")
        if schema_id:
            resources.append(
                (schema_id, Resource.from_contents(contents, default_specification=DRAFT202012))
            )

    registry = Registry().with_resources(resources)
    with _SCHEMA_PATH.open(encoding="utf-8") as handle:
        schema = json.load(handle)
    schema_id = schema["$id"]
    resource = registry.contents(schema_id)
    return Draft202012Validator(resource, registry=registry)


def validate_telemetry_payload(payload: Mapping[str, Any]) -> None:
    """Raise ``jsonschema.ValidationError`` when payload is invalid."""
    telemetry_validator().validate(payload)


@lru_cache(maxsize=1)
def residual_score_validator():
    """Cached validator for ResidualScoreResponse."""
    try:
        from jsonschema import Draft202012Validator
        from referencing import Registry, Resource
        from referencing.jsonschema import DRAFT202012
    except ImportError as exc:
        raise ImportError(
            "jsonschema and referencing are required for schema validation."
        ) from exc

    resources = []
    for schema_path in sorted(_SCHEMAS_ROOT.rglob("*.schema.json")):
        with schema_path.open(encoding="utf-8") as handle:
            contents = json.load(handle)
        schema_id = contents.get("$id")
        if schema_id:
            resources.append(
                (schema_id, Resource.from_contents(contents, default_specification=DRAFT202012))
            )
    registry = Registry().with_resources(resources)
    with _RESIDUAL_SCHEMA_PATH.open(encoding="utf-8") as handle:
        schema = json.load(handle)
    resource = registry.contents(schema["$id"])
    return Draft202012Validator(resource, registry=registry)


def validate_residual_score_response(payload: Mapping[str, Any]) -> None:
    """Raise when a residual-score API body is invalid."""
    residual_score_validator().validate(payload)


def schema_path_relative() -> str:
    return str(_SCHEMA_PATH.relative_to(_SDK_ROOT.parent))
