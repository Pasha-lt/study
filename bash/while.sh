#!/usr/bin/env bash
COUNTER=0
while [[ $COUNTER -lt 10 ]]
do
    echo "The counter is $COUNTER"
    let COUNTER=COUNTER+1
done

# Обработка входящих параметров вызов bash script.sh 23 35 'два'
#!/usr/bin/env bash
while [ "$1" != "" ]
do
    echo "Parameter equals $1"
    shift
done
