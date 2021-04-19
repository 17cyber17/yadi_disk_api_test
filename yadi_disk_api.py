import requests


class API:
    def __init__(self):
        self.base_url = 'https://cloud-api.yandex.net/v1/disk'
        self.headers = {'Authorization': 'Your token'}

    def create_folder(self, path_to_folder):
        res = requests.put(f'{self.base_url}/resources?path={path_to_folder}', headers=self.headers)

    def create_copy_file_or_folder(self, path_copied_resource, path_created_resource):
        res = requests.post(f'{self.base_url}/resources/copy?from={path_copied_resource}&path={path_created_resource}',
                            headers=self.headers)

    def move_file_or_folder(self, path_resource_move, path_created_resource):
        res = requests.post(f'{self.base_url}/resources/move?from={path_resource_move}&path={path_created_resource}',
                            headers=self.headers)

    def delete_file_or_folder(self, path_file_or_folder):
        res = requests.delete(f'{self.base_url}/resources?path={path_file_or_folder}', headers=self.headers)

    def publish_resource(self, path_file_or_folder):
        res = requests.put(f'{self.base_url}/resources/publish?path={path_file_or_folder}', headers=self.headers)

    def unpublish_resource(self, path_file_or_folder):
        res = requests.put(f'{self.base_url}/resources/unpublish?path={path_file_or_folder}', headers=self.headers)

    def upload_url(self, path_created_resource, url):
        res = requests.post(f'{self.base_url}/resources/upload?path={path_created_resource}&url={url}',
                            headers=self.headers)

    def empty_trash(self):
        res = requests.delete(f'{self.base_url}/trash/resources', headers=self.headers)

    def restore_resource_from_trash(self, path_file_or_folder):
        res = requests.put(f'{self.base_url}/trash/resources/restore?path={path_file_or_folder}', headers=self.headers)

    def resources_trash(self):
        res = requests.get(f'{self.base_url}/trash/resources?path=%2F&fields=_embedded.items.path',
                           headers=self.headers)
        return res.text
