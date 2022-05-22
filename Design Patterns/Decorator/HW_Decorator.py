# Вам даны два типа: Circle и Square. Так же дан декоратор ColoredShape.
# Декоратор добавляет цвет к строке, описывающий объект определённой фигуры.
# Однако, тут есть место для трюка:
# дело в том, что у декоратора есть метод resize(), который должен изменять размер хранимой в нём фигуры, 
# но при этом только в классе Circle есть метод resize(), а в Square его нет.
# Требуется дополнить предложенный шаблон реализации без добавления метода resize в класс Square!
# Вот пример юнит-теста, проверяющего API, который вам надо реализовать.

Class Evaluate(TestCase):
  def test_circle(self):
    circle = ColoredShape(Circle(5), "red")
    self.asserEqual("A circle of radius 5 has the color red", str(sircle))

    circle.resize(2)
    self.assertEqual("A circle of radius 10 has the color red", str(sircle))    
    
class Circle:
  def __init__(self, radius):
    self.radius = radius

  def resize(self, factor):
    self.radius *= factor

  def __str__(self):
    # todo

class Square:
  def __init__(self, side):
    self.side = side

  def __str__(self):
    # todo


class ColoredShape:
  def __init__(self, shape, color):
    self.color = color
    self.shape = shape

  def resize(self, factor):
    # todo
    # note that a Square doesn't have resize()

  def __str__(self):
    # todo

    
 # решение

class Circle:
  def __init__(self, radius):
    self.radius = radius

  def resize(self, factor):
    self.radius *= factor

  def __str__(self):
    return 'A circle of radius %s' % self.radius

class Square:
  def __init__(self, side):
    self.side = side

  def __str__(self):
    return 'A square with side %s' % self.side


class ColoredShape:
  def __init__(self, shape, color):
    self.color = color
    self.shape = shape

  def resize(self, factor):
    r = getattr(self.shape, 'resize', None)
    if callable(r):
      self.shape.resize(factor)

  def __str__(self):
    return "%s has the color %s" %\
           (self.shape, self.color)
