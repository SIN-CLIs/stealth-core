import os; from pathlib import Path
OPENCODE_DB_PATH = Path(os.path.expanduser("~/.local/share/opencode/opencode.db"))
LEARN_FILE = Path(os.getcwd()) / "learn.md"
AGENTS_FILE = Path(os.getcwd()) / "agents.md"
CDP_REQUEST_TIMEOUT = 5
AX_POLL_INTERVAL = 1
AX_POLL_MAX_WAIT = 15
CIRCUIT_BREAKER_THRESHOLD = 5
CIRCUIT_BREAKER_RECOVERY = 30
WEB_ROLES = {"AXWebArea","AXRadioButton","AXButton","AXTextField","AXCheckBox","AXStaticText"}
WINDOW_ROLES = {"AXWindow","AXSheet","AXDialog","AXPopover","AXDrawer"}
