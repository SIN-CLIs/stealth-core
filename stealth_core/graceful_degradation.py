"""Graceful Degradation — System läuft auch halb kaputt weiter."""
import logging, time
from enum import Enum
from typing import Any, Callable, Dict, Optional
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

class ServiceStatus(Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    FALLBACK = "fallback"
    UNAVAILABLE = "unavailable"
    BLACKLISTED = "blacklisted"

@dataclass
class ServiceState:
    name: str
    status: ServiceStatus = ServiceStatus.HEALTHY
    consecutive_failures: int = 0
    last_success: float = field(default_factory=time.time)
    last_failure: float = 0.0
    fallback_handler: Optional[Callable] = None
    recovery_timeout: float = 60.0
    max_failures_before_blacklist: int = 10

class GracefulDegradationManager:
    def __init__(self):
        self.services: Dict[str, ServiceState] = {}

    def register_service(self, name: str, fallback: Optional[Callable] = None,
                         recovery_timeout: float = 60.0, max_failures: int = 10):
        self.services[name] = ServiceState(
            name=name, fallback_handler=fallback,
            recovery_timeout=recovery_timeout, max_failures_before_blacklist=max_failures)

    def execute(self, service_name: str, primary: Callable, *args, **kwargs) -> Any:
        svc = self.services[service_name]
        if svc.status == ServiceStatus.BLACKLISTED:
            if svc.fallback_handler: return svc.fallback_handler(*args, **kwargs)
            raise RuntimeError(f"Service {service_name} is blacklisted")

        if svc.status == ServiceStatus.UNAVAILABLE:
            if time.time() - svc.last_failure > svc.recovery_timeout:
                svc.status = ServiceStatus.DEGRADED
            elif svc.fallback_handler:
                return svc.fallback_handler(*args, **kwargs)
            else:
                raise RuntimeError(f"Service {service_name} UNAVAILABLE")

        try:
            result = primary(*args, **kwargs)
            svc.consecutive_failures = 0
            svc.status = ServiceStatus.HEALTHY
            svc.last_success = time.time()
            return result
        except Exception as e:
            svc.consecutive_failures += 1
            svc.last_failure = time.time()
            logger.warning("Service %s failed (%d): %s", service_name, svc.consecutive_failures, e)
            if svc.consecutive_failures >= svc.max_failures_before_blacklist:
                svc.status = ServiceStatus.BLACKLISTED
                if svc.fallback_handler: return svc.fallback_handler(*args, **kwargs)
                raise
            elif svc.consecutive_failures >= 5:
                svc.status = ServiceStatus.UNAVAILABLE
                if svc.fallback_handler: return svc.fallback_handler(*args, **kwargs)
                raise
            elif svc.consecutive_failures >= 3:
                svc.status = ServiceStatus.FALLBACK
                if svc.fallback_handler: return svc.fallback_handler(*args, **kwargs)
            raise

    def get_status(self) -> dict:
        return {name: {"status": svc.status.value, "failures": svc.consecutive_failures,
                       "last_success": svc.last_success} for name, svc in self.services.items()}
