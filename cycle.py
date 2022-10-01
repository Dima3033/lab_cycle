p=int(input("Введіть  число 1 - "))
g=int(input("Введіть  число 2 - "))
temp = p
p = g
g = temp
while p>g:
    p-=1
    print(f'{p}')
