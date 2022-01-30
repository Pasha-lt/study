#Поскольку реализовывать одиночка очень просто, у вас будет задание реализовать функцию is_singleton() . 

# Этот метод принимает фабричный метод в качестве аргумента и вам необходимо определить 
# производит ли этот фабричный метод один и тот же объект или нет. Вернуть True если да, False если нет.

#def is_singleton(factory):
    # todo: call factory() and return true or false
    # depending on whether the factory makes a
    # singleton or not


def is_singleton(factory):
    c1 = factory()
    c2 = factory()
    return c1 is c2
  
