# conftest.py
import pytest
from utils.driver_factory import DriverFactory
from config.settings import IMPLICIT_WAIT_TIME

@pytest.fixture(scope="session")
def mobile_driver():
    driver = DriverFactory.get_mobile_chrome_driver()
    driver.implicitly_wait(IMPLICIT_WAIT_TIME)
    yield driver
    driver.quit()