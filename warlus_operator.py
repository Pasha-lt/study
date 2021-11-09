my_string = "Привет Андрей как дела"
if (n := len(my_string)) > 10:
    print(f'В строке ожидаеться 10 или меньше символов, а помало {n}')
    
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
