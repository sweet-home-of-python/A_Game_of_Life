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
        #pygame.display.flip()
        self.fps_controller.tick(fps)
        pygame.display.update()

class Cells():
    def __init__(self,cells_size):
        '''Создает сетку. Принимает в виде аргумента шаг.'''
        self.cells = {}
        self.cells_size = cells_size


    def cells_generator(self,size):
        height, width = size
        i = 0
        for h in range(0,height,self.cells_size):
            for w in range(0,width,self.cells_size):
                self.cells[i] = Cell((h,w))
                i+=1

class Cell():
    def __init__(self, pos):
        #self.size = 10
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
    def __init__(self, name,persData,size,gender):
        self.class_name = 'Person' + str(Objects.statistic['personObject'])
        self.class_tag = 'personObject'
        self.name = name

        # Особенности
        self.gender = gender
        self.age = 1 # возраст
        # параметры организма
        self.health = 100
        self.starve = 0
        self.alive = True
        self.eat = False
        self.size = size #размер ебаного организма
        self.cells = persData
        

        # Местоположение
        self.position = 500,300 # НУжно переделать
        self.pos_in_cell = 0
        self.step = 20


        Objects.get_object(self)
    
    def random_gender(self):
        genders = ['male','female']
        return rand.choice(genders)

    def death_reason(self):
        ''' Различный причины смерти пиздюка'''
        if self.age >= 80:
            self.alive = False
        if self.health <=0:
            self.alive = False
    
    

    def movenment_new(self,cells):
        '''Обработчик движения'''
        move_direction = [0,1,2,3,4,5,6,7,8] # Направления дввижения.  1 - лево
        move = rand.choice(move_direction)
        x,y = self.position
        pos
        
        Cells.cells[i].fill = True

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
        self.starve +=1
        self.position = x,y
        
    def sensor(self):
        pass

    def golod(self):
        if self.starve > 30:
            self.health -=1

         

    def life_control(self):
       
        print('incest with  boys')

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


    def __str__(self):
        return 'Имя класса: {}\nИмя: {}\nПол: {}\nПозиция: {}\nПозиция в ячейке: {}'.format(self.class_name, self.name, self.gender, self.position, self.pos_in_cell)

class Food():
    def __init__(self):
        
        self.position = 1,1

class Spawner():
    '''Спавнит объекты'''
    pass


class Drawer():
    def __init__(self):
        self.size = 10
    def drawObjects(self,objects,screen):
        '''Рисует принятый объект(ы)'''
        for object in objects:
            pygame.draw.rect(screen, Game.colors['black'], self.pos_to_draw_rect(objects[object].position))
            self.size = objects[object].size #приблуда чтобы по размеру отрисовывались

    def pos_to_draw_rect(self, position):
            '''Преобразует центральные координаты в координаты для квадрата'''
            
            x,y = position
            return  x - self.size, y - self.size, self.size * 2, self.size * 2
    
    def pos_to_draw_circ(self,position):
        '''Преобразует центральные координаты в координаты для круга'''
        radius = 5
        return  position, radius

# Вспомогательные функции


def find_cells_pos(pers,cells):
        '''Ищет позицию перса в ячейках. Возможно нужно вынести в отдельную вспомогательную функцию'''
        for cel in cells.cells:
            if pers.position == cells.cells[cel].pos:
                pers.pos_in_cell = cel


# Временные функции

def cell_visualisator(screen,cells,radius):
    '''Отображает ячейки'''
    i =1
    for cell in cells:
        pygame.draw.circle(screen,Game.colors['black'],cells[cell].pos,radius)
        i+=1
    