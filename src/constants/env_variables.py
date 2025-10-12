import os
from pathlib import Path

RESOURCES_FOLDER: Path = Path(os.getenv("RESOURCES_FOLDER",str(Path(__file__).parent.parent.parent / "resources")))
