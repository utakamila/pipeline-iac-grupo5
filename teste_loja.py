from loja import calcular_total
def test_total_sem_desconto():
  assert calcular_total(10, 3) == 30
def test_total_com_desconto():
  assert calcular_total(100, 2, 0.1) == 180
