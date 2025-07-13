# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from config.settings import EXPLICIT_WAIT_TIME

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT_TIME)

    def go_to_url(self, url):
        self.driver.get(url)
        print(f"Navigated to: {url}")

    def find_element(self, by_locator):
        try:
            return self.wait.until(EC.presence_of_element_located(by_locator))
        except TimeoutException:
            raise NoSuchElementException(f"Element not found within {EXPLICIT_WAIT_TIME} seconds: {by_locator}")

    def find_elements(self, by_locator):
        try:
            return self.wait.until(EC.presence_of_all_elements_located(by_locator))
        except TimeoutException:
            return [] # Return empty list if no elements found within timeout

    def click(self, by_locator):
        element = self.wait.until(EC.element_to_be_clickable(by_locator))
        element.click()
        print(f"Clicked on element: {by_locator}")

    def send_keys(self, by_locator, text):
        element = self.find_element(by_locator)
        element.clear()
        element.send_keys(text)
        print(f"Sent keys '{text}' to element: {by_locator}")

    def wait_for_url_contains(self, text):
        print(f"URL now contains before: '{text}'")
        self.wait.until(EC.url_contains(text))
        print(f"URL now contains: '{text}'")

    def wait_for_visibility(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def wait_for_invisibility(self, by_locator):
        return self.wait.until(EC.invisibility_of_element_located(by_locator))

    def is_element_present(self, by_locator):
        try:
            self.driver.find_element(*by_locator)
            return True
        except NoSuchElementException:
            return False

    def is_element_displayed(self, by_locator):
        try:
            return self.find_element(by_locator).is_displayed()
        except (NoSuchElementException, TimeoutException):
            return False