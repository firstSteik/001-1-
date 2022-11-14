print('вы зашли в калькулятор')

while True:

   action = input('выберите действие которое хотите сделать: \n'

                  'Сложение"+"\n'

                  'Вычитание"-"\n'

                  'Умножение"*"\n'

                  'Возведение в степень"**"\n')

   x = float(input('введите первое слагаемое:\n'))

   y = float(input('введите второе слагаемое:\n'))

   if action == '+':

       print(x + y)

   elif action == '-':

       print(x - y)

   elif action == '*':

       print(x * y)

   elif action == '**':

       print(x % y)

   o = input('вы хотите продолжить?')

   if o == 'да':

       print('Начнем сначала')

   if o == 'нет':

       print('у тебя нет выбора')

   else:

       print('Ответ неверный!')
