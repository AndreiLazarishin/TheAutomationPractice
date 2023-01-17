from constants.start_page import StartPageConsts


class StartPage:

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = StartPageConsts
