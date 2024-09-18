import logging
import urllib.parse
from appium import webdriver
from .logger import setup_logger
from appium.options.android import UiAutomator2Options
from selenium.common.exceptions import WebDriverException

info_logger = setup_logger(name='driver_info_logger')
error_logger = setup_logger(name='driver_error_logger', level=logging.ERROR)

def setup_driver(appium_server_url, capabilities_options):
    try:
        if not isinstance(appium_server_url, str):
            raise TypeError('appium_url must be a string.')
        
        # Validate the URL format
        parsed_url = urllib.parse.urlparse(appium_server_url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError("Invalid Appium Server URL format")

        if not isinstance(capabilities_options, UiAutomator2Options):
            info_logger.info(f'The capabilities_options is not the instance of UiAutomator2Options.')
            capabilities_options = UiAutomator2Options().load_capabilities(capabilities_options)
            
        driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)
        return driver
    except TypeError as e:
        error_logger.error(f'Type error occurred: {e}')
        return None
    except ValueError as e:
        error_logger.error(f'Value error occurred: {e}')
    except WebDriverException as e:
        error_logger.error(f'WebDriverException error occurred: {e}')
        return None
    except Exception as e:
        error_logger.error(f'An unexpected error occurred: {e}')
        return None