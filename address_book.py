from collections import UserDict
from record import Record


class AddressBook(UserDict):

    def __str__(self):
        result=["AddressBook:"]
        for name, record in self.data.items():
            result.append(f"{name}: {record}")
        return "\n".join(result)

    def add_record(self, record)-> None:
        self.data[record.name.value] = record

    def find(self, name:str)-> Record|None:
        return self.data.get(name, None)

    def delete(self, name: str) -> None | str:
        if self.data.pop(name, None) is None:
            return f"{name} not found in your AddressBook"

