import gpt_question
import pygame
import time

class Button:
    def __init__(self, x, y, radius, action=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.action = action
        
    def is_clicked(self, pos):
        return (self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2 < self.radius ** 2
    
    def scroll_clicked(self):
        ...

class animal:
    def __init__(self, name, world, stress = 0):
        # 사전에 있는 동물의 정보
        self.name = name
        self.character = gpt_question.personality()
        self.feature = gpt_question.three_characteristic(name)
        self.food = gpt_question.main_diet(name)
        self.habitat = gpt_question.where_live(name)
        
        # 동물의 스트레스, 위치, 시간
        self.stress = stress
        self.world = world
        self.time = time.time()
        
    def get_hunt(self, prey):
        hunter_result = gpt_question.hunt_result(self.name, prey)
        if hunter_result == "True":
            return 1
        else:
            return 0

    def is_stress(self):
        if self.stress >= 100:
            return 2 # 폭주
        elif self.stress >= 80:
            return 1 # 위험
        else:
            return 0 # 안전
    
    def eat(self):
        self.stress -= 100
        
    #def __del__(self):
        #return (f"[World {self.world + 1}] {self.name} is dead.")

class animal_list:
    def __init__(self, map_cnt = 0, map_animal_cnt = 0, animal_limit = 19):
        self.map_cnt = map_cnt
        self.map_animal_cnt = map_animal_cnt
        self.animal_limit = animal_limit
        self.animal_idx = list()
        self.animal_info = list()
        for i in range(10):
            self.animal_idx.append(-1)
            self.animal_info.append(list())
    
    def animal_append(self, animal_name, map_number):
        if self.animal_idx[map_number] + 1 <= self.animal_limit:
            self.animal_idx[map_number] += 1
            self.animal_info[map_number].append(animal_name)

class Map:
    def __init__(self, cnt = 9, idx = 0):
        self.cnt = cnt
        self.idx = idx
        self.map_list = list()
    
    def Check_Map_Cnt(self):
        if(self.idx) >= self.cnt:
            return 0
        else:
            return 1
    
    def Append_Map(self, map_name):
        self.map_list.append(map_name)
        self.idx += 1

    def draw_grassland(screen, soil_1, soil_2, soil_3, soil_4, soil_5, soil_6, soil_7, soil_8, water, tree_1, tree_2):
        for i in range(15):
            for j in range(15 + i):
                screen.blit(soil_1, (j * 32, i * 32))
                if j == 14 + i:
                    if i == 0:
                        screen.blit(soil_6, (j * 32, i * 32))
                    else:
                        screen.blit(soil_7, (j * 32, i * 32))
            for j in range(10):
                screen.blit(water, ((15 + i + j) * 32, i * 32))
            if i != 14:
                screen.blit(soil_2, ((25 + i) * 32, i * 32))
            else:
                screen.blit(soil_5, ((25 + i) * 32, i * 32))
            for j in range(26 + i, 50):
                screen.blit(soil_1, (j * 32, i * 32))
        for i in range(10):
            for j in range(29 - i):
                screen.blit(soil_1, (j * 32, ((i + 15) * 32)))
                if j == 28 - i:
                    if i == 9:
                        screen.blit(soil_6, (j * 32, ((i + 15) * 32)))
                    else:
                        screen.blit(soil_4, (j * 32, ((i + 15) * 32)))
            for j in range(10):
                screen.blit(water, ((29 - i + j) * 32, ((i + 15) * 32)))
            if i == 0:
                screen.blit(soil_5, ((39 - i) * 32, ((i + 15) * 32)))
            else:
                screen.blit(soil_8, ((39 - i) * 32, ((i + 15) * 32)))
            for j in range(40 - i, 50):
                screen.blit(soil_1, (j * 32, ((i + 15) * 32)))
        screen.blit(tree_1, (3 * 32, 1 * 32))
        screen.blit(tree_2, (41 * 32, 3 * 32))
        screen.blit(tree_1, (35 * 32, 7 * 32))
        screen.blit(tree_2, (8 * 32, 11 * 32))
        screen.blit(tree_1, (17 * 32, 14 * 32))
        screen.blit(tree_2, (45 * 32, 17 * 32))
        screen.blit(tree_1, (38 * 32, 20 * 32))
        screen.blit(tree_2, (11 * 32, 21 * 32))

    def draw_desert(screen, send, cactus_1, cactus_2, cactus_3):
        for i in range(50):
            for j in range(25):
                screen.blit(send, (i * 32, j * 32))
                
        screen.blit(cactus_1, (4 * 32, 3 * 32))
        screen.blit(cactus_2, (24 * 32, 1 * 32))
        screen.blit(cactus_3, (13 * 32, 7 * 32))
        screen.blit(cactus_1, (43 * 32, 5 * 32))
        screen.blit(cactus_2, (28 * 32, 15 * 32))
        screen.blit(cactus_3, (20 * 32, 17 * 32))
        screen.blit(cactus_1, (38 * 32, 20 * 32))
        screen.blit(cactus_2, (8 * 32, 20 * 32))
        screen.blit(cactus_3, (38 * 32, 12 * 32))

    def draw_beach(screen, send, water, palmtree):
        for i in range(25):
            for j in range(i + 1):
                screen.blit(water, (j * 32, i * 32))
            for j in range(i + 1, 50):
                screen.blit(send, (j * 32, i * 32))
        
        screen.blit(palmtree, (25 * 32, 3 * 32))
        screen.blit(palmtree, (13 * 32, 7 * 32))
        screen.blit(palmtree, (40 * 32, 3 * 32))
        screen.blit(palmtree, (27 * 32, 15 * 32))
        screen.blit(palmtree, (43 * 32, 16 * 32))
        screen.blit(palmtree, (34 * 32, 20 * 32))

    def draw_mountain(screen, soil_1, soil_3, soil_4, soil_8, soil_9, water, mountain, tree_1, tree_2):
        for i in range(50):
            for j in range(25):
                screen.blit(soil_1, (i * 32, j * 32))
        for i in range(5):
            for j in range(10):
                for k in range(4):
                    screen.blit(water, ((10 * i + j) * 32, (14 - i + k) * 32))
                screen.blit(soil_3, ((10 * i + j) * 32, (13 - i) * 32))
                screen.blit(soil_9, ((10 * i + j) * 32, (18 - i) * 32))
                if j == 0 and i != 0:
                    screen.blit(soil_8, ((10 * i + j) * 32, (18 - i) * 32))
                if j == 9 and i != 4:
                    screen.blit(soil_4, ((10 * i + j) * 32, (13 - i) * 32))
        screen.blit(mountain, (0, 0))
        screen.blit(mountain, (5 * 32, 1 * 32))
        screen.blit(tree_1, (20 * 32, 1 * 32))
        screen.blit(tree_2, (24 * 32, 7 * 32))
        screen.blit(tree_1, (29 * 32, 3 * 32))
        screen.blit(tree_2, (33 * 32, 6 * 32))
        screen.blit(tree_1, (38 * 32, 4 * 32))
        screen.blit(tree_2, (43 * 32, 1 * 32))
        screen.blit(tree_1, (2 * 32, 22 * 32))
        screen.blit(tree_2, (8 * 32, 19 * 32))
        screen.blit(tree_1, (15 * 32, 20 * 32))
        screen.blit(tree_2, (21 * 32, 18 * 32))  
        screen.blit(tree_1, (28 * 32, 21 * 32))
        screen.blit(tree_2, (34 * 32, 17 * 32))  
        screen.blit(tree_1, (40 * 32, 22 * 32))            
        screen.blit(tree_2, (46 * 32, 18 * 32))  

    def draw_arctic(screen, snow_1, snow_2, water, ice_mountain_1, ice_mountain_2):
        for i in range(19):
            for j in range(50):
                if i == 18:
                    screen.blit(snow_2, (j * 32, i * 32))
                else:
                    screen.blit(snow_1, (j * 32, i * 32))
        for i in range(19, 25):
            for j in range(50):
                screen.blit(water, (j * 32, i * 32))
        
        screen.blit(ice_mountain_1, (3 * 32, 18 * 32))
        screen.blit(ice_mountain_2, (13 * 32, 18 * 32))

    def draw_dashboard(background, screen, dashboard):
        background.fill((210, 180, 140), rect=[0, 0, 1600, 800])
        screen.blit(dashboard, (50, 50))

    def draw_scroll(screen, scroll, left_arrow, right_arrow):
        for i in range(5):
            screen.blit(scroll, (300, 137 + i * 100))
        screen.blit(left_arrow, (150, 310))
        screen.blit(right_arrow, (1300, 310))

    def draw_mini_scroll(screen, mini_scroll, left_arrow, right_arrow):
        for i in range(5):
            screen.blit(mini_scroll, (625, 137 + i * 100))
 
    def draw_food(screen, cancel_button, fish, meat, fruit, vegetable):
        screen.blit(cancel_button, (250, 180))
        screen.blit(cancel_button, (830, 180))
        screen.blit(cancel_button, (250, 420))
        screen.blit(cancel_button, (830, 420))
        screen.blit(fish, (250, 180))
        screen.blit(meat, (830, 180))
        screen.blit(fruit, (250, 420))
        screen.blit(vegetable, (830, 420))
  
    def draw_number(screen, digital_number, x, y, ten, one, multy):
        screen.blit(multy, (x - 130, y))
        screen.blit(digital_number[ten], (x, y))
        screen.blit(digital_number[one], (x + 130, y))
        
    def draw_character(screen, character_image, food, heart):
        screen.blit(character_image, (280, 210))
        screen.blit(food, (240, 475))
        screen.blit(heart, (475, 525))
                
    def draw_select_map(self, background, screen, map_grassland, map_desert, map_beach, map_mountain, map_arctic):
        background.fill((210, 180, 140), rect=[0, 0, 1600, 800])
        for i in range(min(self.idx, 10)):
            if i < 5:
                x = (i + 1) * 65 + i * 240
                y = 100
            else:
                x = (i - 4) * 65 + (i - 5) * 240
                y = 460

            if self.map_list[i] == "grassland":
                screen.blit(map_grassland, (x, y))
            elif self.map_list[i] == "desert":
                screen.blit(map_desert, (x, y))
            elif self.map_list[i] == "beach":
                screen.blit(map_beach, (x, y))
            elif self.map_list[i] == "mountain":
                screen.blit(map_mountain, (x, y))
            elif self.map_list[i] == "arctic":
                screen.blit(map_arctic, (x, y))
        
