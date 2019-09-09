import random as rand
import pygame
import time 
import os
from pygame.locals import *

#from miscLife import*
class Game():
    colors = {'black': (0,0,0),
                    'white':(255,255,255),
                    'red':(255,0,0),
                    'green':(0,255,0),
                    'blue':(0,0,255),
                    'shit':(255,33,255)}

    resolution = 1200,600  # размер экрана

    fps_controller = pygame.time.Clock() # Системная надстройка


    #Глобальные переменные


        
    def refresh_screen(self,fps):
        """Обновляет экран с заданным числом кадров. Принимает ФПС"""
        #pygame.display.flip()
        self.fps_controller.tick(fps)
        pygame.display.update()


    def namegen():
        with open('data/m_names.txt') as f:
            m_names = f.read().splitlines()
        with open('data/f_names.txt') as f:
            f_names = f.read().splitlines()
        return m_names,f_names 



class Grid():
    def __init__(self, grid_step, grid_size):
        '''Создает сетку. Принимает в виде аргумента шаг.'''
        
        self.vertices = {} # Вершины всех ячеек
        
        self.filling_vertlist = []
        
        self.grid_step = grid_step # Расстояние между точками
        self.grid_size = grid_size # Размер сетки (int высота и ширина)

        self.allIndex = []

        self.grid_generator() # генерирует сетку присоздании экземпляра

    def grid_generator(self):
        '''Яенерирует ячейки'''
        height, width = self.grid_size
        iX = 0
        iY = 0
        for w in range(0,width,self.grid_step):
            for h in range(0,height,self.grid_step):
                key = iX,iY
                self.allIndex.append(key)
                self.vertices[key] = Vertex((iX,iY),(h,w))
                iX+=1
            iX = 0
            iY+=1


    def random_vertex(self):
        vert = rand.choice(self.allIndex)
        return vert


class Vertex():
    '''Объект ячейки'''
    def __init__(self, index, pos):
        #self.size = 10
        self.index = index
        self.pos = pos
        self.object = None
    
class Object():
    objects = {}

    statistic = {'person':0,
                 'static':0,
                 'dynamic':0,
                 'food':0
                 }

    def get_object(obj):
        Object.objects[obj.class_name] = obj
        Object.statistic[obj.tag] = Object.statistic[obj.tag] + 1
    


class Person():
    def __init__(self,grid,position):
        self.class_name = 'person' + str(Object.statistic['person'])
        self.tag = 'person'
        

        self.grid = grid


        # Особенности
        
        self.age = 0 # возраст
        self.gender = self.random_gender()
        self.name = self.nameos()
        self.spicies = 'human'
        
        # параметры организма
        self.health = 1000
        self.hunger = 0
        self.alive = True
        self.pohudel = 0


        self.eat = False

        self.size = 10 #размер ебаного организма
        
        self.color = self.gender_color()

        

        self.sensetive = 1 # Чуствительность

        # Местоположение
        self.position = position # теперь замена posincell

        self.life_time = 0

        
    def textolit(self):
        
        default_font = pygame.font.get_default_font()
        font_renderer = pygame.font.Font(default_font, 14)
        label = font_renderer.render(self.name,1,(0,0,0))
        return label

    def sobachya_zizn(self):
        if self.spicies == "sobaka":
            self.health = 10000
            self.starve = 10
            self.name = "Pyosina"
            self.size = 3
            self.color = Game.colors['red']

    def handler(self):
        '''Обрабатываец цикличные функции'''

        self.age +=1 # старение
        self.movenment() # Движение
        #self.sex_or_die() # Размножение   
        self.hunger += 1
        self.starve()
        
        # Обрабатывает голод
        self.death_reason()
        self.death()

    def random_gender(self):
        '''Генерирует пол особи'''
        genders = ['male','female']
        return rand.choice(genders)

    def gender_color(self):
        '''Генерирует цвет особи в зависимости от пола'''
        if self.gender == 'male':
            return Game.colors['black']
        if self.gender == 'female':
            return Game.colors['blue']

    def death_reason(self):
        ''' Различный причины смерти пиздюка'''
        #if self.age >= 40:
           # self.alive = False
        if self.health <= 0:
            self.alive = False
    
    def death(self):
        if self.alive == False:
            return True
        else:
            return False
        

    def movenment(self):
        '''Обработчик движения'''

        self.grid.vertices[self.position].object = None

        vertNone = self.sensor()[1]

        if len(vertNone) > 0:
            move = rand.choice(vertNone)
        else:
            move = self.position

        if move in self.grid.vertices:  # Нужно оптимизировать
            self.position = move
        
        self.grid.vertices[self.position].object = self
    
    def around_vert(self):
        '''Получает индексы ячеек вокруг песра'''

        vert_pos = [] # 0 - текущий индекс 1 - верх

        X,Y = self.position

        #vert_pos.append(self.position) # центр

        vert_pos.append((X,Y - 1))
        vert_pos.append((X + 1, Y - 1))
        vert_pos.append((X + 1,Y))
        vert_pos.append((X + 1,Y + 1))
        vert_pos.append((X,Y + 1))
        vert_pos.append((X - 1,Y + 1))
        vert_pos.append((X - 1,Y))
        vert_pos.append((X - 1,Y - 1))

        return vert_pos

    def sensor(self):
        '''Сканирует пространство вокруг объекта и возвращает индексы пустых и заполненных вершин'''
        vert_pos = self.around_vert()

        vertFill = []
        vertNone = []

        for vert in vert_pos:
            if vert in self.grid.vertices:
                if self.grid.vertices[vert].object == None:
                    vertNone.append(vert)
                else:
                    vertFill.append(vert)

        return vertFill, vertNone

    def kushat(self):
        vf = self.sensor()[0]
        for v in vf:
            object = self.grid.vertices[v].object
            if object.tag == 'food':
                self.hunger -= object.food_types[object.food]
                
                self.grid.vertices[v].object = None
                return (object.class_name)
                
        


        

    def sex_or_die(self):
        '''Убиваеи или шпехается, жеееесть!'''

        vertFill = self.sensor()[0]
        
        for vf in vertFill:
            if self.grid.vertices[vf].object.tag != 'food': 
                if self.grid.vertices[vf].object.gender != self.gender:
                    if self.gender == 'female':
                        return 666
                else:
                    if self.grid.vertices[vf].object.health != self.health:           
                        if self.grid.vertices[vf].object.health > self.health:
                            return self.class_name
                        if self.grid.vertices[vf].object.health < self.health:
                            return self.grid.vertices[vf].object.class_name

    def starve(self):
        if self.hunger > 50:
            self.health -=1
    
   
    def nameos(self):
        '''Возвращает имя из списка имен.'''

        m_names,f_names = Game.namegen()
        if self.gender == "male":
            return rand.choice(m_names)
        if self.gender == "female":
            return rand.choice(f_names)

    def life_control(self):
       
        print('incest with  boys')


    def __str__(self):
        return '\nИмя класса: {}\nИмя: {}\nПол: {}\nПозиция: {}\nПозиция в ячейке: {}'.format(self.class_name, self.name, self.gender, self.position, self.position)



class Food():
    
    def __init__(self,grid):
       self.class_name = 'food' + str(Object.statistic['food'])
       self.tag = 'food'
       self.position = grid.random_vertex()
       self.food_types = {'myaso': 100,'yabloko':15,'banan':25,'bulka hleba':80,'pivas':50,'steik':70,'olivie':70,'saurma':100,'adrenalin_rush':200,'kuba_libra':150}
       self.food = rand.choice(list(self.food_types.keys()))
       self.size = 4
       grid.vertices[self.position].object = self

class Spawner():
    '''спавнит объекты'''
    spawnlist = []
    def SpawnObject(grid,position=(0,0), type='person'):
        if type == 'person':
            Object.get_object(Person(grid, position))
        if type == 'huerson':
            print('sosi huy')
        if type == 'food':
            Object.get_object(Food(grid))
        #print(len(Object.objects))

class Drawer():
    def __init(self):
        self.size =10

    def drawObjects(self,object,grid,screen):
        '''Рисует принятый объект(ы)'''
        self.size = object.size #приблуда чтобы по размеру отрисовывались
        if object.tag =="food":
            self.size = object.size
            pygame.draw.circle(screen,Game.colors['shit'],grid.vertices[object.position].pos,object.size)
        else:
            self.size = object.size
            pygame.draw.rect(screen, object.color, self.pos_to_draw_rect(grid.vertices[object.position].pos))

    def pos_to_draw_rect(self, position):
        '''Преобразует центральные координаты в координаты для квадрата'''
        x,y = position
        return  x - self.size, y - self.size, self.size * 2, self.size * 2

# Вспомогательные функции


# Временные функции
def cell_visualisator(screen,cells,radius):
    '''Отображает ячейки'''
    i = 1
    for cell in cells:
        pygame.draw.circle(screen,Game.colors['black'],cells[cell].pos,radius)
        i+=1

def vertexInConsole(grid):
    verts = grid.vertices.keys()
    text = ''
    prvert = 0
    

    for key in  grid.vertices:
        if key[1] == prvert:
            if grid.vertices[key].object != None:
                text += ' 1 '
            else:
                text += ' 0 '
        else:
            prvert = key[1]
            text += '\n'
    os.system('cls')
    print(text)

    
        