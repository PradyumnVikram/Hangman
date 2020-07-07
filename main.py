__author__ = 'Pradyumn Vikram'
#image data taken from tech with tim
#https://drive.google.com/drive/folders/1VXFa0yNynZNFN-m6VoOM-Ri5gkSi89ym

import pygame
import os
from words import word_list
import re
import random
import time

pygame.init()

def convert_char(s): 
  
    new = "" 
  
    for x in s: 
        new += x + ' '  
  
    return new 
def convert(s): 
  
    new = "" 
    
    for x in s: 
        new += x
  
    return new 

def get_word(word_list):
    word = random.choice(word_list)
    return word
WHITE = (255,255,255)

WIDTH = 15
HEIGHT = 15
 
# This sets the margin between each cell
MARGIN = 10
font = pygame.font.SysFont('comicsans', 50)
alpha_font = pygame.font.SysFont('comicsans', 25)
points_font = pygame.font.SysFont('comicsans', 35)
win_size = (500, 420)
win = pygame.display.set_mode(win_size)
root = os.path.dirname(__file__)


imgs = {}
def won(chars):
    if '_' in chars:
        return False
    return True

for file in os.listdir(os.path.join(root, 'data/')):
    imgs[file[:-4]
         ] = pygame.image.load((os.path.join(root, 'data', file)))

def refresh_window(win, img_id, imgs, word, letters, points):
    win.fill((220, 220, 220))
    img = imgs['hangman'+str(img_id)]
    win.blit(img, (0,50))
    ind = 0
    for row in range(2):
        for column in range(13):
            color = WHITE
            pygame.draw.circle(win,
                             color,
                             [(MARGIN + WIDTH + 7) * column + (MARGIN) + 50,
                              (MARGIN + HEIGHT + 7) * row + MARGIN + 310], 15)
            alph = alpha_font.render(letters[ind], 1, (0,0,0))
            win.blit(alph, ([((MARGIN + WIDTH + 7) * column + (MARGIN) + 50) - 7,
                              ((MARGIN + HEIGHT + 7) * row + MARGIN + 310) - 7]))
            
            ind += 1
    text = font.render(word, 1, (0,0,0))
    points = points_font.render('Score:' + str(points), 1, (0,0,0))
    win.blit(text, ((win_size[0]/2 - text.get_width()/2) + 50,200))
    win.blit(points, (0,0))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.upper().split(' ')
    alphabets = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.upper().split(' ')
    run = True
    img_id = 0
    chosen = False
    grid = [[None for i in range(13)] for j in range(2)]

    points = 0
    while run:
        
        clock.tick(60)
        for event in pygame.event.get():
            if not chosen:
                word = get_word(word_list)
                
                chars = '_ '*(len(word))
                answer = word
                chosen = True
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                column = (pos[0] - 50) // (WIDTH + MARGIN+7)
                row = (pos[1] - 310) // (HEIGHT + MARGIN+7)
                ind = column 
                if row == 1:
                    ind += 13
                clicked = letters[ind]
                letters[ind] = ' '
                if clicked.lower() in word.lower():
                    chars = chars.split(' ')
                    word = word.lower()
                    clicked = clicked.lower()
                    word = [ch for ch in word]
                    while clicked.lower() in word:
                        chars[word.index(clicked.lower())] = clicked.upper()
                        word[word.index(clicked.lower())] = '.'
                            
                    chars = convert_char(chars)
                    word = convert(word)
                else:
                    img_id += 1
        if won(chars):
            letters = alphabets
            points += 1
            chosen = False
            
        elif img_id == 6:
            letters = alphabets
            img_id = 0
            
            print(answer)
            chosen = False
        
        
        refresh_window(win, img_id, imgs, chars, letters, points)
main()
#line

