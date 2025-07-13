# pages/twitch_search_results_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.helpers import scroll_down
import time

class TwitchSearchResultsPage(BasePage):
    # Locators
    VIEW_ALL_CHANNEL_RESULTS = (By.XPATH, "//*[@aria-label = 'View All Channel Search Results']/parent::a")
    LIVE_CHANNELS_LIST_ITEMS = (By.XPATH, "//div[@role = 'list']/div")
    
    def __init__(self, driver):
        super().__init__(driver)

    def click_view_all_channels(self):
        print("Clicking 'View All Channels'...")
        self.click(self.VIEW_ALL_CHANNEL_RESULTS)
        time.sleep(3) # Give time for the page to load after clicking

    def scroll_down_multiple_times(self, times=2):
        print(f"Scrolling down {times} times...")
        scroll_down(self.driver, times=times)

    def click_first_visible_live_channel(self):
        print("Attempting to click the first visible live channel...")
        channels = self.find_elements(self.LIVE_CHANNELS_LIST_ITEMS)
        if not channels:
            print("No live channel elements found on the page.")
            return False

        clicked_channel = False
        for channel in channels:
            try:
                if channel.is_displayed():
                    channel.click()
                    print(f"Clicked on a live channel: {channel.text if channel.text else 'Unnamed Channel'}")
                    clicked_channel = True
                    break
            except Exception as e:
                print(f"Could not click element (might be stale or not interactive yet): {e}")
                continue
        
        if not clicked_channel:
            print("No visible and clickable live channel found.")
        return clicked_channel