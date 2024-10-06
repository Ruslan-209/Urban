
area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
def winner():
    if area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X':
        return 'X'
    if area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X':
        return 'X'
    if area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][0] == 'X' and area[2][0] == 'X':
        return 'X'
    if area[0][1] == 'X' and area[1][1] == 'X' and area[2][1] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][2] == 'X' and area[2][1] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][1] == 'X' and area[2][0] == 'X':
        return 'X'
    if area[0][0] == '0' and area[0][1] == '0' and area[0][2] == '0':
        return '0'
    if area[1][0] == '0' and area[1][1] == '0' and area[1][2] == '0':
        return '0'
    if area[2][0] == '0' and area[2][1] == '0' and area[2][2] == '0':
        return '0'
    if area[0][0] == '0' and area[1][0] == '0' and area[2][0] == '0':
        return '0'
    if area[0][1] == '0' and area[1][1] == '0' and area[2][1] == '0':
        return '0'
    if area[0][2] == '0' and area[1][2] == '0' and area[2][1] == '0':
        return '0'
    if area[0][0] == '0' and area[1][1] == '0' and area[2][2] == '0':
        return '0'
    if area[0][2] == '0' and area[1][1] == '0' and area[2][0] == '0':
        return '0'
    return '*'

def new_area():
    for i in area:
        print(*i)

new_area()
for tern in range(1, 10):
    print(f'Ход {tern}')
    if tern % 2 == 0:
        tern2 = '0'
        print('Ходят нолики')
    else:
        tern2 = 'X'
        print('ходят крестики')
    crow = int(input('веедите число (1, 2, 3): ')) - 1
    horse = int(input('введите число (1, 2, 3): ')) - 1
    if area[crow] [horse] == '*':
            area[crow] [horse] = tern2
    else:
        print('пропускаете ход')
        new_area()
        continue

    new_area()

    if winner() == 'X':
        print('победили крестики')
        break
    if winner() == '0':
        print('победили нолики')
    if winner() == '*' and tern == 9:
        print('Ничья')



