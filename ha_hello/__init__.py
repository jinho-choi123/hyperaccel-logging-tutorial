import sys

import tomli
from loguru import logger

# Read dependencies from pyproject.toml
with open("pyproject.toml", "rb") as f:
    pyproject = tomli.load(f)

logger.remove()

logger.add(
    sink=sys.stderr,
    level=pyproject["tool"]["ha_hello"]["config"]["loguru_active_level"],
)
