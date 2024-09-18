import logging

def setup_logger(name=None, level=logging.INFO):
    if name is None:
        raise ValueError("Logger name must be specified")
    
    logger = logging.getLogger(name)
    
    # Check if the level is valid
    if not isinstance(level, int) or level not in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
        raise ValueError(f"Invalid logging level: {level}")
    
    # Set the logging level
    logger.setLevel(level)
    
    # Check if the logger already has handlers to avoid duplicate logs
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        
        # Define a formatter with a specific format for log messages
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # Set the formatter for the console handler
        console_handler.setFormatter(formatter)
        
        # Add the console handler to the logger
        logger.addHandler(console_handler)
    
    return logger