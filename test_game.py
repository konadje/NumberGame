from game import check_guess, generate_number

def test_check_guess_correct():
    assert check_guess(42, 42) == "Угадал!"

def test_check_guess_less():
    assert check_guess(50, 30) == "Меньше"

def test_check_guess_greater():
    assert check_guess(10, 20) == "Больше"

def test_generate_number_in_range():
    num = generate_number(1, 10)
    assert 1 <= num <= 10
