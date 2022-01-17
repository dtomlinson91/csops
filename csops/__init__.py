import os
from typing import Any

import panaetius


_config_path = os.environ.get("CSOPS_CONFIG")
if _config_path is not None:
    CONFIG: Any = panaetius.Config("csops", _config_path, skiper_header_init=True)
else:
    CONFIG = panaetius.Config("csops", "~/.config")


panaetius.set_config(CONFIG, "gcp_kms_key")
