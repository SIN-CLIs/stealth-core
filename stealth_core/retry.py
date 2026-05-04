"""Retry-Decorator mit exponentiellem Backoff."""
import time
from functools import wraps

class MaxRetriesExceededError(Exception):
    def __init__(self, func_name, attempts, last_error):
        self.func_name = func_name
        self.attempts = attempts
        self.last_error = last_error
        super().__init__(f"{func_name} failed after {attempts} attempts: {last_error}")

def retry(max_attempts=3, backoff=0.5, exponential=True, retry_on=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_e = None
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except retry_on as e:
                    last_e = e
                    if attempt < max_attempts - 1:
                        wait = backoff * (2 ** (attempt + 1) if exponential else 1)
                        time.sleep(wait)
            raise MaxRetriesExceededError(func.__name__, max_attempts, last_e)
        return wrapper
    return decorator
