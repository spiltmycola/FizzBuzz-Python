def stringGen(num):
    string = ''
    mod = False
    if num % 3 == 0:
        string += 'Fizz'
        mod = True
    if num % 5 == 0:
        string += 'Buzz'
        mod = True
    if mod == False:
        string = str(num)
    return string

for i in range(1, 100):
    print(stringGen(i) + ' ')