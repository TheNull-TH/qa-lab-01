from src.estudiante import Aprobado

def test_aprobado():
    assert Aprobado(15) == "Aprobado"

def test_desaprobado():
    assert Aprobado(8) == "Desaprobado"