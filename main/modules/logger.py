import logging

MONITOR_LOG = "logging/monitor.log"
SERVICE_LOG = "logging/service.log"
PROCESS_LOG = "logging/process.log"
REGISTRY_LOG = "logging/registry.log"

def make_logger(name, file, level=logging.INFO, formatter=None):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.FileHandler(file)
    handler.setLevel(level)

    if formatter is None:
        formatter = logging.Formatter("%(asctime)s - %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


monitor_logger = make_logger("monitor_logger", MONITOR_LOG)
service_logger = make_logger("service_logger", SERVICE_LOG)
process_logger = make_logger("process_logger", PROCESS_LOG)
registry_logger = make_logger("registry_logger", REGISTRY_LOG)
