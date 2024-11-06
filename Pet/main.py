import json

from Pet.pet_method import PetMethod

pet_shop = PetMethod()

pet_id, status_code = pet_shop.add_pet(
    name= 'Boby',
    status= 'poop',
    category_name= 'cat',
    tag= 'little'
)

if status_code == 200:
    print("Питомец добавлен с ID:", pet_id.get("id"))

    pet = pet_shop.get_pet(pet_id=pet_id.get("id"))
    print("Информация о питомце:", json.dumps(pet, indent=3, ensure_ascii=False))

    pet_shop.write_to_json(pet, "my_pet.json")
else:
    print("Ошибка при добавлении питомца. Код статуса:", status_code)

