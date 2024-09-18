import logging
from ..utils import open_app
from ..setup import setup_logger

error_logger = setup_logger(name='dana_error_logger', level=logging.ERROR)
def automate_dana(capabilities: dict, additional_capabilities: dict, appium_server_url: str):
    try:
        driver = open_app(capabilities, additional_capabilities, appium_server_url)
        
    except Exception as e:
        error_logger.critical(f'An unexpected error occurred: {e}')