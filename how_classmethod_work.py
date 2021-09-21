class Pupil():
    class_l = 10
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    @classmethod
    def class_change_cls(cls, class_new):
        '''Изменит у всех экземпляров так как у нас class_l находиться без self'''
        cls.class_l = class_new
        
    def class_change_self(self, class_new_self):
        '''self изменит только у текущего экземпляра.'''
        class_l = class_new_self
        
        
a = Pupil('Андрей', 'Скороходов')
b = Pupil('Борис', 'Стасов')
print(a.class_l) # 10
print(b.class_l) # 10
Pupil.class_change_cls(9)
print(a.class_l) # 9
print(b.class_l) # 9
a.class_change_self(20)
print(a.class_l) # 9
print(b.class_l) # 9
