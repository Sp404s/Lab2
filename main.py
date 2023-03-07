word = ''
str = ''
while word != 'stop':
    word = input('Введите слово: ')
    if word != 'stop':
        str += word
        str += ' '
print(str)