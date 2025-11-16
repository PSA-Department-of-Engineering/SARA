"""Logging configuration for SARA application using structlog."""

import logging
import sys
import structlog


def configure_logging(log_level: str = "INFO") -> None:
    """
    Configure structlog for the entire application.
    
    Args:
        log_level: The logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    # Configure standard logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, log_level.upper()),
    )
    
    # Configure structlog
    structlog.configure(
        processors=[
            # Add log level to event dict
            structlog.stdlib.add_log_level,
            # Add logger name to event dict
            structlog.stdlib.add_logger_name,
            # Add timestamp
            structlog.processors.TimeStamper(fmt="iso"),
            # Add line number and function name
            structlog.processors.CallsiteParameterAdder(
                {
                    structlog.processors.CallsiteParameter.FILENAME,
                    structlog.processors.CallsiteParameter.FUNC_NAME,
                    structlog.processors.CallsiteParameter.LINENO,
                }
            ),
            # Stack trace for exceptions
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            # Use ConsoleRenderer for pretty colored output
            structlog.dev.ConsoleRenderer(colors=True),
        ],
        # Use stdlib-compatible logger
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )


def get_logger(name: str = None) -> structlog.stdlib.BoundLogger:
    """
    Get a structlog logger instance.
    
    Args:
        name: The name of the logger (typically __name__ of the module)
    
    Returns:
        A configured structlog logger
    """
    return structlog.get_logger(name)
