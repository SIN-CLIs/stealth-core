import json; from pathlib import Path; from datetime import datetime
STATE_FILE = Path("stealth_state.json")
class StateManager:
    def __init__(self, filepath=STATE_FILE): self.filepath = filepath
    def load(self):
        if not self.filepath.exists(): return {"surveys":{},"sessions":{}}
        return json.loads(self.filepath.read_text())
    def save(self, state): self.filepath.write_text(json.dumps(state, indent=2, default=str))
    def set_survey_status(self, sid, status, extra=None):
        s=self.load(); s["surveys"][sid]={"status":status,"updated_at":datetime.now().isoformat(),**(extra or {})}; self.save(s)
