import time, logging, psutil
logger = logging.getLogger(__name__)

class ProcessGuardian:
    def __init__(self, heartbeat=3):
        self.heartbeat = heartbeat
        self.pids = []

    def register(self, pid):
        self.pids.append(pid)

    def is_alive(self, pid):
        return psutil.pid_exists(pid) and psutil.Process(pid).status() != psutil.STATUS_ZOMBIE

    def monitor(self, restart_callback=None):
        while True:
            for pid in list(self.pids):
                if not self.is_alive(pid):
                    logger.warning("Process %d dead – restart", pid)
                    if restart_callback:
                        restart_callback(pid)
                    self.pids.remove(pid)
            time.sleep(self.heartbeat)
