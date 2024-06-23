
import pygame
import math
from pygame.locals import *
from player import Player
from enemy import Enemy1, Enemy2
from textWithBorder import draw_text_with_border
from buttonWithTextBox import ButtonWithTextBox
from coin import Coin


pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Furious Racer")

font = pygame.font.SysFont("mozugushi", 40)
font_small = pygame.font.SysFont("PixelGamingRegular-d9w0g.ttf",20)
coin_text_col = (255, 255, 0)
text_col = (255, 0, 255)
border_col = (0, 0, 0)
border_thickness = 2

main_menu_bg = pygame.image.load("opening_image.jpg").convert_alpha()
main_menu_bg = pygame.transform.scale(main_menu_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
playtime_bg = pygame.image.load("road.png")
playtime_bg = pygame.transform.scale(playtime_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

pause_btn = ButtonWithTextBox(350, 15, "Pause", None, 20, text_col, (0, 0, 0), (255, 255, 255), 10, 2, 70, 30)
mainMenu_button = ButtonWithTextBox(50, 15, "Main", None, 20, text_col, (0, 0, 0), (255, 255, 255), 10, 2, 70, 30)
start_button = ButtonWithTextBox(50, 480, "Start", "Hokjesgeest-PDGB.ttf", 20, text_col, (0, 0, 0), (255, 255, 255), 10, 2, hover_scale=1.1)
exit_button = ButtonWithTextBox(200, 480, "Exit", "MinecraftEvenings-lgvPd.ttf", 35, text_col, (0, 0, 0), (255, 255, 255), 10, 2, hover_scale=1.1)
resume_button = ButtonWithTextBox(200, 380, "Resume", None, 40, text_col, (0, 0, 0), (255, 255, 255), 10, 2, hover_scale=1.1)
play_again_button = ButtonWithTextBox(50, 380, "Play Again", None, 30, text_col, (0, 0, 0), (255, 255, 255), 10, 2, hover_scale=1.1)
main_menu_button = ButtonWithTextBox(200, 380, "Main Menu", None, 30, text_col, (0, 0, 0), (255, 255, 255), 10, 2, hover_scale=1.1)

player = Player()
enemy1 = Enemy1()
enemy2 = Enemy2()
enemies = pygame.sprite.Group(enemy1, enemy2)
bg_height = playtime_bg.get_height()
y_offset = 0
velocity = 3

coin = None
coin_counter = 0
game_state = 'main'
frame_counter = 0
run = True

def reset_game():
    global player, enemy1, enemy2, y_offset, coin, coin_counter
    player = Player()
    enemy1 = Enemy1()
    enemy2 = Enemy2()
    enemies.empty()
    enemies.add(enemy1)
    enemies.add(enemy2)
    y_offset = 0
    coin = Coin(font_small, coin_text_col, border_col,border_thickness)
    coin_counter = 0
    

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    if game_state == 'main':
        screen.blit(main_menu_bg, (0, 0))
        frame_counter += 1
        if frame_counter // 30 % 2 == 0:
            draw_text_with_border(screen, "Furious Racer", font, text_col, border_col, 70, 250, border_thickness)

        if start_button.draw(screen):
            reset_game()
            game_state = 'playtime'
        if exit_button.draw(screen):
            run = False

    elif game_state == 'playtime':
        screen.blit(playtime_bg, (0, y_offset - bg_height))
        screen.blit(playtime_bg, (0, y_offset))
        y_offset = (y_offset + velocity) % bg_height

        player.update()
        enemies.update()
        player.draw(screen)
        enemies.draw(screen)

        if coin:
            coin.update()
            coin.draw(screen)
            if pygame.sprite.collide_rect(player, coin):
                coin_counter += 1
                coin = Coin(font_small, coin_text_col, border_col, border_thickness)  # Generate a new coin

        if pause_btn.draw(screen):
            game_state = 'paused'
        if not player.is_shaking and pygame.sprite.spritecollide(player, enemies, False):
            player.lives -= 1
            if player.lives <= 0:
                game_state = 'wasted'
            else:
                player.reset_position()

        # Draw health counter
        draw_text_with_border(screen, f"Lives: {player.get_lives()}", font_small, text_col, border_col, 10, 10, border_thickness)
        # Draw coin counter
        draw_text_with_border(screen, f"Coins: {coin_counter}", font_small, text_col, border_col, 10, 40, border_thickness)

    elif game_state == 'paused':
        screen.blit(playtime_bg, (0, y_offset - bg_height))
        screen.blit(playtime_bg, (0, y_offset))
        player.draw(screen)
        enemies.draw(screen)

        if resume_button.draw(screen):
            game_state = 'playtime'
        if mainMenu_button.draw(screen):
            game_state = 'main'

    elif game_state == 'wasted':
        screen.blit(main_menu_bg, (0, 0))
        draw_text_with_border(screen, "Wasted", font, text_col, border_col, 100, 250, border_thickness)
        draw_text_with_border(screen, f"Your Score: {coin_counter}", font_small, text_col, border_col, 70, 350, border_thickness)
        if play_again_button.draw(screen):
            reset_game()
            game_state = 'playtime'
        if main_menu_button.draw(screen):
            game_state = 'main'

    pygame.display.update()

pygame.quit()
