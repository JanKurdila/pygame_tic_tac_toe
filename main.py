import pygame
from Config import config
import sys

def setup_game(window):
    # Načítanie obrázkov
    board_img = pygame.image.load("Obrázky/Board.png")
    x_img = pygame.image.load("Obrázky/X.png")
    o_img = pygame.image.load("Obrázky/O.png")

    # Zmena veľkosti obrázkov X a O (voliteľné, ak chcete zmeniť ich veľkosť)
    x_img = pygame.transform.scale(x_img, (80, 80))
    o_img = pygame.transform.scale(o_img, (80, 80))
    board_img = pygame.transform.scale(board_img, config.ROZLISENIE)

    # Vyplnenie pozadia
    window.fill(config.POZADIE)  # Biele pozadie

    # Zobrazenie hracej dosky
    window.blit(board_img, (0, 0))

    return x_img, o_img, board_img

def draw_figures(window, board, x_img, o_img):
    "Interakcia s používateľom - detekcia na kliknutie myšou a umiestňovanie znakov na dosku"
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                window.blit(x_img, (col * 100 + 10, row * 100 + 10))
            elif board[row][col] == 'O':
                window.blit(o_img, (col * 100 + 10, row * 100 + 10))

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode(config.ROZLISENIE)
    pygame.display.set_caption("Piškvorky")

    # Nastavenie hry
    x_img, o_img, board_img = setup_game(window)

    # Inicializácia hracej dosky
    board = [[None]*3 for _ in range(3)]
    to_move = 'X'

    # Inicializácia Clock
    clock = pygame.time.Clock()

    while True:
        # Ak vypnem okno, musím vypnuť pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # Vypnutie pygamu
                sys.exit() # Vypnutie celého programu

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                clicked_row = mouseY // 100
                clicked_col = mouseX // 100

                if board[clicked_row][clicked_col] is None:
                    board[clicked_row][clicked_col] = to_move
                    to_move = 'O' if to_move == 'X' else 'X'

        # Vyplnenie pozadia a zobrazenie hracej dosky
        window.fill(config.POZADIE)
        window.blit(board_img, (0, 0))

        # Vykreslenie X a O
        draw_figures(window, board, x_img, o_img)

        # Aktualizácia obrazovky
        pygame.display.update()

        # Obmedzenie snímkovej frekvencie
        clock.tick(config.FPS)
