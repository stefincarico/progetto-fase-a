# test_calculator.py
from calculator import add,subtract, divide
import pytest

# Nota il nome della funzione che inizia con "test_"
def test_add_two_positive_numbers():
    # 1. arrange
    num1 = 5
    num2= 7

    # 2. Act (Agisci)
    result = add(num1, num2)

    # 3. Assert (Verifica)
    assert result == 12

def test_add_positive_and_negative_number():
    assert(add(10,-5)) == 5

def test_add_is_intentionally_wrong():
    assert(add(1,2)) == 3 # lo sappiamo già che è sbagliato. il test DEVE fallire AGGIORNATO PER GREEN

def test_subtract_two_number():
    assert(subtract(5,3)) == 2


@pytest.mark.parametrize("a, b, expected_result", [
    (2, 3, 6),         # Caso 1: due positivi
    (-1, 5, -5),       # Caso 2: un negativo
    (-2, -4, 8),       # Caso 3: due negativi
    (5, 0, 0),         # Caso 4: moltiplicazione per zero
])
def test_multiply(a, b, expected_result):
    # Prima importiamo la funzione che VORREMMO testare
    from calculator import multiply
    assert multiply(a, b) == expected_result

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),        # Divisione normale
    (5, 2, 2.5),       # Divisione con risultato decimale
])
def test_divide_normal_cases(a, b, expected):
    """Test per casi di divisione normali"""
    assert divide(a, b) == expected


def test_divide_by_zero():
    """Test per divisione per zero"""
    # Questo test fallirà inizialmente perché non abbiamo ancora implementato il controllo
    with pytest.raises(ValueError):
        divide(10, 0)