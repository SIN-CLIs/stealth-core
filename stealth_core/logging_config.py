import logging, json, sys, warnings
from datetime import datetime

class StructuredFormatter(logging.Formatter):
    def format(self, record):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            return json.dumps({"ts": datetime.utcnow().isoformat(), "level": record.levelname,
                "logger": record.name, "msg": record.getMessage()})

def configure_logging(level=logging.INFO):
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(StructuredFormatter())
    logging.basicConfig(level=level, handlers=[handler])
