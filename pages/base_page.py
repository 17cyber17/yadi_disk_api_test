from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from .locators import BasePageLocators
import urllib.parse
from yadi_disk_api import API

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=1):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def should_be_folder_or_file(self, path):
        true_path = urllib.parse.unquote(path)
        end_name = 0
        beginning_name = 0
        locator = BasePageLocators()

        for i in true_path:
            end_name += 1
            if i == "/":
                locator_folder_or_file = locator.search_for_file_or_folder(true_path[beginning_name:end_name - 1])
                assert self.is_element_present(
                    *locator_folder_or_file), f'There is no folder or file named "{true_path[beginning_name:end_name - 1]}"'
                folder = self.browser.find_element(*locator_folder_or_file)
                driver = self.browser
                actionChains = ActionChains(driver)
                actionChains.double_click(folder).perform()
                beginning_name = end_name

        if beginning_name == 0 and end_name != 0:
            locator_folder_or_file = locator.search_for_file_or_folder(true_path)
            assert self.is_element_present(*locator_folder_or_file), f'There is no folder or file named "{true_path}"'
        else:
            if beginning_name != 0:
                locator_folder_or_file = locator.search_for_file_or_folder(true_path[beginning_name:end_name])
                assert self.is_element_present(
                    *locator_folder_or_file), f'There is no folder or file named "{true_path[beginning_name:end_name]}"'

    def should_not_be_folder_or_file(self, path):
        true_path = urllib.parse.unquote(path)
        end_name = 0
        beginning_name = 0
        locator = BasePageLocators()

        for i in true_path:
            end_name += 1
            if i == "/":
                locator_folder_or_file = locator.search_for_file_or_folder(true_path[beginning_name:end_name - 1])
                assert self.is_element_present(*locator_folder_or_file), f'There is no folder or file named "{true_path}"'
                folder = self.browser.find_element(*locator_folder_or_file)
                driver = self.browser
                actionChains = ActionChains(driver)
                actionChains.double_click(folder).perform()
                beginning_name = end_name

        if beginning_name == 0 and end_name != 0:
            locator_folder_or_file = locator.search_for_file_or_folder(true_path)
            print(self.is_disappeared(*locator_folder_or_file))
            assert self.is_disappeared(*locator_folder_or_file), f'The file or folder named "{true_path}"\
                                                                                            exists, although it shouldnt'
        else:
            if beginning_name != 0:
                locator_folder_or_file = locator.search_for_file_or_folder(true_path[beginning_name:end_name])
                assert self.is_disappeared(
                    *locator_folder_or_file), f'The file or folder named "{true_path[beginning_name:end_name]}"\ ' \
                                              f'exists, although it shouldnt'

    def delete_folder(self, path_to_folder):
        true_path = urllib.parse.unquote(path_to_folder)
        disk = API()
        locator = BasePageLocators()
        end_name = len(true_path)
        beginning_name = 0

        for i in true_path[::-1]:
            beginning_name += 1
            if i == "/":
                print(true_path[:end_name])
                locator_folder_or_file = locator.search_for_file_or_folder(true_path[end_name - beginning_name+1:end_name])
                disk.delete_file_or_folder(true_path[:end_name])
                self.is_disappeared(*locator_folder_or_file)
                end_name = end_name - beginning_name
                beginning_name = 0

        if end_name == len(true_path) and beginning_name != 0:
            print(true_path)
            locator_folder_or_file = locator.search_for_file_or_folder(true_path)
            disk.delete_file_or_folder(true_path)
            self.is_disappeared(*locator_folder_or_file)
        else:
            if end_name != len(true_path):
                print(true_path[:end_name])
                locator_folder_or_file = locator.search_for_file_or_folder(true_path[:end_name])
                disk.delete_file_or_folder(true_path[:end_name])
                self.is_disappeared(*locator_folder_or_file)

