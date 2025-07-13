# pages/twitch_streamer_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.helpers import take_screenshot, handle_modal_popup
import time
from selenium.webdriver.support import expected_conditions as EC

class TwitchStreamerPage(BasePage):
    # Locators
    VIDEO_PLAYER = (By.CSS_SELECTOR, 'video[playsinline]')
    STREAMER_PAGE_MODAL_CLOSE_BUTTON = (By.XPATH, "//div[@role='dialog']//button[@aria-label='Close']")

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_video_player(self):
        print("Waiting for video player to be present on the streamer page...")
        try:
            self.wait_for_visibility(self.VIDEO_PLAYER)
            print("Video player element found.")
        except TimeoutException:
            print("Video player element not found within timeout. Page might be structured differently or still loading.")
        time.sleep(5) # Additional wait for full page load

    def handle_streamer_page_modal(self):
        print("Attempting to handle streamer page pop-up...")
        handle_modal_popup(self.driver, self.wait, [(By.XPATH, "//div[@role='dialog']//button[@aria-label='Close']")])


    def take_streamer_screenshot(self, test_name="streamer_page"):
        print("Taking screenshot of the streamer page...")
        take_screenshot(self.driver, test_name)