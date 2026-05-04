import time, logging
from enum import Enum
logger = logging.getLogger(__name__)

class ServiceStatus(Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    FALLBACK = "fallback"
    UNAVAILABLE = "unavailable"
    BLACKLISTED = "blacklisted"

class GracefulDegradationManager:
    def __init__(self):
        self.services = {}

    def register(self, name, fallback=None, recovery_timeout=60, max_failures=10):
        self.services[name] = {"status": ServiceStatus.HEALTHY, "failures": 0,
            "last_success": time.time(), "last_failure": 0, "fallback": fallback,
            "recovery_timeout": recovery_timeout, "max_failures": max_failures}

    def execute(self, name, primary, *args, **kwargs):
        svc = self.services[name]
        if svc["status"] == ServiceStatus.BLACKLISTED:
            raise RuntimeError(f"Service {name} blacklisted")
        if svc["status"] == ServiceStatus.UNAVAILABLE:
            if time.time() - svc["last_failure"] > svc["recovery_timeout"]:
                svc["status"] = ServiceStatus.DEGRADED
            elif svc["fallback"]:
                return svc["fallback"](*args, **kwargs)
            else:
                raise RuntimeError(f"Service {name} unavailable, no fallback")
        try:
            result = primary(*args, **kwargs)
            svc["failures"] = 0
            svc["status"] = ServiceStatus.HEALTHY
            svc["last_success"] = time.time()
            return result
        except Exception as e:
            svc["failures"] += 1
            svc["last_failure"] = time.time()
            if svc["failures"] >= svc["max_failures"]:
                svc["status"] = ServiceStatus.BLACKLISTED
            elif svc["failures"] >= 5:
                svc["status"] = ServiceStatus.UNAVAILABLE
            elif svc["failures"] >= 3:
                svc["status"] = ServiceStatus.FALLBACK
            raise
