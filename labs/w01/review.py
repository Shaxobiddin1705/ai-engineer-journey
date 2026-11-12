import copy

"""
Listdan nusxa ko'chirishda e'tiborli bo'lish kerak. Listni shunchaki ko'chirishda list reference orqali nusxa ko'chiriladi.
Agar listni o'zgartirsak, asl list ham o'zgaradi.
Agar asl listni o'zgartirmasdan nusxa olish kerak bo'lsa, deepcopy() metodidan foydalanish kerak.
"""
def aliasing():
    a = [1, 2]
    b = a
    b.append(3)
    # print(a)

    c = copy.deepcopy(a)
    c.append(10)
    print(f'a: {a}\nc: {c}')

"""
Pythonda list hech qanchon dic uchun key bo'lolmaydi. Chunki list dic uchun unhashable type
"""
def unsupported_dic_key():
    dic1 = {[1, 2, 3]: 'new_list'}
    print(dic1)

def comprehension():
    nums = [1, 2, 3, 4, 5]
    sq = [n *n for n in nums if n % 2]
    print(sq) # [1, 9, 25]

    lens = {w: len(w) for w in ['uz', 'ru', 'en']}
    print(lens)

def main():
    # aliasing()
    # unsupported_dic_key()
    comprehension()

if __name__ == "__main__":
    main()
