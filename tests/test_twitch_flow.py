# tests/test_twitch_flow.py
import pytest
from pages.twitch_home_page import TwitchHomePage
from pages.twitch_search_results_page import TwitchSearchResultsPage
from pages.twitch_streamer_page import TwitchStreamerPage
import os

class TestTwitchMobileFlow:

    @pytest.mark.parametrize("game_name", ["StarCraft II"])
    def test_twitch_starcraft_streamer_flow(self, mobile_driver, game_name):
        home_page = TwitchHomePage(mobile_driver)
        search_results_page = TwitchSearchResultsPage(mobile_driver)
        streamer_page = TwitchStreamerPage(mobile_driver)

        # Step 1: Go to Twitch
        home_page.load()
        #home_page.handle_initial_modals()

        # Step 2: Click in the search icon and input game
        home_page.click_search_icon()
        home_page.search_for_game(game_name)

        # Step 3: Select View All
        search_results_page.click_view_all_channels()
        
        # Step 4: Scroll down 2 times
        search_results_page.scroll_down_multiple_times(times=2)
        
        # Step 5: Select Live Channels Visible On Scroll
        assert search_results_page.click_first_visible_live_channel(), "Failed to click on a live channel."

        # Step 6: On the streamer page, wait until all is load and take a screenshot
        streamer_page.wait_for_video_player()
        streamer_page.handle_streamer_page_modal()
        streamer_page.take_streamer_screenshot(test_name=f"{game_name.replace(' ', '_').lower()}_streamer_page")
        
        print("Test finished successfully.")