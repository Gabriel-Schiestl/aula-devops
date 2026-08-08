def calcular_total(itens, desconto_percentual=0, cupom=None):
    """
    Calcula o total de uma compra.

    Cada item representa uma tupla no formato:
    (preco_unitario, quantidade)
    """
    if not 0 <= desconto_percentual <= 100:
        raise ValueError("O desconto precisa estar entre 0 e 100.")

    subtotal = sum(
        preco_unitario * quantidade
        for preco_unitario, quantidade in itens
    )

    desconto_total = desconto_percentual + obter_desconto_cupom(cupom)
    desconto_total = min(desconto_total, 100)

    total = subtotal - (subtotal * (desconto_total / 100))
    #teste
    return round(total, 2)

def obter_desconto_cupom(cupom):
    """
    Retorna o desconto associado a um cupom.

    Se o cupom não for válido, retorna 0.
    """
    cupons_validos = {
        "DEVOPS10": 10,
    }

    return cupons_validos.get(cupom, 0)
