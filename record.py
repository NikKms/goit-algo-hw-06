from name import Name
from phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone:str)-> None:
        new_phone = Phone(phone)
        self.phones.append(new_phone)

    def remove_phone(self, phone:str)-> None:
        phone_obj = self._get_phone_or_raise(phone)
        self.phones.remove(phone_obj)

    def edit_phone(self, old_phone:str, new_phone:str)-> None:
        phone_obj = self._get_phone_or_raise(old_phone)
        phone_obj.value = new_phone

    def find_phone(self, phone:str)-> Phone|None:
        return self._find_phone_by_value(phone)

    def _find_phone_by_value(self, phone:str)-> Phone|None:
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def _get_phone_or_raise(self, phone: str)->Phone:
        phone_obj = self._find_phone_by_value(phone)
        if phone_obj is None:
            raise ValueError(f"Phone number {phone} not found")
        return phone_obj



