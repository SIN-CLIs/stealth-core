import urllib.request, sqlite3
from .constants import CDP_REQUEST_TIMEOUT, OPENCODE_DB_PATH

class HealthChecker:
    def check_cdp_port(self, port):
        try:
            r = urllib.request.urlopen(f"http://127.0.0.1:{port}/json", timeout=CDP_REQUEST_TIMEOUT)
            return {"alive": True, "http_status": r.getcode()}
        except Exception as e:
            return {"alive": False, "error": str(e)}

    def check_opencode_db(self):
        if not OPENCODE_DB_PATH.exists():
            return {"alive": False, "reason": "DB not found"}
        try:
            conn = sqlite3.connect(str(OPENCODE_DB_PATH))
            conn.execute("SELECT 1")
            conn.close()
            return {"alive": True}
        except Exception as e:
            return {"alive": False, "reason": str(e)}

    def check_all(self, cdp_port=59734):
        return {"cdp": self.check_cdp_port(cdp_port), "opencode_db": self.check_opencode_db()}
