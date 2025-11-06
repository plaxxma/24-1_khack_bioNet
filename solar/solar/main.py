import pygame
import random
import numpy as np
import copy
import time

import info
import gpt_question

# pygame 시작하기.
pygame.init()
pygame.display.set_caption("BIONET")
fps = pygame.time.Clock()

# 색 설정하기.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (210, 180, 140)

# 게임 폰트 설정하기.
pygame.font.init()
title_font = pygame.font.SysFont('Proxima Nova', 120)
font = pygame.font.SysFont('Proxima Nova', 40)

# 텍스트 출력 함수
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# 게임 screen 설정하기.
screen = pygame.display.set_mode((1600, 1000))
background = pygame.Surface((1600, 1000))
background.fill(BLACK, rect=[0, 0, 1600, 800])
background.fill(WHITE, rect=[0, 800, 1600, 200])

title = pygame.image.load('title.png')
title = pygame.transform.scale(title, (1000, 700))

woodboard = pygame.image.load('woodboard.png')
woodboard = pygame.transform.scale(woodboard, (1600, 200))

dashboard = pygame.image.load('dashboard.jpg')
dashboard = pygame.transform.scale(dashboard, (1500, 700))

button_message = pygame.image.load('button_message.png')
button_message = pygame.transform.scale(button_message, (150, 150))
button_search = pygame.image.load('button_search.png')
button_search = pygame.transform.scale(button_search, (150, 150))
button_shop = pygame.image.load('button_shop.png')
button_shop = pygame.transform.scale(button_shop, (150, 150))
button_back = pygame.image.load('button_back.png')
button_back = pygame.transform.scale(button_back, (150, 150))
button_quit = pygame.image.load('button_quit.png')
button_quit = pygame.transform.scale(button_quit, (125, 125 ))

soil_1 = pygame.image.load('soil_1.png')
soil_1 = pygame.transform.scale(soil_1, (32, 32))
soil_2 = pygame.image.load('soil_2.png')
soil_2 = pygame.transform.scale(soil_2, (32, 32))
soil_3 = pygame.image.load('soil_3.png')
soil_3 = pygame.transform.scale(soil_3, (32, 32))
soil_4 = pygame.image.load('soil_4.jpg')
soil_4 = pygame.transform.scale(soil_4, (32, 32))
soil_5 = pygame.image.load('soil_5.jpg')
soil_5 = pygame.transform.scale(soil_5, (32, 32))
soil_6 = pygame.image.load('soil_6.jpg')
soil_6 = pygame.transform.scale(soil_6, (32, 32))
soil_7 = pygame.image.load('soil_7.jpg')
soil_7 = pygame.transform.scale(soil_7, (32, 32))
soil_8 = pygame.image.load('soil_8.jpg')
soil_8 = pygame.transform.scale(soil_8, (32, 32))
soil_9 = pygame.image.load('soil_9.jpg')
soil_9 = pygame.transform.scale(soil_9, (32, 32))

send = pygame.image.load('send.png')
send = pygame.transform.scale(send, (32, 32))

cactus_1 = pygame.image.load('cactus_1.png')
cactus_1 = pygame.transform.scale(cactus_1, (64, 64))
cactus_2 = pygame.image.load('cactus_2.png')
cactus_2 = pygame.transform.scale(cactus_2, (64, 64))
cactus_3 = pygame.image.load('cactus_3.png')
cactus_3 = pygame.transform.scale(cactus_3, (64, 64))

tree_1 = pygame.image.load('tree_1.png')
tree_1 = pygame.transform.scale(tree_1, (64, 64))
tree_2 = pygame.image.load('tree_2.png')
tree_2 = pygame.transform.scale(tree_2, (64, 64))

palmtree = pygame.image.load('palmtree.png')
palmtree = pygame.transform.scale(palmtree, (64, 64))

water = pygame.image.load('water.png')
water = pygame.transform.scale(water, (32, 32))

snow_1 = pygame.image.load('snow_1.png')
snow_1 = pygame.transform.scale(snow_1, (32, 32))
snow_2 = pygame.image.load('snow_2.png')
snow_2 = pygame.transform.scale(snow_2, (32, 32))

scroll = pygame.image.load('scroll.png')
scroll = pygame.transform.scale(scroll, (1000, 100))
mini_scroll = pygame.image.load('scroll.png')
mini_scroll = pygame.transform.scale(mini_scroll, (700, 100))

left_arrow = pygame.image.load('left_arrow.png')
left_arrow = pygame.transform.scale(left_arrow, (150, 150))
right_arrow = pygame.image.load('right_arrow.png')
right_arrow = pygame.transform.scale(right_arrow, (150, 150))

cancel_button = pygame.image.load('cancel_button.jpg')
cancel_button = pygame.transform.scale(cancel_button, (180, 180))

abc = pygame.image.load('abc.png')
abc = pygame.transform.scale(abc, (64, 64))

map_grassland = pygame.image.load('map_grassland.png')
map_grassland = pygame.transform.scale(map_grassland, (240, 240))
map_desert = pygame.image.load('map_desert.png')
map_desert = pygame.transform.scale(map_desert, (240, 240))
map_beach = pygame.image.load('map_beach.png')
map_beach = pygame.transform.scale(map_beach, (240, 240))
map_mountain = pygame.image.load('map_mountain.png')
map_mountain = pygame.transform.scale(map_mountain, (240, 240))
map_arctic = pygame.image.load('map_arctic.png')
map_arctic = pygame.transform.scale(map_arctic, (240, 240))

mountain = pygame.image.load('mountain.png')
mountain = pygame.transform.scale(mountain, (480, 480))

ice_mountain_1 = pygame.image.load('ice_mountain_1.png')
ice_mountain_1 = pygame.transform.scale(ice_mountain_1, (240, 240))
ice_mountain_2 = pygame.image.load('ice_mountain_2.png')
ice_mountain_2 = pygame.transform.scale(ice_mountain_2, (240, 240))

one = pygame.image.load('one.png')
one = pygame.transform.scale(one, (100, 100))
two = pygame.image.load('two.png')
two = pygame.transform.scale(two, (100, 100))
three = pygame.image.load('three.png')
three = pygame.transform.scale(three, (100, 100))
four = pygame.image.load('four.png')
four = pygame.transform.scale(four, (100, 100))
five = pygame.image.load('five.png')
five = pygame.transform.scale(five, (100, 100))
six = pygame.image.load('six.png')
six = pygame.transform.scale(six, (100, 100))
seven = pygame.image.load('seven.png')
seven = pygame.transform.scale(seven, (100, 100))
eight = pygame.image.load('eight.png')
eight = pygame.transform.scale(eight, (100, 100))
nine = pygame.image.load('nine.png')
nine = pygame.transform.scale(nine, (100, 100))
zero = pygame.image.load('zero.png')
zero = pygame.transform.scale(zero, (100, 100))
multy = pygame.image.load('multy.png')
multy = pygame.transform.scale(multy, (100, 100))
digital_number = [
    zero,
    one,
    two,
    three,
    four,
    five,
    six,
    seven,
    eight,
    nine
]

mini_one = pygame.image.load('one.png')
mini_one = pygame.transform.scale(mini_one, (60, 60))
mini_two = pygame.image.load('two.png')
mini_two = pygame.transform.scale(mini_two, (60, 60))
mini_three = pygame.image.load('three.png')
mini_three = pygame.transform.scale(mini_three, (60, 60))
mini_four = pygame.image.load('four.png')
mini_four = pygame.transform.scale(mini_four, (60, 60))
mini_five = pygame.image.load('five.png')
mini_five = pygame.transform.scale(mini_five, (60, 60))
mini_six = pygame.image.load('six.png')
mini_six = pygame.transform.scale(mini_six, (60, 60))
mini_seven = pygame.image.load('seven.png')
mini_seven = pygame.transform.scale(mini_seven, (60, 60))
mini_eight = pygame.image.load('eight.png')
mini_eight = pygame.transform.scale(mini_eight, (60, 60))
mini_nine = pygame.image.load('nine.png')
mini_nine = pygame.transform.scale(mini_nine, (60, 60))
mini_zero = pygame.image.load('zero.png')
mini_zero = pygame.transform.scale(mini_zero, (60, 60))
mini_multy = pygame.image.load('multy.png')
mini_multy = pygame.transform.scale(mini_multy, (60, 60))

mini_digital_number = [
    mini_zero,
    mini_one,
    mini_two,
    mini_three,
    mini_four,
    mini_five,
    mini_six,
    mini_seven,
    mini_eight,
    mini_nine
]

coin = pygame.image.load('coin.png')
coin = pygame.transform.scale(coin, (128, 128))

heart = pygame.image.load('heart.png')
heart = pygame.transform.scale(heart, (64, 64))

fish = pygame.image.load('fish.png')
fish = pygame.transform.scale(fish, (180, 180))
meat = pygame.image.load('meat.png')
meat = pygame.transform.scale(meat, (180, 180))
fruit = pygame.image.load('fruit.png')
fruit = pygame.transform.scale(fruit, (180, 180))
vegetable = pygame.image.load('vegetable.webp')
vegetable = pygame.transform.scale(vegetable, (180, 180))

mini_fish = pygame.image.load('fish.png')
mini_fish = pygame.transform.scale(mini_fish, (135, 135))
mini_meat = pygame.image.load('meat.png')
mini_meat = pygame.transform.scale(mini_meat, (135, 135))
mini_fruit = pygame.image.load('fruit.png')
mini_fruit = pygame.transform.scale(mini_fruit, (135, 135))
mini_vegetable = pygame.image.load('vegetable.webp')
mini_vegetable = pygame.transform.scale(mini_vegetable, (135, 135))

mouse_pointer = pygame.image.load('mouse_pointer.png')
mouse_pointer = pygame.transform.scale(mouse_pointer, (50, 50))


# map 설정하기.
map_infomation = info.Map()

map_infomation.Append_Map("beach")
map_infomation.Append_Map("grassland")
map_infomation.Append_Map("desert")
map_infomation.Append_Map("beach")
map_infomation.Append_Map("mountain")
map_infomation.Append_Map("arctic")
map_infomation.Append_Map("arctic")
map_infomation.Append_Map("mountain")
'''
map_infomation.Append_Map("beach")
map_infomation.Append_Map("desert")
map_infomation.Append_Map("grassland")
'''

# list index 설정하기.
list_coord = 0

# animal book 설정하기.
animal_book = list()

# chat book 설정하기.
chat_book = list()

# 게임 button 설정하기.
buttons = [
    info.Button(115, 825, 75),
    info.Button(410, 825, 75),
    info.Button(730, 825, 75),
    info.Button(1025, 825, 75)
]

button_icon = [
    button_message,
    button_search,
    button_shop,
    button_back
]

button_map = list()
for i in range(10):
    if i < 5:
        x = (i + 1) * 65 + i * 240
        y = 100
    else:
        x = (i - 4) * 65 + (i - 5) * 240
        y = 460
    button_map.append(info.Button(x + 32.5, y + 32.5, 120))

button_arrow = [
    info.Button(225, 385, 75),
    info.Button(1375, 385, 75)
]

button_scroll = [
    pygame.Rect(300, 137 + 0 * 100, 1000, 100),
    pygame.Rect(300, 137 + 1 * 100, 1000, 100),
    pygame.Rect(300, 137 + 2 * 100, 1000, 100),
    pygame.Rect(300, 137 + 3 * 100, 1000, 100),
    pygame.Rect(300, 137 + 4 * 100, 1000, 100)
]

button_animal = [
    info.Button(1000, 385, 32),
    info.Button(900, 430, 32),
    info.Button(800, 200, 32),
    info.Button(700, 400, 32),
    info.Button(1400, 260, 32),
    info.Button(860, 185, 32),
    info.Button(1240, 690, 32),
    info.Button(500, 750, 32),
    info.Button(1324, 525, 32)
]

button_food = [
    info.Button(300, 230, 50),
    info.Button(880, 230, 50),
    info.Button(300, 470, 50),
    info.Button(880, 470, 50)
]

button_setting = [
    info.Button(307.5, 542.5, 67.5),
    info.Button(507, 557, 32)
]

# 돈 설정하기.
money = 20

# 물건 개수 설정하기.
food_list = [
    0,
    0,
    0,
    0
]

# 게임 stage 설정하기.
stage = [
    1, # 게임 처음 화면
    2, # map select 화면
    3, # map 1
    4, # map 2
    5, # map 3
    6, # map 4
    7, # map 5
    8, # map 6
    9, # map 7
    10, # map 8
    11, # map 9
    12, # map 10
    13, # message
    14, # message_select
    15, # search
    16, # mate_select
    17, # shop
    18 # character_select
]

currunt_stage = 1
previous_stage = -1
currunt_character = None

# 동물 구성하기.
animal_infomation = info.animal_list()
image_list = {}
image_big_list = {}
image_buffer = []
image_big_buffer = []
trash_name = []
for i in range(300):
    image_buffer.append(None)
    image_big_buffer.append(None)
    trash_name.append(None)
image_number = 1

# 초반 구성하기.
map_infomation.Append_Map("grassland")

shark = info.animal("shark", 0)
if "shark" not in image_list:
    gpt_question.image_create("shark", image_number)
    temp = pygame.image.load(f'generated_image_{image_number}.png')
    temp = pygame.transform.scale(temp, (64, 64))
    temp_2 = pygame.image.load(f'generated_image_{image_number}.png')
    temp_2 = pygame.transform.scale(temp_2, (250, 250))
    image_buffer[image_number - 1] = temp
    image_list["shark"] = image_buffer[image_number - 1]
    image_big_buffer[image_number - 1] = temp_2
    image_big_list["shark"] = image_big_buffer[image_number - 1]
    image_number += 1
cat = info.animal("cat", 0)
if "cat" not in image_list:
    gpt_question.image_create("cat", image_number)
    temp = pygame.image.load(f'generated_image_{image_number}.png')
    temp = pygame.transform.scale(temp, (64, 64))
    temp_2 = pygame.image.load(f'generated_image_{image_number}.png')
    temp_2 = pygame.transform.scale(temp_2, (250, 250))
    image_buffer[image_number - 1] = temp
    image_list["cat"] = image_buffer[image_number - 1]
    image_big_buffer[image_number - 1] = temp_2
    image_big_list["cat"] = image_big_buffer[image_number - 1]
    image_number += 1

animal_infomation.animal_append(shark, 0)
animal_infomation.animal_append(cat, 0)

if "shark" not in animal_book:
    animal_book.append("shark")
if "cat" not in animal_book:
    animal_book.append("cat")

play = True
while play:
    deltaTime = fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False     
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if currunt_stage == 1:
                for button in buttons:
                    if button.is_clicked(pos):
                        if button == buttons[3]:
                            play = False
                        else:
                            currunt_stage = 2
            elif currunt_stage == 2:
                for button in buttons:
                    if button.is_clicked(pos):
                        if button == buttons[0]:
                            currunt_stage = 13
                        elif button == buttons[1]:
                            currunt_stage = 15
                        elif button == buttons[2]:
                            currunt_stage = 17
                        elif button == buttons[3]:
                            currunt_stage = 1
                for index in range(10):
                    if button_map[index].is_clicked(pos) and map_infomation.idx >= index:
                        currunt_stage = index + 3
                        break 
            elif currunt_stage >= 3 and currunt_stage <= 12:
                for button in buttons:
                    if button.is_clicked(pos):
                        if button == buttons[0]:
                            currunt_stage = 13
                        elif button == buttons[1]:
                            currunt_stage = 15
                        elif button == buttons[2]:
                            currunt_stage = 17
                        elif button == buttons[3]:
                            currunt_stage = 2
                for button in button_animal:
                    if button.is_clicked(pos):
                        currunt_character = animal_infomation.animal_info[currunt_stage - 3][button_animal.index(button)]
                    
                    
                        print(currunt_character.food)
        
        
                        currunt_stage = 18
            elif currunt_stage == 13:
                for button in buttons:
                    if button.is_clicked(pos):
                        if button == buttons[0]:
                            currunt_stage = 13
                            list_coord = 0
                        elif button == buttons[1]:
                            currunt_stage = 15
                            list_coord = 0
                        elif button == buttons[2]:
                            currunt_stage = 17
                            list_coord = 0
                        elif button == buttons[3]:
                            currunt_stage = 2
                for button in button_scroll:
                    if button.collidepoint(pos):
                        temp = button_scroll.index(button)
                        if list_coord * 5 + temp < len(chat_book):
                            currunt_stage = 14
                            ...
                for button in button_arrow:
                    if button.is_clicked(pos):
                        if button == button_arrow[0]:
                            if list_coord > 0:
                                list_coord -= 1
                        elif button == button_arrow[1]:
                            list_coord += 1
            elif currunt_stage == 14:
                for button in buttons:
                    if button.is_clicked(pos):
                        if button == buttons[0]:
                            currunt_stage = 13
                            list_coord = 0
                        elif button == buttons[1]:
                            currunt_stage = 15
                            list_coord = 0
                        elif button == buttons[2]:
                            currunt_stage = 17
                            list_coord = 0
                        elif button == buttons[3]:
                            currunt_stage = 13    
            elif currunt_stage == 15:
                for button in buttons:
                    if button.is_clicked(pos):
                        if button == buttons[0]:
                            currunt_stage = 13
                            list_coord = 0
                        elif button == buttons[1]:
                            currunt_stage = 15
                            list_coord = 0
                        elif button == buttons[2]:
                            currunt_stage = 17
                            list_coord = 0
                        elif button == buttons[3]:
                            currunt_stage = 2
                for button in button_arrow:
                    if button.is_clicked(pos):
                        if button == button_arrow[0]:
                            if list_coord > 0:
                                list_coord -= 1
                        elif button == button_arrow[1]:
                            list_coord += 1
            elif currunt_stage == 16:
                for button in button_scroll:
                    if button.collidepoint(pos):
                        temp = button_scroll.index(button)
                        if list_coord * 5 + temp < len(animal_book):
                            mate_partner = animal_book[list_coord * 5 + temp]
                            baby = gpt_question.birth(currunt_character.name, mate_partner, map_infomation.map_list[currunt_character.world])
                            if baby[-1] == '.':
                                baby.replace('.', ' ')
                            if baby not in animal_book:
                                animal_book.append(baby)
                            trash_name[image_number] = info.animal(baby, 0)
                            if baby not in image_list:
                                gpt_question.image_create(baby, image_number)
                                temp = pygame.image.load(f'generated_image_{image_number}.png')
                                temp = pygame.transform.scale(temp, (64, 64))
                                temp_2 = pygame.image.load(f'generated_image_{image_number}.png')
                                temp_2 = pygame.transform.scale(temp_2, (250, 250))
                                image_buffer[image_number - 1] = temp
                                image_list[baby] = image_buffer[image_number - 1]
                                image_big_buffer[image_number - 1] = temp_2
                                image_big_list[baby] = image_big_buffer[image_number - 1]
                                image_number += 1
                            animal_infomation.animal_append(trash_name[image_number - 1], currunt_character.world)
                for button in button_arrow:
                    if button.is_clicked(pos):
                        if button == button_arrow[0]:
                            if list_coord > 0:
                                list_coord -= 1
                        elif button == button_arrow[1]:
                            list_coord += 1
                for button in buttons:
                    if button.is_clicked(pos):
                        if button == buttons[3]:
                            currunt_stage = 2   
            elif currunt_stage == 17:
                for button in buttons:
                    if button.is_clicked(pos):
                        if button == buttons[0]:
                            currunt_stage = 13
                        elif button == buttons[1]:
                            currunt_stage = 15
                        elif button == buttons[2]:
                            currunt_stage = 17
                        elif button == buttons[3]:
                            currunt_stage = 2 
                for button in button_food:
                    if button.is_clicked(pos) and money > 0:
                            money -= 1
                            food_list[button_food.index(button)] += 1
            elif currunt_stage == 18:
                for button in buttons:
                    if button.is_clicked(pos):
                        if button == buttons[0]:
                            currunt_stage = 13
                        elif button == buttons[1]:
                            currunt_stage = 15
                        elif button == buttons[2]:
                            currunt_stage = 17
                        elif button == buttons[3]:
                            currunt_stage = 2
                for button in button_setting:              
                    if button.is_clicked(pos):
                        if button == button_setting[0]:
                            if currunt_character.food == "Fish." and food_list[0] > 0:
                                food_list[0] -= 1
                                currunt_character.eat()
                            elif currunt_character.food == "Meat." and food_list[1] > 0:
                                food_list[1] -= 1
                                currunt_character.eat()
                            elif currunt_character.food == "Fruit." and food_list[2] > 0:
                                food_list[2] -= 1
                                currunt_character.eat()
                            elif currunt_character.food == "Vegetable." and food_list[3] > 0:
                                food_list[3] -= 1
                                currunt_character.eat()
                        elif button == button_setting[1]:
                            currunt_stage = 16
                            
                            


    # 화면 출력하기.
    screen.blit(background, (0, 0))
    screen.blit(woodboard, (0, 800))
    for i in range(4):
        screen.blit(button_icon[i], (buttons[i].x, buttons[i].y))
    
    screen.blit(coin,(1230, 815))
    screen.blit(mini_multy, (1370, 850))
    screen.blit(mini_digital_number[money // 10], (1440, 850))
    screen.blit(mini_digital_number[money % 10], (1520, 850))
    
    # icon 변경하기.
    if currunt_stage == 1:
        button_icon[3] = button_quit
    else:
        button_icon[3] = button_back  
        
    # stage 출력하기.
    if currunt_stage == 1:
        background.fill(BROWN, rect=[0, 0, 1600, 800])
        screen.blit(title, (300, 0))
        draw_text("Press any button!", title_font, BLACK, screen, 435, 640)
    elif currunt_stage == 2:
        map_infomation.draw_select_map(background, screen, map_grassland, map_desert, map_beach, map_mountain, map_arctic)
    elif currunt_stage >= 3 and currunt_stage <= 12:
        map_idx = currunt_stage - 3
        if map_infomation.map_list[map_idx] == "grassland":
            info.Map.draw_grassland(screen, soil_1, soil_2, soil_3, soil_4, soil_5, soil_6, soil_7, soil_8, water, tree_1, tree_2)
        elif map_infomation.map_list[map_idx] == "desert":
            info.Map.draw_desert(screen, send, cactus_1, cactus_2, cactus_3)
        elif map_infomation.map_list[map_idx] == "beach":
            info.Map.draw_beach(screen, send, water, palmtree)
        elif map_infomation.map_list[map_idx] == "mountain":
            info.Map.draw_mountain(screen, soil_1, soil_3, soil_4, soil_8, soil_9, water, mountain, tree_1, tree_2)
        elif map_infomation.map_list[map_idx] == "arctic":
            info.Map.draw_arctic(screen, snow_1, snow_2, water, ice_mountain_1, ice_mountain_2)
        for idx in range(animal_infomation.animal_idx[map_idx] + 1):
            animal_buffer = animal_infomation.animal_info[map_idx][idx].name
            screen.blit(image_list[animal_buffer], (button_animal[idx].x - 16, button_animal[idx].y - 16))
    if currunt_stage == 13:
        info.Map.draw_dashboard(background, screen, dashboard)
        info.Map.draw_scroll(screen, scroll, left_arrow, right_arrow)
        for i in range(5):
            if list_coord * 5 + i < len(chat_book):
                draw_text(chat_book[list_coord * 5 + i], font, BLACK, screen, 450, 170 + i * 100)
    if currunt_stage == 14:
        info.Map.draw_dashboard(background, screen, dashboard)
    if currunt_stage == 15:
        info.Map.draw_dashboard(background, screen, dashboard)
        info.Map.draw_scroll(screen, scroll, left_arrow, right_arrow)
        for i in range(5):
            if list_coord * 5 + i < len(animal_book):
                draw_text(animal_book[list_coord * 5 + i], font, BLACK, screen, 450, 170 + i * 100)
    if currunt_stage == 16:
        info.Map.draw_dashboard(background, screen, dashboard)
        info.Map.draw_scroll(screen, scroll, left_arrow, right_arrow)
        for i in range(5):
            if list_coord * 5 + i < len(animal_book):
                draw_text(animal_book[list_coord * 5 + i], font, BLACK, screen, 450, 170 + i * 100)
    if currunt_stage == 17:
        info.Map.draw_dashboard(background, screen, dashboard)
        info.Map.draw_food(screen, cancel_button, fish, meat, fruit, vegetable)
        info.Map.draw_number(screen, digital_number, 565, 230, food_list[0] // 10, food_list[0] % 10, multy)
        info.Map.draw_number(screen, digital_number, 1150, 230, food_list[1] // 10, food_list[1] % 10, multy)
        info.Map.draw_number(screen, digital_number, 565, 470, food_list[2] // 10, food_list[2] % 10, multy)
        info.Map.draw_number(screen, digital_number, 1150, 470, food_list[3] // 10, food_list[3] % 10, multy)
    if currunt_stage == 18:
        info.Map.draw_dashboard(background, screen, dashboard)
        info.Map.draw_mini_scroll(screen, mini_scroll, left_arrow, right_arrow)
        draw_text(f"name: {currunt_character.name}", font, BLACK, screen, 775, 170 + 0 * 100)
        draw_text(f"character: {currunt_character.character}", font, BLACK, screen, 775, 170 + 1 * 100)
        draw_text(f"food: {currunt_character.food}", font, BLACK, screen, 775, 170 + 2 * 100)
        draw_text(f"habitat: {currunt_character.habitat}", font, BLACK, screen, 775, 170 + 3 * 100)
        draw_text(f"stress: {currunt_character.stress}", font, BLACK, screen, 775, 170 + 4 * 100)        
        if currunt_character.food == "Fish.":
            info.Map.draw_character(screen, image_big_list[currunt_character.name], mini_fish, heart)
        elif currunt_character.food == "Meat.":
            info.Map.draw_character(screen, image_big_list[currunt_character.name], mini_meat, heart)
        elif currunt_character.food == "Fruit.":
            info.Map.draw_character(screen, image_big_list[currunt_character.name], mini_fruit, heart)
        elif currunt_character.food == "Vegetable.":
            info.Map.draw_character(screen, image_big_list[currunt_character.name], mini_vegetable, heart)
    
    # 마우스 포인터 표시하기.
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(mouse_pointer,(mouse_x - 25, mouse_y - 25))
    
    # stress 증가시키기.
    for i in range(10):
        for idx in range(animal_infomation.animal_idx[i] + 1):
            if idx != -1:
                if time.time() - animal_infomation.animal_info[i][idx].time >= 10:
                    animal_infomation.animal_info[i][idx].time = time.time()
                    animal_infomation.animal_info[i][idx].stress += 40
                    temp = animal_infomation.animal_info[i][idx].is_stress()
                    if temp == 2:
                        chat_book.append(f"[wolrd{animal_infomation.animal_info[i][idx].world}] {animal_infomation.animal_info[i][idx].name} is rage!")
                    elif temp == 1:
                        chat_book.append(f"[wolrd{animal_infomation.animal_info[i][idx].world}] {animal_infomation.animal_info[i][idx].name} is dangerous!")

    # 화면 업데이트
    pygame.display.flip()
    
pygame.quit()