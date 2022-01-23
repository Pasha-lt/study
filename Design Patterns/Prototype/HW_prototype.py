# Даны класса Point (точка) и Line (линия). Реализуйте метод deep_copy для создания глубокой копии объекта Line.
# Этот метод должен возвращать копию объекта Line со скопированными начальной и конечной точками.
# Примечание: не путайте deep_copy() с __deepcopy__()


#class Point:
#    def __init__(self, x=0, y=0):
#        self.x = x
#        self.y = y

#class Line:
#    def __init__(self, start=Point(), end=Point()):
#        self.start = start
#        self.end = end

#    def deep_copy(self):
#        TODO




class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        start = Point(self.start.x, self.start.y)
        end = Point(self.end.x, self.end.y)  
        return Line(start, end)
      
      
