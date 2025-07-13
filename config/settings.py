# config/settings.py
import os

BASE_URL = "https://www.twitch.tv/"
IMPLICIT_WAIT_TIME = 10
EXPLICIT_WAIT_TIME = 20
SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'screenshots')

# Mobile Emulation Settings
MOBILE_EMULATION_DEVICE_METRICS = {"width": 375, "height": 667, "pixelRatio": 3}
MOBILE_EMULATION_USER_AGENT = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"