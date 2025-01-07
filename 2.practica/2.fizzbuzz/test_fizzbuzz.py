from fizzbuzz import getFizzbuzz

def test_getFizzbuzz_output():
    # Llamar a la función con un rango pequeño
    output = getFizzbuzz(1, 16)

    # Salida esperada
    expected_output = [
        "1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz",
        "11", "fizz", "13", "14", "fizzbuzz", "16",
    ]

    # Comparar los resultados
    assert output == expected_output