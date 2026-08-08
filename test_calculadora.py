import pytest

from calculadora import calcular_total


def test_total_sem_desconto():
    itens = [(10.0, 2), (5.0, 1)]

    assert calcular_total(itens) == 25.0


def test_total_com_dez_por_cento_de_desconto():
    itens = [(100.0, 2), (50.0, 1)]

    assert calcular_total(itens, desconto_percentual=10) == 225.0


def test_desconto_invalido():
    with pytest.raises(ValueError):
        calcular_total([(100.0, 1)], desconto_percentual=110)


def test_total_com_cupom():
    itens = [(100.0, 2), (50.0, 1)]

    assert calcular_total(itens, cupom="DEVOPS10") == 225.0

def test_total_com_cupom_e_desconto():
    itens = [(100.0, 2), (50.0, 1)]

    assert calcular_total(itens, desconto_percentual=5, cupom="DEVOPS10") == 212.5

def test_nao_deve_ultrapassar_100_por_cento_de_desconto():
    itens = [(100.0, 2), (50.0, 1)]

    assert calcular_total(itens, desconto_percentual=95, cupom="DEVOPS10") == 0.0

def test_total_com_cupom_invalido():
    itens = [(100.0, 2), (50.0, 1)]

    assert calcular_total(itens, cupom="INVALIDO") == 250.0
