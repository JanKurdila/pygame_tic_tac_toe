import pygame
from Config import config
import sys

def setup_game(window):
    # Načítanie obrázkov
    board_img = config.BOARD_IMAGE
    x_img = config.X_IMAGE
    o_img = config.O_IMAGE

    # Zmena veľkosti obrázkov X a O (voliteľné, ak chcete zmeniť ich veľkosť)
    x_img = pygame.transform.scale(x_img, (80, 80))
    o_img = pygame.transform.scale(o_img, (80, 80))
    board_img = pygame.transform.scale(board_img, config.ROZLISENIE)

    # Vyplnenie pozadia
    window.fill(config.POZADIE)  # Použitie konfiguračnej farby pozadia

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

def check_win(board):
    # Kontrola výhry v riadkoch
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]

    # Kontrola výhry v stĺpcoch
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # Kontrola výhry po diagonálach
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    # Ak nie je žiadny víťaz a nie je žiadne voľné miesto na doske, je to remíza
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                return None
    return "DRAW"

def highlight_winner(window, board, winner):
    # Pozícia víťaznej kombinácie
    if winner == 'X':
        winner_img = x_img
    else:
        winner_img = o_img

    # Kontrola výhry v riadkoch
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == winner:
            pygame.draw.line(window, config.FARBA_VITAZSTVA, (0, row * 100 + 50), (config.ROZLISENIE[0], row * 100 + 50), 5)

    # Kontrola výhry v stĺpcoch
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == winner:
            pygame.draw.line(window, config.FARBA_VITAZSTVA, (col * 100 + 50, 0), (col * 100 + 50, config.ROZLISENIE[1]), 5)

    # Kontrola výhry po diagonálach
    if board[0][0] == board[1][1] == board[2][2] == winner:
        pygame.draw.line(window, config.FARBA_VITAZSTVA, (50, 50), (config.ROZLISENIE[0] - 50, config.ROZLISENIE[1] - 50), 5)
    if board[0][2] == board[1][1] == board[2][0] == winner:
        pygame.draw.line(window, config.FARBA_VITAZSTVA, (config.ROZLISENIE[0] - 50, 50), (50, config.ROZLISENIE[1] - 50), 5)

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

    # Inicializácia premenných clicked_row a clicked_col mimo bloku udalosti
    clicked_row = None
    clicked_col = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                clicked_row = mouseY // 100
                clicked_col = mouseX // 100

                if board[clicked_row][clicked_col] is None:
                    board[clicked_row][clicked_col] = to_move
                    to_move = 'O' if to_move == 'X' else 'X'  # Opravená syntax chyba

        # Vyplnenie pozadia a zobrazenie hracej dosky
        window.fill(config.POZADIE)
        window.blit(board_img, (0, 0))

        # Vykreslenie X a O
        draw_figures(window, board, x_img, o_img)

        # Kontrola výhry
        result = check_win(board)
        if result is not None:
            # Ak je výhra, zvýrazníme výhernej kombináciu
            highlight_winner(window, board, result)

        # Aktualizácia obrazovky
        pygame.display.update()

        # Obmedzenie snímkovej frekvencie
        clock.tick(config.FPS)
