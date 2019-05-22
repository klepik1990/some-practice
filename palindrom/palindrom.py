def revers(text):
    '''
    :param text:
    :return:
    '''
    return text[::-1]

def palindrom(text):
    '''
    :param text:
    :return:
    '''
    return text==revers(text)

punctuation = (',', '.', ' ', '!', '?', '*', '(', ')')
no_punctuation = []
some_input= input('Введите текст:')

for i in some_input.lower():
    if i not in punctuation:
        no_punctuation += i

if palindrom(no_punctuation):
    print('Это палиндром')
else:
    print('Нет, не палиндром')

print(no_punctuation)