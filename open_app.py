import logging
from ..setup import *
from appium.options.android import UiAutomator2Options
from selenium.common.exceptions import WebDriverException

# Initialize the logger
logger = setup_logger(name='open_app_logger', level=logging.INFO)

def open_app(capabilities: dict, additional_capabilities: dict, appium_server_url: str):
    try:
        # Validate capabilities
        if 'appPackage' not in additional_capabilities:
            logger.error("The 'appPackage' capability is missing from additional_capabilities.")
            raise ValueError("Missing required capability: 'appPackage'")

        # Merge capabilities
        capabilities.update(additional_capabilities)
        
        # Convert capabilities to AppiumOptions instance
        capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
        
        # Set up the driver
        driver = setup_driver(appium_server_url, capabilities_options)
        logger.info(f"Driver successfully initialized for {additional_capabilities['appPackage']}")
        
        # Check if the app is already in focus
        current_package = driver.current_package
        package_name = additional_capabilities['appPackage']
        
        if current_package != package_name:
            logger.info(f"App is not currently in focus. Activating app: {package_name}")
            driver.activate_app(package_name)
        else:
            logger.info(f"App {package_name} is already in focus.")
        
        return driver

    except ValueError as e:
        logger.error(f"ValueError encountered: {e}")
        raise

    except WebDriverException as e:
        logger.error(f"WebDriverException encountered: {e}")
        raise

    except Exception as e:
        logger.critical(f"An unexpected error occurred: {e}", exc_info=True)
        raise