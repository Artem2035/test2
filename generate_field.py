import random


def make_block(a, i, j, end_x, end_y):
    if i == end_x and j == end_y:
        kol = 0
        for i in a:
            if i.count(-1) != 0:
                kol += 1
        if kol == 0:
            return 0
        else:

            return -1
    x = y = 0
    flag = False
    while not (flag):
        if (0 <= i + x <= 1) and (0 <= j + y <= 1) and a[x + i][j + y] == -1:
            flag = True
            a[x + i][j + y] = a[i][j] + 1
            if make_block(a, x + i, j + y, end_x, end_y) == -1:
                flag = False
                a[x + i][j + y] = -1
                x = random.randint(-1, 1)
                if x != 0:
                    y = 0
                else:
                    y = random.randint(-1, 1)
        else:
            x = random.randint(-1, 1)
            if x != 0:
                y = 0
            else:
                y = random.randint(-1, 1)


def generate_field_hard(field, size):
    for line in range(size // 2):
        start_ind = 1
        end_ind = 2
        if line % 2 == 0:
            for block in range(0, size, 2):
                b = [i[block:block + 2] for i in field[line * 2:(line + 1) * 2]]
                if not (block == size - 2):
                    make_block(b, 0, 0, 0, 1)
                else:
                    make_block(b, 0, 0, 1, 0)
                for i in range(0, 2):
                    for j in range(0, 2):
                        field[line * 2 + i][j + start_ind - 1] = b[i][j]

                if end_ind < size:
                    field[line * 2][end_ind] = field[line * 2][end_ind - 1] + 1
                else:
                    if (line + 1) * 2 < size:
                        field[(line + 1) * 2][1] = field[(line + 1) * 2 - 1][size - 2] + 1

                start_ind += 2
                end_ind += 2
        else:
            for block in range(0, size, 2):
                b = [i[block:block + 2] for i in field[line * 2:(line + 1) * 2]]
                if block == 0:
                    make_block(b, 0, 1, 1, 1)
                elif not (block == size - 2):
                    make_block(b, 1, 0, 1, 1)
                else:
                    make_block(b, 1, 0, 1, 1)
                for i in range(0, 2):
                    for j in range(0, 2):
                        field[line * 2 + i][j + start_ind - 1] = b[i][j]

                if end_ind < size:
                    field[line * 2 + 1][end_ind] = field[line * 2 + 1][end_ind - 1] + 1
                else:
                    if (line + 1) * 2 < size:
                        field[(line + 1) * 2][0] = field[(line + 1) * 2 - 1][size - 1] + 1
                start_ind += 2
                end_ind += 2
            for i in field[line * 2:(line + 1) * 2]:
                i.reverse()

    gen = random.randint(1,4)
    if gen == 1:
        for row in field:
            row.reverse()
    elif gen == 2:
        field.reverse()
    elif gen ==3:
        field.reverse()
        for row in field:
            row.reverse()


def easy_generate(field, size):
    for i in range(size):
        if i % 2 == 0:
            for j in range(1,size):
                field[i][j]= field[i][j - 1] + 1
            if i+1<size:
                field[i + 1][size - 1] = field[i][size - 1] + 1
        else:
            for j in range(size-2,-1,-1):
                field[i][j]= field[i][j + 1] + 1
            if i+1<size:
                field[i + 1][0] = field[i][0] + 1

def middle_generate(field, size):
    for i in range(size):
        if i % 2 == 0:
            for j in range(1,size):
                field[j][i]=field[j-1][i]+1
            if i+1<size:
                field[size-1][i+1] = field[size-1][i] + 1
        else:
            for j in range(size-2,-1,-1):
                field[j][i]=field[j+1][i]+1
            if i + 1 < size:
                field[0][i + 1] = field[0][i] + 1