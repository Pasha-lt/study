# Магический квадрат - матрица чисел, в которой сумма чисел любой строки, столбца или диагонали одинакова.
# Вам даётся проект из трёх классов, которые могут быть использованы для построения магического квадрата. 
# Это классы:
# Generate: этот класс генерирует список из девяти случайных чисел
# Splitter: это класс, который принимает двумерный список и разбивает его на все возможные одномерные списки. 
# Он даёт в результате колонки, строки и две диагонали.
# Verifier: этот класс принимает двумерный список и проверяет, что сумма чисел любого из содержимых списков одинакова.
# Вам только остаётся реализовать фасад, названный "MagicSquareGenerator" который генерирует магический квадрат заданного размера.

from random import randint

class Generator:
  def generate(self, count):
    return [randint(1,9) for x in range(count)]

class Splitter:
  def split(self, array):
    result = []

    row_count = len(array)
    col_count = len(array[0])

    for r in range(row_count):
      the_row = []
      for c in range(col_count):
        the_row.append(array[r][c])
      result.append(the_row)

    for c in range(col_count):
      the_col = []
      for r in range(row_count):
        the_col.append(array[r][c])
      result.append(the_col)

    diag1 = []
    diag2 = []

    for c in range(col_count):
      for r in range(row_count):
        if c == r:
          diag1.append(array[r][c])
        r2 = row_count - r - 1
        if c == r2:
          diag2.append(array[r][c])

    result.append(diag1)
    result.append(diag2)

    return result

class Verifier:
  def verify(self, arrays):
    first = sum(arrays[0])

    for i in range(1, len(arrays)):
      if sum(arrays[i]) != first:
        return False

    return True

class MagicSquareGenerator:
  def generate(self, size):
    # todo - return a magic square of the given size
    
    
#######solution###############

from random import randint

class Generator:
  def generate(self, count):
    return [randint(1,9) for x in range(count)]

class Splitter:
  def split(self, array):
    result = []

    row_count = len(array)
    col_count = len(array[0])

    for r in range(row_count):
      the_row = []
      for c in range(col_count):
        the_row.append(array[r][c])
      result.append(the_row)

    for c in range(col_count):
      the_col = []
      for r in range(row_count):
        the_col.append(array[r][c])
      result.append(the_col)

    diag1 = []
    diag2 = []

    for c in range(col_count):
      for r in range(row_count):
        if c == r:
          diag1.append(array[r][c])
        r2 = row_count - r - 1
        if c == r2:
          diag2.append(array[r][c])

    result.append(diag1)
    result.append(diag2)

    return result

class Verifier:
  def verify(self, arrays):
    first = sum(arrays[0])

    for i in range(1, len(arrays)):
      if sum(arrays[i]) != first:
        return False

    return True

class MagicSquareGenerator:
  def generate(self, size):
    g = Generator()
    s = Splitter()
    v = Verifier()

    while True:
      square = []
      for x in range(size):
        square.append(g.generate(size))

      if v.verify(s.split(square)):
        break

    return square
