from comparison import *
from clescles import *
import pygame
import random
import tkinter as tk

pygame.init()

KAART_BREEDTE = 100
KAART_LENGTE = 150 
KAART_AFSTAND = 20  # Afstanden tussen kaarten (om ze netjes te positioneren)
score_player = 0
BORD_START_POSITIE = (50, 50)  # Startpositie van het spelbord (linkerbovenhoek van het eerste kaartvak)
kaarten_op_bord = []  # Variabele voor kaarten die op het bord liggen (lege lijst, wordt later gevuld)
geselecteerde_kaarten = []  # Variabele om geselecteerde kaarten bij te houden (voor een mogelijke set)
MAX_KAARTEN_OP_BORD = 12  # Maximaal aantal kaarten op het bord
twelvecards = []
card_images = []
selected_cards = []
button = {}
cards = []  # Lijst voor kaarten met hun Rects en afbeeldingen

current_time = pygame.time.get_ticks()

lastset = []

lijst = [*range(81)]
random.shuffle(lijst)

WINDOW_SIZE = [1250, 700]  # Afmeting van spelscherm instellen (in pixels: [breedte,hoogte])

# -------- FUNCTIE DEFINITIES --------

# Fonts
font = pygame.font.Font(None, 50)
timer_font = pygame.font.Font(None, 40)  # Font voor de timer

# Timer variabelen
start_time = pygame.time.get_ticks()
timer_duration = 30000  # 30 seconden in milliseconden
timer_running = True

def makethedeck(): 
    for q in range(0, 12):
        twelvecards.append(lijst.pop())

def replace3():
    for i in range(3):
        twelvecards.pop(0)
        twelvecards.append(lijst.pop())

def replace_found_set(set):  # from high to low
    if len(lijst) > 0:
        set.sort()
        twelvecards[set[2]] = lijst.pop()
        twelvecards[set[1]] = lijst.pop()
        twelvecards[set[0]] = lijst.pop()
        makedeck()

def makedeck():  # 12 kaarten op het scherm bouwen
    screen.fill("pink")
    selected_cards.clear()
    cards.clear()
    global score_player
    if score_player == 0:
        score_text = font.render(f'YOUR SCORE: 0', True, "black")
        screen.blit(score_text, (20, 20))
    card_images.clear()

    for i in twelvecards:
        image = pygame.image.load(card(i).imagename())
        image = pygame.transform.scale(image, (KAART_BREEDTE, KAART_LENGTE)) 
        card_images.append(image)
   
    start_x = (1250 - (4 * KAART_BREEDTE + 3 * KAART_AFSTAND)) // 2  # Centreer raster horizontaal
    start_y = (700 - (3 * KAART_LENGTE + 2 * KAART_AFSTAND)) // 2  # Centreer raster verticaal
   
    for row in range(3):  # 3 rijen
        for col in range(4):  # 4 kolommen
            x = start_x + col * (KAART_BREEDTE + KAART_AFSTAND)
            y = start_y + row * (KAART_LENGTE + KAART_AFSTAND)
            rect = pygame.Rect(x , y  , KAART_BREEDTE , KAART_LENGTE )
            cards.append({"rect": rect, "image": card_images[row * 4 + col], "selected": False, "kaart": card(twelvecards[row * 4 + col]), "index" : row * 4 + col})
    checksets()

def checksets():
    print(listofsets(cards))
    if (len(listofsets(cards))) == 0:
        replace_found_set(lastset)

def kaartenklikken():
    mouse_pos = event.pos
    for card in cards:
        if card["rect"].collidepoint(mouse_pos):
            if card["selected"]:
                card["selected"] = False
                border_rect = card["rect"].inflate(20, 20) 
                pygame.draw.rect(screen, "pink", border_rect, 20)  
                selected_cards.remove(card)
            elif len(selected_cards) < 3:
                card["selected"] = True
                selected_cards.append(card)
    for card in cards:
        if card["selected"]:
            border_rect = card["rect"].inflate(20, 20) 
            pygame.draw.rect(screen, "lightgreen", border_rect, 20)

button_layout_rect = pygame.Rect(575, 20, 100, 50)

def makebutton():
    pygame.draw.rect(screen, "lightgreen", button_layout_rect)  
    font = pygame.font.Font(None, 50)
    text = font.render('SET!', True, "black")  # Tekst op de knop
    screen.blit(text, (button_layout_rect.x + 10, button_layout_rect.y + 10))  # Plaats de tekst

def checkbutton():
    global score_player
    mouse_pos = event.pos 
    if button_layout_rect.collidepoint(mouse_pos) and len(selected_cards) == 3:
        if checkforset(selected_cards[0]["kaart"], selected_cards[1]["kaart"], selected_cards[2]["kaart"]):
            lastset.clear()
            lastset.append(selected_cards[0]["index"])
            lastset.append(selected_cards[1]["index"])
            lastset.append(selected_cards[2]["index"])
            score_player +=  1
            replace_found_set(lastset)
            score_text = font.render(f'YOUR SCORE: {score_player}', True, "black")
            screen.blit(score_text, (20, 20))
        else: 
            score_text = font.render(f'WRONG SET', True, "red")
            screen.blit(score_text, (100, 100))

def draw_timer():
    if timer_running:
        elapsed_time = pygame.time.get_ticks() - start_time  # Bereken de verstreken tijd
        remaining_time = max(0, timer_duration - elapsed_time)  # Zorg ervoor dat de tijd niet negatief wordt
        seconds_left = remaining_time // 1000  # Omrekenen naar seconden
        timer_text = timer_font.render(f'Time: {seconds_left}s', True, "black")
        screen.blit(timer_text, (WINDOW_SIZE[0] - 120, 20))  # Plaats de timer rechtsbovenin

        if remaining_time == 0:
            global spel_is_afgelopen
            spel_is_afgelopen = True  # Stop het spel als de timer afloopt

# -------- PYGAME INITIALISATIE --------
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)  # Spelscherm maken (en opslaan in een variabele screen)
screen.fill("pink")
pygame.display.set_caption("Vind de SET")  # Titel van spelscherm instellen
clock = pygame.time.Clock()  # Zorgt voor verversingssnelheid van het scherm

# -------- HOOFDLOOP VAN HET PROGRAMMA --------
makethedeck()
makedeck()

spel_is_afgelopen = False
while not spel_is_afgelopen:
    # --- Check gebeurtenissen (zoals muiskliks enz.) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Het kruisje is aangeklikt
            spel_is_afgelopen = True  # Het spel moet eindigen
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Linkermuisknop
            kaartenklikken()
            checkbutton()

    # --- Teken de graphics ---
    for i in cards:
        screen.blit(i["image"], i["rect"].topleft)
    makebutton()
    draw_timer()  # Teken de timer op het scherm

    # --- Ververs het beeldscherm met de nieuwe graphics ---
    clock.tick(30)  # Ververs scherm met 30 frames per seconde
    pygame.display.flip()  # Ververs het beeldscherm met de bijgewerkte versie

# -------- AFSLUITING --------
pygame.quit()  # Sluit het scherm af
