"""D003: Python kolleksiyalari va mutability."""

import copy


def ex01_tuple_immutability():
    """
    Type ni qiymatini o'zgartirishga urinish, bu TypeError xatosini keltirib chiqaradi.
    """
    numbers = (1, 2, 3, 4, 5)
    try:
        numbers[0] = 10
    except TypeError:
        print("Tuples are immutable, you cannot change their elements.")


def ex02_list_mutable():
    """
    bitta o'zgaruvchining qiymatini boshqa o'zgaruvchiga tayinlash va keyin uni o'zgartirish,
    bu a o'zgaruvchisining qiymatini o'zgartirmaydi.
    """
    fruits = ["apple", "banana", "cherry"]
    fruits2 = fruits
    fruits2.append("orange")
    # True, both variables point to the same list object
    print(f"fruits is fruits2: {fruits is fruits2}")
    print(f"fruits id = {id(fruits)}")
    print(f"fruits2 id = {id(fruits2)}")
    print(f"fruits = {fruits}")
    print(f"fruits2 = {fruits2}")


def ex03_list_copying():
    """
    bitta o'zgaruvchining qiymatini boshqa o'zgaruvchiga tayinlash va keyin uni o'zgartirish,
    bu a o'zgaruvchisining qiymatini o'zgartirmaydi.
    """
    numbers = [1, 2, 3, 4, 5]
    numbers2 = copy.copy(numbers)
    numbers2.append(6)
    numbers3 = copy.deepcopy(numbers)
    numbers3.append(7)
    # False, both variables point to different list objects
    print(f"numbers is numbers2: {numbers is numbers2}")
    print(f"numbers is numbers3: {numbers is numbers3}")
    print(f"numbers2 is numbers3: {numbers2 is numbers3}")
    print(f"numbers id = {id(numbers)}")
    print(f"numbers2 id = {id(numbers2)}")
    print(f"numbers3 id = {id(numbers3)}")
    # print(f"numbers = {numbers}")
    # print(f"numbers2 = {numbers2}")
    # print(f"numbers3 = {numbers3}")
    assert numbers is not numbers2
    assert numbers is not numbers3
    assert numbers2 is not numbers3


def ex04_list_mutable_nested():
    """
    Nested list yaratish va uni o'zgartirish, bu barcha ichki ro'yxatlar bir xil ob'ektga ishora qilganligi sababli,
    barcha ichki ro'yxatlar bir xil qiymatga ega bo'ladi.
    """
    grid = [[0] * 3] * 3
    print(f"grid = {grid}")
    grid[0][0] = 1
    print(f"grid = {grid}")
    print(f"grid[0] is grid[1]: {grid[0] is grid[1]}")


def ex05_dict_comprehension():
    text = "salom dunyo salom python dunyo salom"
    dic = {word: text.count(word) for word in text.split()}
    print(dic)
    d1 = dic.get("salom", 0)
    d2 = dic.setdefault("salom", 0)
    assert d1 == d2


def ex06_dict_mutable_key():
    """
    Dictionary yaratishda mutable type (list) ni key sifatida ishlatishga urinish,
    bu TypeError xatosini keltirib chiqaradi.
    """
    try:
        dic = {[1, 2]: "value", (1, 2): "value"}
        print(dic)
    except TypeError as e:
        print(f"Error: {e}")
    dic = {(1, 2): "value"}
    print(dic)


def ex07_sets():
    """
    Set yaratish va setlar ustida amallar bajarish.
    1. & - Ushbu operator ikkita setning kesishmasini topadi.
    2. - - Ushbu operator birinchi setdan ikkinchi setni chiqaradi.
    3. | - Ushbu operator ikkita setning birlashmasini topadi.
    4. ^ - Ushbu operator ikkita setning simmetrik farqini topadi.
    """
    usa_cars = {
        "Fors",
        "Chevrolet",
        "Dodge",
        "Tesla",
        "Cadillac",
        "Ferrari",
        "Lamborghini",
    }
    italian_cars = {"Ferrari", "Lamborghini", "Maserati", "Fiat", "Chevrolet", "Tesla"}
    both_cars = usa_cars & italian_cars
    only_usa_cars = usa_cars - italian_cars
    at_least_one_car = usa_cars | italian_cars
    print(f"USA va Italian ikkalasida mavjud bo'lgan avtomobillar: {both_cars}")
    print(f"USA da faqat, Italian da yo'q bo'lgan avtomobillar: {only_usa_cars}")
    print(f"Eng kamida birida mavjud bo'lgan avtomobillar: {at_least_one_car}")


def ex08_list_to_set():
    numbers = [3, 1, 3, 2, 1]
    print(f"Set: {set(numbers)}")
    dic = {number: str(number) for number in set(numbers)}
    print(dic)


def ex09_mutable_immutable_value_function():
    numbers = [1, 2, 3, 4, 5]
    print(f"List of numbers before ex09_helper: {numbers}")
    ex09_helper(numbers)
    print(f"list of numbers outside ex09: {numbers}")

    number = 10
    print(f"Number before ex09_helper: {number}")
    ex09_helper2(number)
    print(f"Number outside ex09: {number}")


def ex09_helper(numbers):
    numbers.append(6)
    print(f"Inside ex09_helper: {numbers}")


def ex09_helper2(number):
    number += 1
    print(f"Inside ex09_helper2: {number}")


def ex10_tuple_mutable_elements():
    """
    Tuple ichida mutable elementlar (masalan, list) bo'lishi mumkin, lekin tuple o'zi immutable hisoblanadi.
    1. Tuple ichidagi list elementini o'zgartirishga urinish TypeError xatosini keltirib chiqaradi.
    2. Tuple ichidagi list elementini append qilish orqali o'zgartirish mumkin, chunki list mutable hisoblanadi.
    3. Tuple ichidagi list elementini o'zgartirish tuple o'zi immutable bo'lishiga qaramay, listning o'zgarishi mumkin.
    """
    try:
        t = (1, [2, 3])
        t[1] += [4]
    except TypeError as e:
        print(f"Error: {e} {t}")

    t2 = (1, [2, 3])
    t2[1].append(4)
    print(t2)


def main() -> None:
    # ex01_tuple_immutability()
    # ex02_list_mutable()
    # ex03_list_copying()
    # ex04_list_mutable_nested()
    # ex05_dict_comprehension()
    # ex06_dict_mutable_key()
    # ex07_sets()
    # ex08_list_to_set()
    # ex09_mutable_immutable_value_function()
    ex10_tuple_mutable_elements()


if __name__ == "__main__":
    main()
