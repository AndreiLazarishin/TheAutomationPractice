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

    def test_text_box_and_submit(self, start_page):
        start_page.open_text_box_section()
        start_page.fill_text_box()
        start_page.verify_submit_data()
