from address_book import AddressBook
from record import Record


def main():
    try:
        # Створення нової адресної книги
        book = AddressBook()

        # Перевірка, чи адресна книга порожня
        print("Початкова адресна книга (має бути порожня):")
        print(book)

        # Створення запису для John
        john_record = Record("John")
        john_record.add_phone("1234567890")
        john_record.add_phone("5555555555")

        # Додавання запису John до адресної книги
        book.add_record(john_record)

        # Створення і додавання нового запису для Jane
        jane_record = Record("Jane")
        jane_record.add_phone("9876543210")
        book.add_record(jane_record)

        # Виведення всіх записів у книзі
        print("\nАдресна книга після додавання John і Jane:")
        print(book)

        # Додавання некоректного телефону
        try:
            invalid_record = Record("Invalid User")
            invalid_record.add_phone("12345abcde")  # Некоректний номер
        except ValueError as e:
            print(f"Помилка під час додавання некоректного телефону: {e}")

        # Пошук запису John
        john = book.find("John")
        if john:
            print("\nЗнайдено John:")
            print(john)

            # Редагування телефону
            try:
                john.edit_phone("1234567890", "1112223333")
                print("\nЗапис John після редагування телефону:")
                print(john)
            except ValueError as e:
                print(f"Помилка під час редагування телефону: {e}")

            # Спроба редагувати неіснуючий номер
            try:
                john.edit_phone("0000000000", "2223334444")
            except ValueError as e:
                print(f"Помилка під час редагування неіснуючого телефону: {e}")

            # Пошук конкретного телефону
            found_phone = john.find_phone("5555555555")
            if found_phone:
                print(f"\nЗнайдено телефон у записі John: {found_phone.value}")
            else:
                print("\nТелефон не знайдено у записі John.")
        else:
            print("John не знайдено в адресній книзі.")

        # Видалення телефону
        try:
            john.remove_phone("5555555555")
            print("\nЗапис John після видалення телефону:")
            print(john)
        except ValueError as e:
            print(f"Помилка під час видалення телефону: {e}")

        # Спроба видалити неіснуючий номер
        try:
            john.remove_phone("9999999999")
        except ValueError as e:
            print(f"Помилка під час видалення неіснуючого телефону: {e}")

        # Видалення запису Jane
        book.delete("Jane")
        print("\nАдресна книга після видалення Jane:")
        print(book)

        # Спроба видалити неіснуючий запис
        try:
            book.delete("Jane")
        except ValueError as e:
            print(f"Помилка під час видалення неіснуючого запису: {e}")

        # Перевірка, чи адресна книга порожня після видалення всіх записів
        book.delete("John")
        print("\nАдресна книга після видалення всіх записів (має бути порожня):")
        print(book)

    except Exception as e:
        print(f"Сталася несподівана помилка: {e}")


if __name__ == '__main__':
    main()
