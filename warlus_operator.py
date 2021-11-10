## example 1
my_string = "Привет Андрей как дела"
if (n := len(my_string)) > 10:
    print(f'В строке ожидаеться 10 или меньше символов, а помало {n}')

## example 2
# Without Walrus
nums = []
num = input('Type a number: ')
while num.isdigit():
    nums.append(int(num))
    num = input('Type a number')
print(nums)

# With Walrus
nums = []
while (num := input('Type a number: ')).isdigit():
    nums.append(num)
print(nums)

## example 3
# Without Warlus
var = 5
if var == 5:
    ans = input('Type your answer: ')
    if ans != '':
        print('Nice')

# With Warlus
var = 5
if var == 5 and (ans := input('Type your answer: ') != ''):
    print(ans)
