from wire import Wire


def make_field(field,generated_field, size:int, direction, type: str):
    m = size**2
    x = 0
    y = 0
    end_x = 0
    end_y = 0
    for i in generated_field:
        if 0 in i:
            y = generated_field.index(i)
            x = i.index(0)
        if m - 1 in i:
            end_y = generated_field.index(i)
            end_x = i.index(m - 1)
    direction.append([y,x])

    if type == "hard":
        field[y][x]= Wire(x*40,y*40,-90,"line")
        if (size//2)%2 == 0:
            field[end_y][end_x]= Wire(end_x*40,end_y*40,-90,"line")
        else:
            field[end_y][end_x] = Wire(end_x * 40, end_y * 40, 0, "line")
    elif type == "easy":
        field[y][x] = Wire(x * 40, y * 40, 0, "line")
        field[end_y][end_x] = Wire(end_x * 40, end_y * 40, 0, "line")
    elif type == "middle":
        field[y][x] = Wire(x * 40, y * 40, -90, "line")
        field[end_y][end_x] = Wire(end_x * 40, end_y * 40, -90, "line")
    for element in range(1,m):
        if y + 1 < size:
            if generated_field[y][x]+1==generated_field[y+1][x]:
                direction.append([y+1,x])
                y += 1
        if y -1 >= 0:
            if generated_field[y][x]+1==generated_field[y-1][x]:
                direction.append([y-1,x])
                y -= 1
        if x + 1 < size:
            if generated_field[y][x]+1==generated_field[y][x+1]:
                direction.append([y,x+1])
                x += 1
        if x -1 >= 0:
            if generated_field[y][x]+1==generated_field[y][x-1]:
                direction.append([y,x-1])
                x -= 1

    for i in range(1,m-1):
        block = direction[i-1:i+2]
        angle = -1
        format = ""
        if block[0][0]==block[1][0]==block[2][0]:
            angle = 0
            format = "line"
        if block[0][1]==block[1][1]==block[2][1]:
            angle = -90
            format = "line"
        #повороты 90,180,270,360
        if block[0][0]+1==block[1][0]:
            if block[1][1] + 1==block[2][1]:
                angle = 90
                format = "angle"
        elif block[0][1]-1==block[1][1]:
            if block[1][0] - 1==block[2][0]:
                angle = 90
                format = "angle"

        if block[0][0]-1==block[1][0]:
            if block[1][1] + 1==block[2][1]:
                angle = 180
                format = "angle"
        elif block[0][1]-1==block[1][1]:
            if block[1][0] + 1==block[2][0]:
                angle = 180
                format = "angle"

        if block[0][0]-1==block[1][0]:
            if block[1][1] - 1==block[2][1]:
                angle = 270
                format = "angle"
        elif block[0][1]+1==block[1][1]:
            if block[1][0] + 1==block[2][0]:
                angle = 270
                format = "angle"

        if block[0][0]+1==block[1][0]:
            if block[1][1] - 1==block[2][1]:
                angle = 360
                format = "angle"
        elif block[0][1]+1==block[1][1]:
            if block[1][0] - 1==block[2][0]:
                angle = 360
                format = "angle"
        if angle != -1 and format != "":
            field[block[1][0]][block[1][1]] = Wire(block[1][1]*40,block[1][0]*40,angle,format)

    path = direction.copy()