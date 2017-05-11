import logging
import os

def init_logger(logger_file="testlog.log", mode="a"):
    """Initiate logging."""
    formatter = logging.Formatter('%(asctime)s %(levelname)8s %(filename)s @ '
                                  '%(lineno)d %(funcName)s: %(message)s')

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.handlers = []
    if logger_file:
        file_handler = logging.FileHandler(logger_file, mode=mode)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    logger.addHandler(console)

    logging.info("Default logging initiated.")
    return logger


def rollback_log(log_file):
    """Empty the log file."""
    if not os.path.isfile(log_file):
        logging.warn("Log file %s does not exist?!", log_file)
        return

    logging.info("Emptying log file %s", log_file)
    logging.shutdown()
    open(log_file, "w").close()