from pytest import mark


def add_two_elements(a, b):
    return a + b


@mark.parametrize(
    'a,b,expected', [
        (0, 0, 0),
        (1, 0, 1),
        (0, 1, 1),
        (1, 1, 2),
        (1, 2, 3),
        (1, 10, 11),
        (113, 3, 116)
    ]
)
def test_with_param(a, b, expected):
    assert add_two_elements(a, b) == expected


@mark.parametrize(
    'tv_brand', [
        ('Samsung'),
        ('Sony'),
        ('Apple')
    ]
)
def test_television_turned_on(tv_brand):
    print(f"{tv_brand} is turned on")


@mark.ok
def test_browser_can_navigate_to_training_ground(browser):
    browser.get('http://techstepcademy.com/training-ground')
