from constants.start_page import StartPageConsts

from pages.utils import log_decorator


class StartPage:

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConsts

    @log_decorator
    def fill_text_box(self):
        """Fill the input fields"""
