import subprocess, json
from stealth_core import retry, ProcessGuardian

def test_imports():
    from stealth_core import CircuitBreaker, retry
    assert True
