import random as rand
import pygame
import time 
#from miscLife import*
class Game():
    colors = {'black': (0,0,0),
                    'white':(255,255,255),
                    'red':(255,0,0),
                    'green':(0,255,0),
                    'blue':(0,0,255)}

    resolution = 1200,600  # размер экрана

    fps_controller = pygame.time.Clock() # Системная надстройка


    #Глобальные переменные

    #names = namegen()
    
        
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

class Cells():
    def __init__(self,cell_size,sells_size):
        '''Создает сетку. Принимает в виде аргумента шаг.'''
        self.cells = {}
        self.cell_size = cell_size # Расстояние между точками


        self.cells_size = sells_size # Размер самой сетки
        height, width = self.cells_size
        self.cells_len = height//cell_size

        self.cells_generator()

    def cells_generator(self):
        '''Яенерирует ячейки'''
        height, width = self.cells_size
        i = 0
        for h in range(0,height,self.cell_size):
            for w in range(0,width,self.cell_size):
                self.cells[i] = Cell((h,w))
                i+=1

class Cell():
    '''Объект ячейки'''
    def __init__(self, pos):
        #self.size = 10
        self.pos = pos
        self.fill = False
        self.object = None
    
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
        

        # Особенности
        
        self.age = 1 # возраст
        self.gender = self.random_gender()
        self.name = 'хир'#self.nameos()
        
        # параметры организма
        self.health = 100
        
        self.starve = 0
        self.alive = True
        self.eat = False
        self.size = 10 #размер ебаного организма
        
        self.color = self.gender_color()
        #self.cells = persData
        

        self.sensetive = 1 # Чуствительность

        # Местоположение
        self.position = 0,0 # НУжно переделать
        self.pos_in_cell = 0
        self.step = 10
        self.life_time = 0

        
        Objects.get_object(self)
        
        print(str(self))

    
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

    def random_position(self):
        '''Возвращает случайную позицию с учетом сетки'''
        pos = []
        x,y = Game.resolution
        for i in range(0,y,20):
            pos.append(i)
        return rand.choice(pos),rand.choice(pos)

    def death_reason(self):
        ''' Различный причины смерти пиздюка'''
        if self.age >= 40:
            self.alive = False
        if self.health <= 0:
            self.alive = False
    
    def death(self):
        if self.alive == False:
            return True
        else:
            return False
        
    


    def movenment(self,cells):
        '''Обработчик движения'''
        move_direction = [0,1,2,3,4,5,6,7,8] # Направления дввижения.  1 - лево
       # move_direction = [3] # Направления дввижения.  1 - Вверх
        move = rand.choice(move_direction)
        
        cell_len = cells.cells_len/2
        new_pos_in_cell = self.pos_in_cell
        x,y = self.position
        if move == 1:
            new_pos_in_cell = self.pos_in_cell - 1
        if move == 2:
            new_pos_in_cell = self.pos_in_cell - cell_len - 1
        if move == 3: 
            new_pos_in_cell = self.pos_in_cell - cell_len
        if move == 4:
            new_pos_in_cell = self.pos_in_cell - cell_len + 1
        if move == 5:
            new_pos_in_cell = self.pos_in_cell + 1
        if move == 6:
            new_pos_in_cell = self.pos_in_cell + cell_len + 1
        if move == 7:
            new_pos_in_cell = self.pos_in_cell + cell_len
        if move == 8: 
            new_pos_in_cell = self.pos_in_cell + cell_len - 1    
        
        if new_pos_in_cell in cells.cells:
            self.pos_in_cell = new_pos_in_cell

    def movenment_old(self):
        move_direction = [0,1,2,3,4,5,6,7,8] # Направления дввижения.  1 - лево
        move = rand.choice(move_direction)
        step = 1
        x,y = self.position
        if move == 1:
            if x > 5:
                x-=self.step
        if move == 2:
            if x > 5 and y < 600:
               x-=self.step 
               y+=self.step
        if move == 3: 
            if y < 600:
             y+=self.step
        if move == 4: 
            if x < 1200 and y < 600:
                x+=self.step
                y+=self.step
        if move == 5: 
            if x < 1200:
                x+=self.step
        if move == 6: 
            if x < 1200 and y > 5:
                x+=self.step
                y-=self.step
        if move == 7:
            if y > 5:
                y-=self.step
        if move == 8: 
            if x > 5 and y > 5:
                x-=self.step 
                y-=self.step
        self.starve +=1
        self.golod()
        self.life_time +=1
        self.death_reason()

        self.position = x,y
        

    def sensor(self):
        pass

    def golod(self):
        if self.life_time == 10:
            self.age +=1
            self.life_time = 0
        #if self.starve > 100:
            #self.health -=1

   
    def nameos(self):
        '''Возвращает имя из списка имен.'''
        m_names,f_names = Game.names
        if self.gender == "male":
            return rand.choice(m_names)
        if self.gender == "female":
            return rand.choice(f_names)

    def life_control(self):
       
        print('incest with  boys')


    def __str__(self):
        return 'Имя класса: {}\nИмя: {}\nПол: {}\nПозиция: {}\nПозиция в ячейке: {}'.format(self.class_name, self.name, self.gender, self.position, self.pos_in_cell)



class Food():
    def __init__(self):
        
        self.position = 1,1

class Spawner():
    '''спавнит объекты'''
    spawnlist = []
    pos = 10,10
    def SpawnObject(count = 1, type = 'person'):
        if type == 'person':
            pass
        if type == 'huerson':
            print('sosi huy')
        


class Drawer():
    def __init__(self):
        self.size = 10
    def drawObjects(self,objects,screen):
        '''Рисует принятый объект(ы)'''
        for object in objects:
            pygame.draw.rect(screen, objects[object].color, self.pos_to_draw_rect(objects[object].position))
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
def find_cell_pos(cells,person):
    '''Ищет позицию перса в ячейках.'''
    cells = cells.cells
    for cel in cells:
        if person.position == cells[cel].pos:
            return cel


# Временные функции
def cell_visualisator(screen,cells,radius):
    '''Отображает ячейки'''
    i = 1
    for cell in cells:
        pygame.draw.circle(screen,Game.colors['black'],cells[cell].pos,radius)
        i+=1


    