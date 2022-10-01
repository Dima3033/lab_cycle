p=int(input("Введіть  число 1 - "))
g=int(input("Введіть  число 2 - "))
if p >g:
    temp = p
    p=g
    g=temp
elif p%2==0:
    p+=1
while p<g:
    print(f'{p}')
    p+=1


