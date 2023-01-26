from constants.start_page import StartPageConsts
from pages.base_page import BasePage

from pages.utils import log_decorator, rand_username, rand_email, rand_str


class StartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConsts

    def open_text_box_section(self):
        """Open the Text box section"""
        self.click(xpath=self.constants.ELEMENTS_CARD_XPATH)

    @log_decorator
    def fill_text_box(self, username=rand_username, email=rand_email, address=rand_str):
        """Fill the input fields"""
        self.fill_field(xpath=self.constants.TEXT_BOX_FULL_NAME_XPATH, value=username)
        self.fill_field(xpath=self.constants.EMAIL_INPUT_FIELD_XPATH, value=email)
        self.fill_field(xpath=self.constants.PERMANENT_ADDRESS_FIELD_XPATH, value=address)
        self.click(self.constants.SUBMIT_BUTTON_XPATH)

    @log_decorator
    def verify_submit_data(self, fill_text_box):
        """Fill fields and submit"""
        assert self.is_exists(self.constants.OUTPUT_AREA_XPATH)
        return StartPage(self.driver)
