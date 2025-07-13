# utils/helpers.py
import os
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from config.settings import SCREENSHOT_DIR

def take_screenshot(driver, name):
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    screenshot_path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to: {screenshot_path}")

def scroll_down(driver, times=1, scroll_factor=0.8, delay=2):
    """
    Scrolls down the page by a certain factor of the window height.
    :param driver: WebDriver instance
    :param times: Number of times to scroll down.
    :param scroll_factor: Factor of window height to scroll (e.g., 0.8 for 80%).
    :param delay: Time to wait after each scroll.
    """
    for _ in range(times):
        driver.execute_script(f"window.scrollBy(0, window.innerHeight * {scroll_factor});")
        time.sleep(delay)

def handle_modal_popup(driver, wait, selectors, action='click', timeout=5):
    """
    Attempts to handle various modal pop-ups by looking for specified selectors.
    :param driver: WebDriver instance.
    :param wait: WebDriverWait instance.
    :param selectors: A list of (By.Strategy, locator_string) tuples for modal close/accept buttons.
    :param action: 'click' or 'dismiss'.
    :param timeout: How long to wait for each modal.
    """
    for by_strategy, locator in selectors:
        try:
            modal_button = wait.until(EC.element_to_be_clickable((by_strategy, locator)), timeout)
            if modal_button:
                if action == 'click':
                    modal_button.click()
                    print(f"Handled pop-up using locator: {locator}")
                elif action == 'dismiss' and hasattr(modal_button, 'send_keys'): # For dismissing with ESC if element is an input
                    modal_button.send_keys(webdriver.common.keys.Keys.ESCAPE)
                    print(f"Dismissed pop-up using ESC on locator: {locator}")
                time.sleep(2) # Give time for modal to disappear
                return True
        except TimeoutException:
            continue
        except NoSuchElementException:
            continue
    print("No relevant pop-up found or handled.")
    return False