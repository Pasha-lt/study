#пишем условие чтобы проверить задан ли у нас первый параметр  if [ $1 != “” ] - важно соблюдать пробелы,
# затем пишем then ставим 4 пробела и пишем что выполнится если условие будет верным закрываем код написав обратный if -> fi
#если мы введем этот скрипт без параметра который пойдет в $1 то нам выдаст ошибку ./script.sh: line 2: [: !=: unary operator expected
#для того чтобы такого избежать помещаем $1 в двойные кавычке if [ “$1” != “” ] теперь если не передадим первый параметр то у нас скрипт отработает но ничего не выведет. 

#Скрипт1

#!/usr/bin/env bash
if [ $1 != "" ]
then
    echo 'Привет Андрей'
fi

#Также мы можем добавить к ‘if’ ещё и ‘else’ он отработает если основное условие не сработало. 

#Скрипт 2
#!/usr/bin/env bash
if [ "$1" != "" ]
then
    echo 'Привет Андрей'
else
    echo 'А где Андрей?'
fi