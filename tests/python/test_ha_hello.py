from ha_hello.ha_hello import HaSecretWeapon


def test_ha_hello_init():
    ha_hello = HaSecretWeapon()
    assert ha_hello is not None


def test_ha_hello_add():
    ha_hello = HaSecretWeapon()
    assert ha_hello.add(1, 2) == 3


def test_ha_hello_get_book_id():
    ha_hello = HaSecretWeapon()
    assert ha_hello.get_book_id() == 1


def test_ha_hello_get_book_name():
    ha_hello = HaSecretWeapon()
    assert ha_hello.get_book_name() == 2


def test_ha_hello_get_book_author():
    ha_hello = HaSecretWeapon()
    assert ha_hello.get_book_author() == 3


def test_ha_hello_get_book_price():
    ha_hello = HaSecretWeapon()
    assert ha_hello.get_book_price() == 4


def test_ha_hello_get_book_content():
    ha_hello = HaSecretWeapon()
    assert ha_hello.get_book_content() == 5
