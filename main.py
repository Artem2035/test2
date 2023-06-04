import pygame
from button import Button
import generate_field
import make_field


def start_game(field_size: int, difficulty: str):
    new_game = ""
    back_color = (255, 255, 255)
    size_field = field_size
    size = (size_field * 40, size_field * 40 + 50)

    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Light'em up!")

    FPS = 30
    clock = pygame.time.Clock()

    generated_field = []
    for i in range(size_field):
        generated_field.append([])
        for j in range(size_field):
            generated_field[i].append(-1)
    generated_field[0][0] = 0

    if difficulty == "Easy":
        generate_field.easy_generate(generated_field, size_field)
    elif difficulty == "Middle":
        generate_field.middle_generate(generated_field, size_field)
    elif difficulty == "Hard":
        generate_field.generate_field_hard(generated_field, size_field)

    field = []
    for i in range(size_field):
        field.append([])
        for j in range(size_field):
            field[i].append(-1)

    path = []

    if difficulty == "Easy":
        make_field.make_field(field, generated_field, size_field, path, "easy")
    elif difficulty == "Middle":
        make_field.make_field(field, generated_field, size_field, path, "middle")
    elif difficulty == "Hard":
        make_field.make_field(field, generated_field, size_field, path, "hard")
    # input box
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(5, size_field * 40 + 5, 40, 32)
    color_inactive = pygame.Color('black')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    size_text = ''
    # buttons
    difficulty_button = Button(50, size_field * 40 + 5, 80, 32, 'Easy')
    start_button = Button(135, size_field * 40 + 5, 80, 32, 'Start')
    #game timer
    timer_font = pygame.font.Font(None, 20)
    game_time = 60
    text_game_time = pygame.Surface((50,20))
    rect_game_time = pygame.Rect(size_field*40//2-10, size_field * 40+37, 25, 20)
    text_game_time = timer_font.render(str(game_time), True, pygame.Color('black'))
    pygame.time.set_timer(pygame.USEREVENT,1000)
    #game messages
    mesg_win = pygame.image.load(f'assets/mis-pass.bmp')
    mesg_win_rect = mesg_win.get_rect()
    mesg_fail = pygame.image.load(f'assets/mis-fail.bmp')
    mesg_fail_rect = mesg_fail.get_rect()
    # game
    #game_status - False игра не выиграна, True игра выйграна
    game_status = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
                # buttons clicks
                if difficulty_button.buttonRect.collidepoint(event.pos):
                    if difficulty_button.text == "Easy":
                        difficulty_button.text = "Middle"
                    elif difficulty_button.text == "Middle":
                        difficulty_button.text = "Hard"
                    elif difficulty_button.text == "Hard":
                        difficulty_button.text = "Easy"
                if start_button.buttonRect.collidepoint(event.pos):
                    if size_text != "":
                        num = int(size_text)
                        if 5 < num < 17 and num % 2 == 0:
                            running = False
                            new_game = difficulty_button.text
                # game event
                if event.button == 1:
                    if not(game_status):
                        if game_time != 0:
                            y = int(event.pos[0] // 40)
                            x = int(event.pos[1] // 40)
                            if x > size_field - 1 or y > size_field - 1:
                                break
                            cell = field[x][y]
                            cell.rotate()
                            field[x][y] = cell
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        size_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        size_text = size_text[:-1]
                    else:
                        if len(size_text) + 1 <= 2 and str.isdigit(event.unicode):
                            if size_text == "" and (0 < int(event.unicode) <= 9):
                                size_text += event.unicode
                            elif 5 < int(size_text + event.unicode) < 17:
                                size_text += event.unicode
            if event.type == pygame.USEREVENT and not(game_status):
                if game_time != 0:
                    game_time -= 1
                    text_game_time = timer_font.render(str(game_time), True, pygame.Color('black'))

        screen.fill(back_color)

        for i in range(len(path)):
            y = path[i][0]
            x = path[i][1]
            element = field[y][x]
            if element.angle == element.right_angle:
                element.surf = element.surf_light
            else:
                element.surf = element.surf_no_light
                for j in range(i + 1, len(path)):
                    y = path[j][0]
                    x = path[j][1]
                    element = field[y][x]
                    element.surf = element.surf_no_light
                break

        #количество заженных клеток
        kol = 0
        for i in range(len(path)):
            y = path[i][0]
            x = path[i][1]
            element = field[y][x]
            if element.angle == element.right_angle:
                kol += 1
            else:
                break

        for row in field:
            for cell in row:
                screen.blit(cell.surf, cell.get_coordinates(), cell.rect)

        # Render the current text.
        txt_surface = font.render(size_text, True, color)
        # Blit the text and Blit the input_box rect
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        # render buttons
        difficulty_button.buttonSurface.fill(pygame.Color('white'))
        difficulty_button.buttonSurf = font.render(difficulty_button.text, True, (20, 20, 20))
        difficulty_button.buttonSurface.blit(difficulty_button.buttonSurf, [
            difficulty_button.buttonRect.width / 2 - difficulty_button.buttonSurf.get_rect().width / 2,
            difficulty_button.buttonRect.height / 2 - difficulty_button.buttonSurf.get_rect().height / 2
        ])
        screen.blit(difficulty_button.buttonSurface, difficulty_button.buttonRect)
        pygame.draw.rect(screen, pygame.Color("black"), difficulty_button.buttonRect, 2)
        start_button.buttonSurf = font.render(start_button.text, True, (20, 20, 20))
        start_button.buttonSurface.blit(start_button.buttonSurf, [
            start_button.buttonRect.width / 2 - start_button.buttonSurf.get_rect().width / 2,
            start_button.buttonRect.height / 2 - start_button.buttonSurf.get_rect().height / 2
        ])
        screen.blit(start_button.buttonSurface, start_button.buttonRect)
        pygame.draw.rect(screen, pygame.Color("black"), start_button.buttonRect, 2)
        #timer render
        screen.blit(text_game_time, rect_game_time)
        #game status check
        if kol == size_field ** 2:
            game_status = True
            screen.blit(mesg_win,(size_field*20-90,size_field*20), mesg_win_rect)
        if game_time == 0 and not(game_status):
            for i in range(len(path)):
                y = path[i][0]
                x = path[i][1]
                element = field[y][x]
                #if element.angle != element.right_angle:
                element.surf = pygame.transform.rotate(element.surf_light, element.angle - element.right_angle)
                screen.blit(element.surf, element.get_coordinates(), element.rect)
            screen.blit(mesg_fail, (size_field * 20 - 90, size_field * 20), mesg_fail_rect)

        #screen update
        pygame.display.update()
        clock.tick(FPS)
    if new_game != "":
        return int(size_text), new_game
    else:
        return False


game = [6, "Easy"]
game_run = True
while game_run:
    game = start_game(game[0], game[1])
    if not (game):
        game_run = False
pygame.quit()
