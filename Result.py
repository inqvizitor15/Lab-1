print(' ------------Флаг------------')
print()
RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLUE = '\u001b[44m'
BLACK = '\u001b[40m'
END = '\u001b[0m'
#
for i in range(6):
    if i < 2:
        print(f'{RED}{"  " * 15}{END}')
    elif 2 <= i < 4:
        print(f'{WHITE}{"  " * 15}{END}')
    else:
        print(f'{BLUE}{"  " * 15}{END}')

print()
print()
print()
print('\t\t-------------Узор--------------')
print()

print(f'{BLUE}{"  " * 1}{WHITE}{"  " * 10}{BLUE}{"  " * 1}{WHITE}{"  " * 10}{BLUE}{"  " * 1}{END}')
print(f'{WHITE}{"  " * 1}{BLUE}{"  " * 1}{WHITE}{"  " * 8}{BLUE}{"  " * 1}{WHITE}{"  " * 1}{BLUE}{"  " * 1}{WHITE}{"  " * 8}{BLUE}{"  " * 1}{WHITE}{"  " * 1}{END}')
print(f'{WHITE}{"  " * 2}{BLUE}{"  " * 1}{WHITE}{"  " * 6}{BLUE}{"  " * 1}{WHITE}{"  " * 3}{BLUE}{"  " * 1}{WHITE}{"  " * 6}{BLUE}{"  " * 1}{WHITE}{"  " * 2}{END}')
print(f'{WHITE}{"  " * 3}{BLUE}{"  " * 1}{WHITE}{"  " * 4}{BLUE}{"  " * 1}{WHITE}{"  " * 5}{BLUE}{"  " * 1}{WHITE}{"  " * 4}{BLUE}{"  " * 1}{WHITE}{"  " * 3}{END}')
print(f'{WHITE}{"  " * 4}{BLUE}{"  " * 1}{WHITE}{"  " * 2}{BLUE}{"  " * 1}{WHITE}{"  " * 7}{BLUE}{"  " * 1}{WHITE}{"  " * 2}{BLUE}{"  " * 1}{WHITE}{"  " * 4}{END}')
print(f'{WHITE}{"  " * 5}{BLUE}{"  " * 1}{BLUE}{"  " * 1}{WHITE}{"  " * 9}{BLUE}{"  " * 1}{BLUE}{"  " * 1}{WHITE}{"  " * 5}{END}')

print(f'{WHITE}{"  " * 5}{BLUE}{"  " * 1}{BLUE}{"  " * 1}{WHITE}{"  " * 9}{BLUE}{"  " * 1}{BLUE}{"  " * 1}{WHITE}{"  " * 5}{END}')
print(f'{WHITE}{"  " * 4}{BLUE}{"  " * 1}{WHITE}{"  " * 2}{BLUE}{"  " * 1}{WHITE}{"  " * 7}{BLUE}{"  " * 1}{WHITE}{"  " * 2}{BLUE}{"  " * 1}{WHITE}{"  " * 4}{END}')
print(f'{WHITE}{"  " * 3}{BLUE}{"  " * 1}{WHITE}{"  " * 4}{BLUE}{"  " * 1}{WHITE}{"  " * 5}{BLUE}{"  " * 1}{WHITE}{"  " * 4}{BLUE}{"  " * 1}{WHITE}{"  " * 3}{END}')
print(f'{WHITE}{"  " * 2}{BLUE}{"  " * 1}{WHITE}{"  " * 6}{BLUE}{"  " * 1}{WHITE}{"  " * 3}{BLUE}{"  " * 1}{WHITE}{"  " * 6}{BLUE}{"  " * 1}{WHITE}{"  " * 2}{END}')
print(f'{WHITE}{"  " * 1}{BLUE}{"  " * 1}{WHITE}{"  " * 8}{BLUE}{"  " * 1}{WHITE}{"  " * 1}{BLUE}{"  " * 1}{WHITE}{"  " * 8}{BLUE}{"  " * 1}{WHITE}{"  " * 1}{END}')
print(f'{BLUE}{"  " * 1}{WHITE}{"  " * 10}{BLUE}{"  " * 1}{WHITE}{"  " * 10}{BLUE}{"  " * 1}{END}')

print()
print()
print()
print('\t-------------Функция--------------')
print()
plot_list = [[0 for i in range(10)] for i in range(10)]
result_list = [2 * i for i in range(10)]

step = abs(result_list[0] - result_list[9]) / 9
for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][0] = step * (8 - i) + step
for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result_list[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list [i][k + 1] = 1

for i in range(9):

    for j in range(10):

        if j == 0:
            if plot_list[i][j] >= 10:
                print(str(plot_list[i][j]) + '\t', end = '')
            else:
                print(str(plot_list[i][j]) + '\t' + '\t', end = '')

        if plot_list[i][j] == 0:
            print(f'{BLACK}{"  " * 2}{END}', end = '')
        if plot_list[i][j] == 1:
            print(f'{WHITE}{"  " * 2}{END}', end = '')

    print()


print()
print()
print()

print('\t-------------Обработка файла--------------')
print()

file = open('sequence.txt', 'r')
plist = []
for number in file:
    plist.append(float(number))
file.close()

sum0 = sum([abs(plist[i]) for i in range(len(plist))])
sum1 = sum([abs(plist[i]) for i in range(len(plist)) if i % 2 == 0])
sum2 = sum([abs(plist[i]) for i in range(len(plist)) if i % 2 != 0])

prcnt1 = sum1 / sum0 * 100
prcnt2 = sum2 / sum0 * 100

print(f'{RED}{"  " * int(51 / 2)}{END} {round(prcnt1, 2)}')
print(f'{BLUE}{"  " * int(49 / 2)}{END} {round(prcnt2, 2)}')


