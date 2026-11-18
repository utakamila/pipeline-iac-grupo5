def calcular_total(preco, quantidade, desconto=0):
  total = preco * quantidade
  return total - (total * desconto)
