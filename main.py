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
    window.fill((255, 255, 255))  # Biele pozadie

    # Zobrazenie hracej dosky
    window.blit(board_img, (0, 0))

    return x_img, o_img

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode(config.ROZLISENIE)
    pygame.display.set_caption("Piškvorky")

    # Nastavenie hry
    x_img, o_img = setup_game(window)

    while True:
        # Ak vypnem okno, musím vypnuť pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # Vypnutie pygamu
                sys.exit() # Vypnutie celého programu

        pygame.display.update()