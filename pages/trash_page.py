from .base_page import BasePage
from yadi_disk_api import API


class TrashPage(BasePage):
    def delete_full_folder(self, path_to_folder):
        disk = API()
        disk.delete_file_or_folder(self.root_directory(path_to_folder))

    @staticmethod
    def path_to_trash():
        disk = API()
        path = []
        end_path = 0
        beginning_path = 0
        len_path = 4
        resources_trash = disk.resources_trash()

        # Нужно начинать с четвертого для того что бы не добавить лишний путь т.к четвертым символом обязательно будет _
        for i in resources_trash[4:]:
            len_path += 1
            if i == "/":
                beginning_path = len_path
            if i == '_':
                end_path = len_path + 40
                # Путь в корзине отличается от оригинального лишь суфиксом и его длина составляет 40 символов.
                path.append(resources_trash[beginning_path:end_path])

        return path
