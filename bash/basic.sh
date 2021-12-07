# запуск "bash script.sh"
# скрипт 1
#!/usr/bin/env bash
X="Try print this text"
echo $X

# Если мы хотим в переменную засунуть команду тогда нужно поставить знак доллара а саму команду взять в скобки  скрипт2
# date - вернет дату
#!/usr/bin/env bash
NOW=$(date)
echo $NOW
