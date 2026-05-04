import pytest, time, psutil
from stealth_core.graceful_degradation import GracefulDegradationManager, ServiceStatus

class TestChaosResilience:
    def test_recovery_after_blacklist(self):
        degradation = GracefulDegradationManager()
        degradation.register_service("test_svc", max_failures_before_blacklist=3)
        def failing_func(): raise RuntimeError("Simulated")
        for i in range(3):
            with pytest.raises(RuntimeError): degradation.execute("test_svc", failing_func)
        assert degradation.services["test_svc"].status == ServiceStatus.BLACKLISTED
        def fallback(): return "fallback_works"
        degradation.services["test_svc"].fallback_handler = fallback
        assert degradation.execute("test_svc", failing_func) == "fallback_works"

    def test_system_self_heals(self):
        degradation = GracefulDegradationManager()
        degradation.register_service("heal_svc", recovery_timeout=0.1, max_failures=10)
        degradation.services["heal_svc"].consecutive_failures = 6
        degradation.services["heal_svc"].status = ServiceStatus.UNAVAILABLE
        degradation.services["heal_svc"].last_failure = time.time() - 1.0
        assert degradation.execute("heal_svc", lambda: "ok") == "ok"
        assert degradation.services["heal_svc"].status == ServiceStatus.HEALTHY
