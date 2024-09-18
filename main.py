import time
import logging
from src.utils import open_app
from src.setup import setup_logger

# Set up desired capabilities
capabilities = dict(
    platformName='Android', 
    automationName= 'UiAutomator2', 
    noReset=True, 
    fullReset=False
)

APPIUM_PORT = '4723'
APPIUM_HOST = '127.0.0.1'
appium_server_url = f'http://{APPIUM_HOST}:{APPIUM_PORT}/wd/hub'

info_logger = setup_logger(name='main_info_logger')
error_logger = setup_logger(name='main_error_logger', level=logging.ERROR)

# Never use appActivity.
# Instead we should check the state where are we right when we open the app and navigate it through syntetic users actions.
def main():
    try:
        driver = open_app(capabilities, dict(
            udid='FA7X5PMVUSWWLZ59',
            deviceName= 'Android A',
            appPackage= 'com.miui.calculator.go'
        ), appium_server_url)

        info_logger.info('Script execute successfully.')
        time.sleep(5)
    except Exception as e:
        error_logger.critical(f"An unexpected error occurred: {e}")
    finally:
        info_logger.info('Quit the app.')
        if 'driver' in locals():
            driver.quit()

if __name__ == '__main__':
    main()