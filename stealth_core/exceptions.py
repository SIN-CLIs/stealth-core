class StealthSuiteError(Exception): pass
class ChromeNotFoundError(StealthSuiteError): pass
class CDPConnectionError(StealthSuiteError): pass
class MaxRetriesExceededError(StealthSuiteError):
    def __init__(self, func_name, attempts, last_exc):
        super().__init__(f"{func_name}: {attempts} attempts failed: {last_exc}")
class CircuitBreakerOpenError(StealthSuiteError): pass
class AXElementNotFoundError(StealthSuiteError): pass
