import logging

from colorlog import ColoredFormatter


def custom(name):
    formatter = ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s %(message_log_color)s%(message)s",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
        secondary_log_colors={
            "message": {
                "DEBUG": "blue",
                "INFO": "reset",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "red",
            }
        },
        style="%",
    )

    # Create a logger and set its formatter
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)  # Set your desired logging level
    handler = logging.StreamHandler()  # You can also specify a different output stream
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
