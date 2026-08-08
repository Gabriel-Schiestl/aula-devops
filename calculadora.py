def calcular_total(itens, desconto_percentual=0, cupom=None):
    """
    Calcula o total de uma compra.

    Cada item representa uma tupla no formato:
    (preco_unitario, quantidade)

    O desconto percentual é aplicado sobre o subtotal da compra.

    Se um cupom válido for fornecido, o desconto associado ao cupom
    será adicionado ao desconto percentual.
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
    Retorna o desconto associado a um cupom (em percentual).

    Se o cupom não for válido, retorna 0.
    """
    if cupom is None:
        return 0
    if not isinstance(cupom, str):
        return 0

    cupons_validos = {
        "DEVOPS10": 10,
    }

    return cupons_validos.get(cupom.strip().upper(), 0)
