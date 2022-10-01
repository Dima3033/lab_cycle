p=int(input("Введіть  число 1 - "))
g=int(input("Введіть  число 2 - "))
if p%2==1:
    p+=1
while p<g:
    print(f'{p}')
    p+=2
else:
    print('робота завершена')
