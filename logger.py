import sys
import logging

def setup_chat_logger(log_file="chat.log"):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Remove existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    fh = logging.FileHandler(log_file, mode='w')
    fh.setLevel(logging.INFO)
    # Filter out noisy HTTP/traces lines from the file handler
    class _HttpNoiseFilter(logging.Filter):
        def filter(self, record: logging.LogRecord) -> bool:
            msg = record.getMessage()
            # drop lines mentioning HTTP request details or traces ingest endpoints
            if 'HTTP Request:' in msg or 'traces/ingest' in msg:
                return False
            return True
    fh.addFilter(_HttpNoiseFilter())
    fh.setFormatter(logging.Formatter(
        fmt='[%(asctime)s] [%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    ))

    logger.addHandler(fh)
    
    logger.info("--------- New Session -------------")
    return logger
