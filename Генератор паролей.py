from random import *
global digits, lowercase_letters, uppercase_letters, punctuation
digits = '0123456789'
lowercase_letters = 'loabcdefghijkmnpqrstuvwxyz'
uppercase_letters = 'OABCDEFGHIJKLMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

def pass_gen():
    try:
        temp_digits = digits
        temp_lower = lowercase_letters
        temp_upper = uppercase_letters
        temp_punc = punctuation
        count = int(input('Сколько паролей вы хотите сгенерировать?'))
        ambiguous_letters = input('Хотите ли вы исключить из паролей неоднозначные буквы, такие как: "l1o0O"? Да или Нет')
        if ambiguous_letters.lower() == 'да':
            temp_digits = digits[2:]
            temp_lower = lowercase_letters[2:]
            temp_upper = uppercase_letters[1:]

        lengh = int(input('Какой длины вы хотите пароль?'))
        temp_list = temp_digits + temp_lower + temp_upper + temp_punc
        for i in range(count):
            password = ''
            for j in range(lengh):
                password += choice(temp_list)
            print(password)
        return
    except:
        pass_gen()

pass_gen()

again = input('Чтобы сгенерировать новые пароли, напишите "еще".')
while again == 'еще':
    print()
    pass_gen()
print('Конец операции')

