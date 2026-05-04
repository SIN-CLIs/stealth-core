import time, logging
from .exceptions import MaxRetriesExceededError
logger = logging.getLogger(__name__)

def retry(max_attempts=3, backoff_factor=0.5, exponential=True, retry_on=(Exception,)):
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except retry_on as e:
                    last_exc = e
                    if attempt == max_attempts:
                        raise MaxRetriesExceededError(f"{func.__name__} failed after {max_attempts}: {e}") from e
                    wait = backoff_factor * (2 ** (attempt - 1) if exponential else 1)
                    logger.warning("Retry %d/%d %s: %s. Wait %.1fs", attempt, max_attempts, func.__name__, e, wait)
                    time.sleep(wait)
        return wrapper
    return decorator
