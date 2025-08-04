from app.logic import escolher_garrafas

def test_caso_sem_sobra():
    result, sobra = escolher_garrafas(7, [1, 3, 4.5, 1.5, 3.5])
    assert sobra == 0
    assert sorted(result) == sorted([1, 4.5, 1.5])

def test_caso_com_sobra():
    result, sobra = escolher_garrafas(5, [1, 3, 4.5, 1.5])
    assert sobra == 0.5
    assert sorted(result) == sorted([1, 4.5])

def test_pequeno_ajuste():
    result, sobra = escolher_garrafas(4.9, [4.5, 0.4])
    assert sobra == 0
    assert sorted(result) == sorted([4.5, 0.4])