# Написать по 3 теста на структуры данных SET и INT
import pytest

# Тестирование структуры int


# тест 1 на корректность работы int()
@pytest.mark.parametrize("test_input, expected_result", [(2, 2), (-2, -2), (0, 0)])
def test_int_positive_normal_input(test_input, expected_result):
    assert int(test_input) == expected_result


# тест 2 на преобразоватния str,float в int
@pytest.mark.parametrize("test_input, expected_result", [(2.5, 2), (-2.5, -2),
                                                         ('4', 4), ('-6', -6)])
def test_int_positive_strange_input(test_input, expected_result):
    assert int(test_input) == expected_result


# тест 3(негативный) на TypeError для преобразования списка из 1 символа в int
def test_int_negative_error():
    try:
        assert int([1]) == 1
    except TypeError:
        pass


#  Тестирование структуры set


# Проверочный тест 1 на корректность работы set()
@pytest.mark.parametrize("test_input, expected_result", [(['hello', 'daddy', 'hello', 'mum'], {'hello', 'daddy', 'mum'}),
                                                         ('abbc', {'b', 'a', 'c'})])
def test_set_positive_normal_input(test_input, expected_result):
    assert set(test_input) == expected_result


# тест 2 на корректность работы метода .discard()
def test_set_positive_method_discard():
    num_set = {1, 2, 3, 4, 5, 6}
    num_set.discard(3)
    assert num_set == {1, 2, 4, 5, 6}


# тест 3(негативный) на удаление из пустого множества KeyError
def test_set_negative_error():
    test_input = set()
    try:
        assert test_input.pop() == 0
    except KeyError:
        pass