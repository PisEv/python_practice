import pygame
import sys


def check_win(mas, sign):
    num = 0
    for row in mas:
        num += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if num == 0:
        return 'Ничья'
    return False


pygame.init()
size_block = 100
playing_field = 15
width = heigth = size_block * 3 + playing_field * 4
size_window = (width, heigth)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Крестики-нолики)")
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
count = 0
game_over = False
mas = [[0] * 3 for i in range(3)]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + playing_field)
            row = y_mouse // (size_block + playing_field)
            if mas[row][col] == 0:
                if count % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                count += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            count = 0
            screen.fill(black)
    game_over = check_win(mas, 'x')

    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = (144,0,32)
                elif mas[row][col] == 'o':
                    color = (71,167,106)
                else:
                    color = ( 255,250,250)
                x = col * size_block + (col + 1) * playing_field
                y = row * size_block + (row + 1) * playing_field
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == (144,0,32):
                    pygame.draw.line(screen, white, (x + 3, y + 3), (x + size_block - 3, y + size_block - 3), 3)
                    pygame.draw.line(screen, white, (x + size_block - 3, y + 3), (x + 3, y + size_block - 3), 3)
                elif color == (71,167,106):
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3,
                                       3)
    if (count - 1) % 2 == 0:
        game_over = check_win(mas, 'x')
    else:
        game_over = check_win(mas, 'o')

    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont('arial', 50)
        if game_over == 'x':
            game_over = 'Победитель - Х'
        elif game_over == 'o':
            game_over = 'Победитель - O'
        txt1 = font.render(game_over, True, white)
        text_rect = txt1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(txt1, (text_x, text_y))
    pygame.display.update()