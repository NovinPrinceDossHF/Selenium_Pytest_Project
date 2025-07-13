# pages/twitch_home_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from config.settings import BASE_URL
from utils.helpers import handle_modal_popup
from selenium.webdriver.support import expected_conditions as EC

class TwitchHomePage(BasePage):
    # Locators
    SEARCH_ICON = (By.XPATH, "//*[text() = 'Browse']/../..")
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[data-test-selector="mobile-search-input"], input[placeholder="Search"]')
    CONSENT_BUTTONS = [
        (By.XPATH, "//button[contains(., 'Accept Recommended Settings')]"),
        (By.XPATH, "//button[contains(., 'Accept Cookies')]")
    ]
    OVERLAY_CLOSE_BUTTONS = [
        (By.XPATH, "//button[@aria-label='Close']"),
        (By.XPATH, "//button[contains(., 'No Thanks')]")
    ]

    def __init__(self, driver):
        super().__init__(driver)
        self.url = BASE_URL

    def load(self):
        self.go_to_url(self.url)
        self.wait_for_url_contains("twitch.tv")

    def handle_initial_modals(self):
        print("Attempting to handle initial modals/pop-ups...")
        handle_modal_popup(self.driver, self.wait, self.CONSENT_BUTTONS)
        handle_modal_popup(self.driver, self.wait, self.OVERLAY_CLOSE_BUTTONS)

    def click_search_icon(self):
        print("Clicking search icon...")
        self.click(self.SEARCH_ICON)

    def search_for_game(self, game_name):
        encoded_search_term = game_name.replace(" ", "%20")
        print(f"Inputting '{game_name}' into search bar and pressing Enter...")
        self.send_keys(self.SEARCH_INPUT, game_name)
        self.find_element(self.SEARCH_INPUT).send_keys(Keys.ENTER)
        self.wait_for_url_contains(f"search?term={encoded_search_term}") 