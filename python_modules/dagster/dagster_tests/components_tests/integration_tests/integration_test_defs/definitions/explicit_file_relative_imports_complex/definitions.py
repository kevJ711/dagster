import dagster as dg

from .submodule import asset_in_submodule as asset_in_submodule  # noqa: TID252


@dg.asset
def asset_in_some_file() -> None: ...
