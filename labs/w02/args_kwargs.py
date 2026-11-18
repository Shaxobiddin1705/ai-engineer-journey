def average(*numbers) -> float:
    # numbers empty or not ekanligini tekshiradi
    if not numbers:
        return 0
    return sum(numbers)/len(numbers)

def format_price(amount, *, currency, decimals) -> str:
    return f'{amount:,.{decimals}f} {currency}'.replace(',', ' ')

def create_order(product_id, **options) -> dict:
    expected_keys = ('quantity', 'color', 'size')

    for key in options:
        if key not in expected_keys:
            raise TypeError( f"{key} - kutilgan kalitlar qatorida yo'q")
        else:
            result = {'product_id': product_id}

    result = {'product_id': product_id,'quantity': options.get('quantity', 1)}
    if 'color' in options:
        result['color'] = options['color']
    if('size' in options):
        result['size'] = options['size']
    return result

def add_tag(tags=[]):
    tags.append(1)
    return tags

def add_tag_fixed(tag, tags=None):
    tags.append(tag)
    return tags

def call_and_log(func, *args, **kwargs):
    return func(*args, **kwargs)

def main():
    # average function
    assert average(1, 2, 3, 4, 5, 6, 7) == 4
    assert average() == 0

    # format price function
    assert format_price(1200000, currency = 'UZS', decimals = 0) == '1 200 000 UZS'
    assert format_price(12000, currency = 'USD', decimals = 2) == '12 000.00 USD'

    # create order
    assert create_order(10, color='red', size = 'S') == {'product_id': 10, 'quantity': 1, 'color': 'red', 'size': 'S'}
    assert create_order(4, **{"size": 'M'}) == {'product_id': 4, 'quantity': 1, 'size': 'M'}
    assert create_order(0) == {'product_id': 0, 'quantity': 1}

    # Mutable default
    assert add_tag(tags=[0, 2]) == [0, 2, 1]
    assert add_tag(tags=[5, 6]) == [5, 6, 1]
    # print(add_tag.__defaults__)
    assert add_tag_fixed(10, tags=[1, 2, 3]) == [1, 2, 3, 10]
    assert add_tag_fixed(0, tags=[5, 6]) == [5, 6, 0]

    assert call_and_log(format_price, 120, currency="USD", decimals=2) == "120.00 USD"

if __name__ == '__main__':
    main()
