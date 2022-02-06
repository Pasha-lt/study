# Задача на паттерн Адаптер
# Вам даётся класс Square и функция calculate_area(), которая вычисляет площадь прямоугольника.

# Чтобы была возможность передавать экземпляр класса Square в метод calculate_area(),
# вам необходимо реализовать класс SquareToRectangleAdapter. 

# Это адаптер принимает экземпляр квадрата и адаптирует его таким образом,
# что экземпляр этого адаптера можно будет передавать в метод calculate_area().



#class Square:
#    def __init__(self, side=0):
#        self.side = side

#def calculate_area(rc):
#    return rc.width * rc.height

#class SquareToRectangleAdapter:
#    def __init__(self, square):
        # TODO


class Square:
    def __init__(self, side=0):
        self.side = side

def calculate_area(rc):
    return rc.width * rc.height

class SquareToRectangleAdapter:
    def __init__(self, square):
        self.square = square
        
    @property    
    def width(self):
        return self.square.side
        
    @property    
    def height(self):
        return self.square.side
    
