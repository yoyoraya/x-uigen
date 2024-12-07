import logging

def setup_logger():
    """Configure and return a logger instance"""
    logger = logging.getLogger('xui-extractor')
    logger.setLevel(logging.INFO)
    
    # Create console handler with formatting
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

logger = setup_logger()
