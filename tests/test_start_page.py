import logging

from selenium import webdriver

from constants.base import DRIVER_PATH, BASE_URL

log = logging.getLogger(__name__)


class TestStartPage:

    def test_open_the_page(self):
        driver = webdriver.Chrome(DRIVER_PATH)
        driver.get(BASE_URL)
        driver.implicitly_wait(1.5)
        driver.close()
