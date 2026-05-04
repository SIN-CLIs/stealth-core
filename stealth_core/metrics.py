from prometheus_client import Counter, Histogram, Gauge
SHELL_COMMANDS = Counter("stealth_commands_total","Total commands",["tool","status"])
COMMAND_DURATION = Histogram("stealth_command_duration_seconds","Command duration",["tool"])
ACTIVE_CHROME_INSTANCES = Gauge("stealth_chrome_instances","Active Chrome processes")
AX_ELEMENTS_FOUND = Counter("stealth_ax_elements_found_total","AX elements found",["role"])
SURVEYS_COMPLETED = Counter("stealth_surveys_completed_total","Completed surveys",["provider"])
