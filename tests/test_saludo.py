def saludar(nombre):
    return f"Hola {nombre}"

def test_saludar():
    assert saludar("Ana") == "Hola Ana"