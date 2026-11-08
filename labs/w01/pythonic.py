def ex01_list_comprehension():
    """
    List comprehension yordamida 1000 dan katta bo'lgan view qiymatlarini
    1000 ga bo'lib, faqat butun qismini olish va natijalarni yangi listga joylashtirish.
    Misol uchun, 1200 // 1000 --> 1
    """
    views = [1200, 5400, 300, 8900, 4100, 760, 15000, 2300, 990, 6700]
    result = [view // 1000 for view in views if view > 1000]
    print(result)


def ex02_dict_comprehension():
    users = ["ali_vlog", "zarina.uz", "tech_bek", "momo"]
    dic = {user_name: len(user_name) for user_name in users}
    print(dic)


def ex03_flatten():
    nested_list = [[1, 2], [3, 4], [5]]
    list = [item for sublist in nested_list for item in sublist]
    print(list)


def ex04_slicing_list():
    views = [1200, 5400, 300, 8900, 4100, 760, 15000, 2300, 990, 6700]
    # boshidagi 3 ta elementni olish
    print(views[:3])
    # oxiridagi 3 ta elementni olish
    print(views[-3:])


def ex05_slicing_str():
    print(is_palindrome("radar"))  # True
    print(is_palindrome("HeL:Lo"))  # False


def is_palindrome(s: str) -> bool:
    """
    Berilgan string palindrom ekanligini tekshiradi.
    Palindrom - bu orqaga o'qilganda ham bir xil bo'lgan so'z yoki ibora.
    Misol uchun, "radar" palindromdir, chunki u orqaga o'qilganda ham "radar" bo'ladi.
    """
    # Barcha harflarni kichik harflarga o'tkazish va faqat harflarni olish
    cleaned_s = "".join(filter(str.isalpha, s.lower()))
    print(f"cleaned_s = {cleaned_s}")
    print(f"cleaned_s[::-1] = {cleaned_s[::-1]}")
    return cleaned_s == cleaned_s[::-1]


def ex06_unpacking():
    x, y = (1, 2)
    print(f"x = {x}, y = {y}")
    y, x = (x, y)
    print(f"x = {x}, y = {y}")

    views = [1200, 5400, 300, 8900, 4100, 760, 15000, 2300, 990, 6700]
    first, middle, last = views[0], views[1:-1], views[-1]
    print(f"first = {first}, middle = {middle}, last = {last}")


def ex07_unpacking_with_dic():
    stats = {"ali_vlog": 15000, "zarina.uz": 8900, "tech_bek": 4100}
    for index, (user, view) in enumerate(stats.items()):
        print(f"{index + 1}. {user} --> {view} ")


def ex08_f_string():
    stats = {"ali_vlog": 15000, "zarina.uz": 8900, "tech_bek": 4100}
    for user, view in stats.items():
        print(f"{user=:<12} --> {view:>10,} = {(view / 1000):.2%}")


def main() -> None:
    # ex01_list_comprehension()
    # ex02_dict_comprehension()
    # ex03_flatten()
    # ex04_slicing_list()
    # ex05_slicing_str()
    # ex06_unpacking()
    # ex07_unpacking_with_dic()
    ex08_f_string()


if __name__ == "__main__":
    main()
