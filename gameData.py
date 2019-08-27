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
        
        
        
        self.grid_step = grid_step # Расстояние между точками
        self.grid_size = grid_size # Размер сетки (int высота и ширина)


        height, width = self.grid_size
        self.vert_len = height//grid_step # Длинна сетки


        #limints для ограничения движения
        self.up_limits = []
        self.down_limits = []


        self.grid_generator() # генерирует сетку присоздании экземпляра


    def grid_generator(self):
        '''Яенерирует ячейки'''
        height, width = self.grid_size
        i = 0
        for h in range(0,height,self.grid_step):
            self.up_limits.append(i)
            self.down_limits.append(i + (width//self.grid_step)-1)
            for w in range(0,width,self.grid_step):
                self.vertices[i] = Vertex(i,(h,w))
                i+=1


    def random_vertex(self):
        vert = rand.choice(self.vertices)
        return vert.index


class Vertex():
    '''Объект ячейки'''
    def __init__(self,index, pos):
        #self.size = 10
        self.index = index
        self.pos = pos
        self.object = None
    
class Object():
    objects = {}

    statistic = {'personObject':0,
                 'staticObject':0,
                 'dynamicObject':0
                 }

    def get_object(obj):
        Object.objects[obj.class_name] = obj
        Object.statistic[obj.class_tag] = Object.statistic[obj.class_tag] + 1
    
    

class Person():
    def __init__(self,grid,position):
        self.class_name = 'Person' + str(Object.statistic['personObject'])
        self.class_tag = 'personObject'
        

        self.grid = grid


        # Особенности
        
        self.age = 10 # возраст
        self.gender = self.random_gender()
        self.name = self.nameos()
        
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
        self.position = position # теперь замена posincell

        self.life_time = 0

        

        
        #print(str(self))

    
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

    def random_position(self,vertices):
        pass

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
        
    


    def movenment(self):
        '''Обработчик движения'''
        move_direction = [0,1,2,3,4,5,6,7,8] # Направления дввижения.  1 - Вверх
        #move_direction = [1] # Направления дввижения.  1 - Вверх
        move = rand.choice(move_direction)
        
        temp_pos = self.position
        vert_pos = self.around_vert()
                
        if move in [8,1,2]:
            if vert_pos[0] not in self.grid.up_limits:
                temp_pos = vert_pos[move]
        elif move in [4,5,6]:
            if vert_pos[0] not in self.grid.down_limits:
                temp_pos = vert_pos[move]
        else: 
            temp_pos = vert_pos[move]

        if temp_pos in self.grid.vertices:
            self.position = temp_pos

  
    def around_vert(self):
        '''Получает индексы ячеек вокруг песра'''

        vert_len = self.grid.vert_len/2

        vert_pos = [] # 0 - текущий индекс 1 - верх

        vert_pos.append(self.position)
        vert_pos.append(self.position - 1)
        vert_pos.append(self.position - vert_len - 1)
        vert_pos.append(self.position - vert_len)
        vert_pos.append(self.position - vert_len + 1)
        vert_pos.append(self.position + 1)
        vert_pos.append(self.position + vert_len + 1)
        vert_pos.append(self.position + vert_len)
        vert_pos.append(self.position + vert_len - 1 )

        return vert_pos

    def sensor(self,grid):
        '''Сканирует пространство вокруг объекта'''
        pass

    def golod(self):
        if self.life_time == 10:
            self.age +=1
            self.life_time = 0
        #if self.starve > 100:
            #self.health -=1

   
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
    def __init__(self):
        
        self.position = 1,1

class Spawner():
    '''спавнит объекты'''
    spawnlist = []
    def SpawnObject(grid,position = 1, type = 'person'):
        if type == 'person':
            Object.get_object(Person(grid, position))
        if type == 'huerson':
            print('sosi huy')
       


class Drawer():
    def __init__(self):
        self.size = 10


    def drawObjects(self,object,grid,screen):
        '''Рисует принятый объект(ы)'''
        pygame.draw.rect(screen, object.color, self.pos_to_draw_rect(grid.vertices[object.position].pos))
            #self.size = objects[object].size #приблуда чтобы по размеру отрисовывались

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


    