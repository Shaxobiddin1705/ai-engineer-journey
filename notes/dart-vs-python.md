# Dart ↔ Python: comprehension, slicing, unpacking, f-string

> D004 · 2026-11-07 · Hafta 01

## 1. Comprehension

| Tushuncha | Dart | Python | Farqi / tuzoq |
|---|---|---|---|
| List: filter + transform | `[for (var x in xs) if (x > 0) x * 2]` | `[x * 2 for x in xs if x > 0]` | Python'da **ifoda birinchi** yoziladi, `for`/`if` keyin |
| Dict (Map) | `{for (var u in users) u: u.length}` | `{u: len(u) for u in users}` | Deyarli bir xil |
| Set | `{for (var x in xs) x % 3}` | `{x % 3 for x in xs}` | Python'da bo'sh `{}` — bu **dict**, bo'sh set: `set()` |
| Ichma-ich (flatten) | `[for (var r in m) for (var x in r) x]` | `[x for r in m for x in r]` | `for` tartibi oddiy ichma-ich sikl bilan bir xil: tashqi → ichki |
| Lazy (dangasa) ketma-ketlik | `xs.where((x) => x > 0).map((x) => x * 2)` | `(x * 2 for x in xs if x > 0)` | `()` — generator expression, list emas. Bir marta aylanadi |
| if/else ifodada | `[for (var x in xs) x > 0 ? '+' : '-']` | `['+' if x > 0 else '-' for x in xs]` | Ternary `for`dan **oldin** yoziladi; filtrlovchi `if` esa keyin |

## 2. Slicing

| Tushuncha | Dart | Python | Farqi / tuzoq |
|---|---|---|---|
| Bo'lak olish | `xs.sublist(1, 4)` | `xs[1:4]` | `stop` kirmaydi (ikkalasida ham) |
| Boshidan n ta | `xs.sublist(0, 3)` / `xs.take(3)` | `xs[:3]` | |
| Oxiridan n ta | `xs.sublist(xs.length - 3)` | `xs[-3:]` | Python'da manfiy indeks oxiridan sanaydi |
| Oxirgi element | `xs.last` | `xs[-1]` | Dart'da `xs[-1]` → `RangeError` |
| Qadam (step) | Yo'q: `[for (var i = 0; i < xs.length; i += 2) xs[i]]` | `xs[::2]` | `[start:stop:step]` |
| Teskari | `xs.reversed.toList()` | `xs[::-1]` yoki `list(reversed(xs))` | |
| String teskari | `s.split('').reversed.join()` | `s[::-1]` | String ham sequence — slice ishlaydi |
| Chegaradan chiqish | `xs.sublist(0, 100)` → `RangeError` | `xs[0:100]` → xato yo'q, borini qaytaradi | Indeks (`xs[100]`) esa Python'da ham `IndexError` |
| Nusxa olish | `[...xs]` / `List.of(xs)` | `xs[:]` / `xs.copy()` / `list(xs)` | Ikkalasida ham nusxa **sayoz (shallow)** |

## 3. Unpacking

| Tushuncha | Dart (3.0+) | Python | Farqi / tuzoq |
|---|---|---|---|
| Almashtirish (swap) | `(a, b) = (b, a);` | `a, b = b, a` | Vaqtinchalik o'zgaruvchi kerak emas |
| Tuple/record yoyish | `var (name, age) = ('Ali', 25);` | `name, age = ('Ali', 25)` | |
| Bosh + qolgani | `var [first, ...rest] = xs;` | `first, *rest = xs` | `rest` — har doim list |
| Bosh, o'rta, oxir | `var [first, ...mid, last] = xs;` | `first, *mid, last = xs` | |
| Soni mos kelmasa | Compile/runtime xato | `ValueError: too many values to unpack` | `*` bo'lmasa soni aniq mos kelishi shart |
| Map aylanish | `for (var MapEntry(:key, :value) in m.entries)` | `for k, v in m.items():` | |
| Indeks bilan aylanish | `for (var (i, x) in xs.indexed)` | `for i, x in enumerate(xs, start=1):` | `enumerate` boshlang'ich raqamni oladi |
| Ikki ro'yxatni juftlash | `for (var i = 0; i < a.length; i++) (a[i], b[i])` | `for x, y in zip(a, b):` | `zip` qisqasi tugaganda to'xtaydi |
| Argumentlarni yoyish | `Function.apply(f, args)` | `f(*args, **kwargs)` | Python'da juda keng ishlatiladi |
| Collection'larni birlashtirish | `[...a, ...b]`, `{...m1, ...m2}` | `[*a, *b]`, `{**m1, **m2}` | Dart `...` ↔ Python `*` / `**` |

## 4. f-string

| Tushuncha | Dart | Python | Farqi / tuzoq |
|---|---|---|---|
| Interpolatsiya | `'Salom, $name'` | `f"Salom, {name}"` | Python'da `f` prefiksi **shart**, bo'lmasa `{name}` matn bo'lib qoladi |
| Ifoda | `'${a + b}'` | `f"{a + b}"` | |
| Kasr xonalari | `x.toStringAsFixed(2)` | `f"{x:.2f}"` | Formatlash qoidasi `:` dan keyin |
| Chapga tekislash | `name.padRight(12)` | `f"{name:<12}"` | `<` chap, `>` o'ng, `^` markaz |
| O'ngga tekislash | `'$n'.padLeft(10)` | `f"{n:>10}"` | |
| Ming ajratgich | Core'da yo'q (`intl` → `NumberFormat`) | `f"{n:,}"` → `15,000` | |
| Foiz | `'${(er * 100).toStringAsFixed(2)}%'` | `f"{er:.2%}"` → `3.45%` | Python o'zi 100 ga ko'paytiradi |
| Birlashtirilgan | — | `f"{n:>10,}"` | Tekislash + ajratgich birga |
| Debug | Yo'q | `f"{x=}"` → `x=5` | Tez debug uchun juda qulay |
| Ko'p qatorli | `'''...'''` | `"""..."""` (yoki `f"""..."""`) | |

## Asosiy tuzoqlar (eslab qolish uchun)

1. Comprehension'da ifoda **oldinda**: `[ifoda for x in xs if shart]`.
2. `{}` — bo'sh **dict**, bo'sh set emas.
3. Slice chegaradan chiqsa xato bermaydi, indeks esa beradi.
4. `xs[:]` — yangi list, lekin ichidagi obyektlar o'sha-o'sha (shallow).
5. `*` unpacking'da "qolganini list qil", chaqiruvda "yoyib ber" degani.
6. f-string'da `f` ni unutmang.
