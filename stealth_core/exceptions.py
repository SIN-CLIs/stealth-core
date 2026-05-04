class StealthSuiteError(Exception): pass
class ChromeNotFoundError(StealthSuiteError): pass
class CDPConnectionError(StealthSuiteError): pass
class MaxRetriesExceededError(StealthSuiteError): pass
class CircuitBreakerOpenError(StealthSuiteError): pass
class AXElementNotFoundError(StealthSuiteError): pass
