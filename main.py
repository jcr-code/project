import time
import pygame
from admin import *
from pygame import Rect
vec = pygame.math.Vector2

# STACK
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackList:
    def __init__(self):
        self.top = None

    def printStack(self):
        temp = self.top
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def is_empty(self):
        if (self.top is None):
            return True
        return False

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if (self.is_empty()):
            return False
        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        if not self.is_empty():
            return self.top.data

stk = StackList()

# Initialize the pygame
pygame.init()

#Create the screen
screen_width = 1920 #x
screen_height = 1080 #y
screen = pygame.display.set_mode((screen_width, screen_height))

#Title and Icon Title
pygame.display.set_caption("WHAT WOULD YOU DO?")
icon = pygame.image.load('question.png')
pygame.display.set_icon(icon)

#Background
class Background:
    def __init__(self, dataBackground):
        background = pygame.image.load(dataBackground)
        screen.blit(background, (0, 0))

pygame.mixer.init()
#Background music
class BackgroundMus:
    def __init__(self, music):
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)

#Text Box
font = pygame.font.SysFont('ARIAL', 32)
class TextBox:
    def drawing_text(self, msg):
        text_surface = font.render(msg, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (screen_width / 2, screen_height / 2)
        screen.blit(text_surface, text_rect)

    def drawing_timer(self, msg):
        text = font.render(msg, True, (255, 255, 255))
        screen.blit(text, (screen_width / 2 - 500, screen_height / 2))
#Button
clicked = False

class Button:

    button_col = (127, 127, 127) #Abu-abu
    hover_col = (255, 0, 0) #Merah
    click_col = (255, 255, 255) #putih
    text_col = (0, 0, 0) #hitam
    width = 280
    height = 40

    def __init__(self, x, y , text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):

        global clicked
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #create pygame Rect obect for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        #check mousehover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)

        #Button shading
        pygame.draw.line(screen, (255,255,255), (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, (0, 0, 0), (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        #adding text into button
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width/2) - int(text_len / 2), self.y + 5))
        return action

#Clock
clock = pygame.time.Clock()

#Clock and Timer
current_time = 0
pressed_button = 0
time = 300

#Game Loop
running = True

nodeTree = bst.root #Default Node Tree adalah Root

backgroundfile = pygame.image.load(nodeTree.dataGame[0][0]) #Default background awal game
#List of text
index1 = 0 #Default Index

#Untuk memunculkan Text baru
newText = ''

#Agar Choice tidak dijalankan pada tahap awal dan diset True jika sudah sampai terakhir
kePilihan = False

#Untuk play music
awal = True

returnBut = None
while running:
    # updating screen dengan warna hitam 0,0,0
    screen.fill((0, 0, 0))

    sfxSementara = 'dark-forest.wav'
    pygame.mixer.Sound(sfxSementara).play()

    current_time = pygame.time.get_ticks() #Return miliseconds
    # if(current_time <= 3000 and current_time >= 2900): #3 detik
    screen.blit(backgroundfile, (0, 0))

    if awal:
        pygame.mixer.music.load(nodeTree.dataGame[0][1])
        pygame.mixer.music.play()
        awal = False

    for event in pygame.event.get():
        #Jika quit ditekan
        if event.type == pygame.QUIT:
            running = False
        #Jika left mouse button ditekan
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.music.load("screen_click.wav")
            pygame.mixer.music.play()
            # pressed_button = pygame.time.get_ticks()
            if index1 != len(nodeTree.dataGame[1]) and not kePilihan:
                newText = nodeTree.dataGame[1][index1]
                index1 += 1
                time = 300
            else:
                index1 = 0
                kePilihan = True
    # current_time = pygame.time.get_ticks()

    if (kePilihan):
        if nodeTree.dataGame[2][0] == None:
            newText = 'Restart to play again'
            TextBox().drawing_text(newText)
        else:
            textBut1 = Button(screen_width // 2 - 300, screen_height // 2, nodeTree.dataGame[2][0])
            textBut2 = Button(screen_width // 2, screen_height // 2, nodeTree.dataGame[2][1])
            time -= 1
            TextBox().drawing_timer(str(time))
            if (time == 0):
                newText = 'You die, take too much time too choice. Restart to play again'
                nodeTree = ''
                TextBox().drawing_text(newText)
                kePilihan = False
            if textBut1.draw_button():
                stk.push(nodeTree)
                nodeTree = bst.search(nodeTree.nextVal[0])
                newText = ''
                backgroundfile = pygame.image.load(nodeTree.dataGame[0][0])
                kePilihan = False
                awal = True
            if textBut2.draw_button():
                stk.push(nodeTree)
                nodeTree = bst.search(nodeTree.nextVal[1])
                newText = ''
                backgroundfile = pygame.image.load(nodeTree.dataGame[0][0])
                kePilihan = False
                awal = True
    else:
        TextBox().drawing_text(newText)
        returnBut = Button(100, 100, 'back')
        if returnBut.draw_button():
            if stk.peek() == None:
                newText = "There's no return"
                TextBox().drawing_text(newText)
            else:
                nodeTree = stk.pop()
                newText = ''
                backgroundfile = pygame.image.load(nodeTree.dataGame[0][0])
                kePilihan = False
                awal = True
    pygame.display.update()
