import requests
import json
from random import randint
from decorator import print_status_code

class PetMethod:
    URL = "https://petstore.swagger.io/v2/pet"

    def get_pet(self, pet_id: int) -> dict | str:
        url = f"{self.URL}/{pet_id}"
        response = requests.get(url=url)
        if response.status_code != 200:
            return "Eror"
        return response.json()

    @print_status_code
    def add_pet(
            self,
            name: str,
            status: str,
            category_name: str,
            tag: str
    ):
        headers = {
            'Content-Type': 'application/json'
        }
        body = {
            'id': randint(0, 100),
            'category': {
                'id': randint(0, 100),
                'name': category_name,
            },
            'name': name,
            'tags': [{'name': tag}],
            'status': status,
            'photoUrls': ['https://randompicture.xyz/']
        }
        response = requests.post(url=self.URL, data=json.dumps(body), headers=headers)
        if response.status_code != 200:
            return None, response.status_code
        return response.json(), response.status_code

    @staticmethod
    def write_to_json(data, file_name="my_pet.json"):
        with open(file_name, 'w', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False, indent=3)
