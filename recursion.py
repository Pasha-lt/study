# пример 1 
# поиск факториала
def fact(x):
   if x == 1: # базовый(случай при котором будет выход из рекурсии) и рекурсивный.
       return 1
   else:
       return x*fact(x-1)
# Сначала возвращается 1 потом 2 потом 3
print(fact(5))

# 2 пример
"""
Нужно рекурсивно пройти словарь и вернуть значения ключа.
"""
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(struct, key):
    if key in struct:
        return struct[key]
    
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict): #Проверяем вернулся ли нам словарь
            result = find_key(sub_struct, key)
            if result:
                break
    else:
        result = None
    return result

user_key = input('Какой ключ ищем? ')
value = find_key(site, user_key)
if value:
    print(value)
else:
    print('Такого ключа нет')
