from src.calculadora import sumar
from src.calculadora import es_par
import pytest
from src.calculadora import dividir

def test_dividir():
    assert dividir(10, 2) == 5

def test_division_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)

def test_es_par():
    assert es_par(4) == True

def test_sumar():
    assert sumar(2, 3) == 5