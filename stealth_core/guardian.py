import os, time, logging, subprocess
from dataclasses import dataclass

@dataclass
class HealthStatus:
    component: str
    is_healthy: bool
    details: str
    timestamp: float

class ProcessGuardian:
    def __init__(self, check_interval=3):
        self.check_interval = check_interval
        self.watched = {}

    def watch(self, name, pid=None, port=None, db_path=None):
        self.watched[name] = {"pid": pid, "port": port, "db_path": db_path}

    def check(self):
        results = []
        for name, cfg in self.watched.items():
            if cfg["pid"]:
                alive = self._pid_alive(cfg["pid"])
                results.append(HealthStatus(name, alive, "Lebt" if alive else "Tot", time.time()))
            if cfg["port"]:
                ok = self._port_open(cfg["port"])
                results.append(HealthStatus(f"{name}:{cfg['port']}", ok, "Offen" if ok else "Geschlossen", time.time()))
        return results

    def monitor_loop(self, restart_cb=None):
        while True:
            for name, cfg in self.watched.items():
                if cfg["pid"] and not self._pid_alive(cfg["pid"]):
                    if restart_cb:
                        restart_cb(name, cfg)
            time.sleep(self.check_interval)

    def _pid_alive(self, pid):
        try: os.kill(pid, 0); return True
        except: return False

    def _port_open(self, port):
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try: s.connect(("127.0.0.1", port)); s.close(); return True
        except: return False
