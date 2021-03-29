from .base_page import BasePage
from .locators import BasePageLocators

class DiskPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(DiskPage, self).__init__(*args, **kwargs)
