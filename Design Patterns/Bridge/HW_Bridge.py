# Задача на паттерн Мост
# Вам дана иерархия наследования, проблема которой заключается в необходимости реализации огромного количества классов.
# Необходимо провести рефакторинг этой иерархии, задав в базовом классе Shape конструктор, принимающий интерфейса Renderer, объявленный как:

# class Render(ABC)
#    @property
#    def what_to_render_as(self): 
#        return None

# VectorRenderer и RasterRenderer так же должны оперировать через интерфейс Renderer.
# Каждый наследник класса Shape должен иметь конструктор, принимающий Renderer и реализованный таким образом,
# что вызовы __str__() на экземплярах этих наследников должны работать корректно. Например:
# str(Triangle(RasterRenderer()) # returns "Drawing Triangle as pixels"

# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too

# class Renderer(ABC):
#     @property
#     def what_to_render_as(self):
#         return None
        
# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer


from abc import ABC

class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


class Shape(ABC):
    def __init__(self, renderer, name):
        self.renderer = renderer
        self.name = name

    def __str__(self):
        return 'Drawing %s as %s' % (self.name, self.renderer.what_to_render_as)


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Triangle')


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Square')


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'pixels'


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'lines'
