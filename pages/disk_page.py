from .base_page import BasePage
from yadi_disk_api import API
import urllib.parse
from .locators import BasePageLocators


class DiskPage(BasePage):
    def delete_folder(self, path_to_folder):
        # Раскодируем специальные символы для упрощения работы.
        true_path = urllib.parse.unquote(path_to_folder)
        disk = API()
        locator = BasePageLocators()
        end_name = len(true_path)
        beginning_name = 0

        # Идем по пути в обратном направлении.
        for i in true_path[::-1]:
            beginning_name += 1
            if i == "/":
                locator_folder_or_file = locator.search_for_file_or_folder(true_path[end_name-beginning_name+1:end_name])
                # Удаляем папку и проверяем что она исчезла.
                disk.delete_file_or_folder(true_path[:end_name])
                self.is_disappeared(*locator_folder_or_file)
                end_name = end_name - beginning_name
                beginning_name = 0

        # Рассматривается случай если путь состоял только из корня.
        if end_name == len(true_path) and beginning_name != 0:
            locator_folder_or_file = locator.search_for_file_or_folder(true_path)
            disk.delete_file_or_folder(true_path)
            self.is_disappeared(*locator_folder_or_file)
        else:
            # Удаление последней(корневой) папки.
            if end_name != len(true_path):
                locator_folder_or_file = locator.search_for_file_or_folder(true_path[:end_name])
                disk.delete_file_or_folder(true_path[:end_name])
                self.is_disappeared(*locator_folder_or_file)
