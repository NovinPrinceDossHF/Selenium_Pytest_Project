# utils/driver_factory.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config.settings import MOBILE_EMULATION_DEVICE_METRICS, MOBILE_EMULATION_USER_AGENT

class DriverFactory:
    @staticmethod
    def get_mobile_chrome_driver():
        chrome_options = Options()

        mobile_emulation = {
            "deviceMetrics": MOBILE_EMULATION_DEVICE_METRICS,
            "userAgent": MOBILE_EMULATION_USER_AGENT
        }

        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        
        # Suppress "DevTools listening on ws://..." message
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(service=webdriver.ChromeService(ChromeDriverManager().install()), options=chrome_options)
        return driver