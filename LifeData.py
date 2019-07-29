import random as rand
import pygame
import time 


class Game():
    colors = {'black': (0,0,0),
                    'white':(255,255,255),
                    'red':(255,0,0),
                    'green':(0,255,0),
                    'blue':(0,0,255)}

    resolution = 1200,600  # размер экрана

    fps_controller = pygame.time.Clock()
    
        
    def refresh_screen(self,fps):
        """Обновляет экран с заданным числом кадров. Принимает ФПС"""
        pygame.display.flip()
        self.fps_controller.tick(fps)
        pygame.display.update()

class Cells():
    def __init__(self,):
        self.cells = {}


    def cells_generator(self,size):
        height, width = size
        i = 0
        for h in range(0,height,10):
            for w in range(0,width,10):
                self.cells[i] = Cell((h,w),False)
                i+=1

class Cell():
    def __init__(self, pos, fill):
        self.size = 10
        self.pos = pos
        self.fill = False
    
class Objects():
    objects = {}

    statistic = {'personObject':0,
                 'staticObject':0,
                 'dynamicObject':0
                 }

    def get_object(obj):
        Objects.objects[obj.class_name] = obj
        Objects.statistic[obj.class_tag] = Objects.statistic[obj.class_tag] + 1
    
    

class Person():
    def __init__(self, name):
        self.class_name = 'Person' + str(Objects.statistic['personObject'])
        self.class_tag = 'personObject'
        self.name = name

        # Особенности
        self.gender = self.random_gender()
        
        # параметры организма
        self.health = 100
        self.starve = 10
        self.alive = True

        # Местоположение
        self.position = 500,300 # НУжно переделать
        self.step = 20


        Objects.get_object(self)
    

    def random_gender(self):
        genders = ['male','female']
        return rand.choice(genders)

    def movenment(self):
        move_direction = [0,1,2,3,4,5,6,7,8] # Направления дввижения.  1 - лево
        move = rand.choice(move_direction)
        x,y = self.position

        if move == 1: 
            x-=10
        if move == 2:
           x-=10 
           y+=self.step
        if move == 3: 
            y+=10
        if move == 4: 
            x+=10
            y+=self.step
        if move == 5: 
            x+=10
        if move == 6: 
            x+=10
            y-=self.step
        if move == 7: 
            y-=10
        if move == 8: 
            x-=10 
            y-=self.step

        self.position = x,y

    def sensor(self):
        pass
       

    def life_control(self):
        print('poseluy mou zalupu')
        print('incest with young boys')

    def face_to_face(self,person2):
        '''Обработка встречи, если одинаковый пол то махач, если разный то чпоканье'''
        if self.gender == person2.gender:
            if self.health > person2.health:
                del person2
            if self.health < person2.health:
                del self
        #else:
           #person = Person(self.name + person2.name)
         # Я не знаю как правильно это написать, создание нового перса, и еще
         # не уверен что удаление персов тоже сработает

class Food():
    def __init__(self):
        
        self.position = 1,1

class Spawner():
    '''Спавнит объекты'''
    pass


class Drawer():
    def drawObjects(self,objects,screen):
        '''Рисует принятый объект(ы)'''
        for object in objects:
            pygame.draw.rect(screen, Game.colors['black'], self.pos_to_draw(objects[object].position))

    def pos_to_draw(self, position):
            '''Преобразует центральные координаты в координаты для квадрата'''
            size = 10
            x,y = position
            return  x - size, y - size, size * 2, size * 2