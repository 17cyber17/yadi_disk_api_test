import requests

class API():
    def __init__(self):
        self.base_url = 'https://cloud-api.yandex.net/v1/disk'
        self.headers = {'Authorization': 'AgAAAAARY09qAADLWzX1TShKB0zKjjC7hLBzxt4'}

    def create_folder(self, path_to_folder):
        res = requests.put(f'{self.base_url}/resources?path={path_to_folder}', headers=self.headers)
        print(res)

    def create_copy_file_or_folder(self, path_copied_resource, path_created_resource):
        res = requests.post(f'{self.base_url}/resources/copy?from={path_copied_resource}&path={path_created_resource}',
                            headers=self.headers)
        print(res)

    def move_file_or_folder(self, path_resource_move, path_created_resource):
        res = requests.post(f'{self.base_url}/resources/move?from={path_resource_move}&path={path_created_resource}',\
                            headers=self.headers)
        print(res)

    def delete_file_or_folder(self, path_file_or_folder):
        res = requests.delete(f'{self.base_url}/resources?path={path_file_or_folder}', headers=self.headers)
        print(res)

    def publish_resource(self, path_file_or_folder):
        res = requests.put(f'{self.base_url}/resources/publish?path={path_file_or_folder}', headers=self.headers)
        print(res)

    def unpublish_resource(self, path_file_or_folder):
        res = requests.put(f'{self.base_url}/resources/unpublish?path={path_file_or_folder}', headers=self.headers)
        print(res)

    def upload_url(self, path_created_resource, url):
        res = requests.post(f'{self.base_url}/resources/upload?path={path_created_resource}&url={url}',\
                            headers=self.headers )
        print(res)

    def empty_trash(self):
        res = requests.delete(f'{self.base_url}/trash/resources', headers=self.headers)
        print(res)

    #Этот запрос я не смог  заставить работать даже на полигоне яндекса.
    #Написал в поддержку по этому  поводу.
    def restore_resource_from_trash(self, path_file_or_folder):
        res = requests.put(f'{self.base_url}/trash/resources/restore?path={path_file_or_folder}', headers=self.headers)
        print(res)