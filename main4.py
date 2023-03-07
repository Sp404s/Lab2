import random
cor=0
z=0
while z!=3:
    a = random.randint(1,20)
    b = random.randint(1,20)
    c = int(input(f'Сколько будет {a}+{b}='))
    if c == a+b:
        print('Правельно!')
        cor+=1
    else:
        print('Не правельно.')
        z+=1
print('Игра оконечна','\nПравельных ответов: ', cor)
