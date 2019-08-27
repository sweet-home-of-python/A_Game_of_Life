


from gameData import *
from pygame.locals import *

game = Game() # Класс настроек



######### Инициализация сетки #########
grid = Grid(40,game.resolution) # Создаем сетку
#######################################


pygame.init()
sc = pygame.display.set_mode(game.resolution, display=1)
pygame.display.set_caption('A Game of Life')


#celsc = pygame.display.set_mode(game.resolution, display=0)
#clock = pygame.time.Clock()сааывафвафывафыв

#persData = grid


pesosus = []


Play = True # Запуск

drawer = Drawer()


#for i in range(0,10):
#    pesosus.append(Person(str(i)))

count = 1000
Play = True

filling_vertlist = []

while Play:
    
    sc.fill(game.colors['white'])# Заливка

    cell_visualisator(sc,grid.vertices,2) # Работает медленно, нужно отображение переделывать/ Курю документацию
    
    
   # Вспомогтельные переменные 
    count = 0
    dead_list = []
    male_list = []
    female_list = []

    
    
    # Очистка ячеек
    for vert in filling_vertlist:
        grid.vertices[vert].object = None
    
    filling_vertlist = []




        #------------ Обработка всех объектов --------------#

    for key in Object.objects:
        
        key_pos = Object.objects[key].position
       
        grid.vertices[key_pos].object = Object.objects[key]
        
        filling_vertlist.append(key_pos)

        
        
        
        drawer.drawObjects(Object.objects[key],grid,sc) # Новая отрисовка


        Object.objects[key].movenment() # Обработчик движения






        # Обработка смерти
            
        if  Object.objects[key].alive == False:
            dead_list.append(key)



    


    # Убирает список персов
    for tag in dead_list:
        if tag in Object.objects:
            del Object.objects[tag]
    

    
    per_limit = 1000

    if (len(Object.objects)) > per_limit:
        tagg = list(Object.objects.keys())
        rand.shuffle(tagg)
        tagg = tagg[per_limit:]
        for tag in tagg:
            if tag in Object.objects:
                del Object.objects[tag]


    print(len(Object.objects))

    game.refresh_screen(15) # Обновляет экран 

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type==QUIT:
            Play = False
        if keys[pygame.K_ESCAPE]:
            Play = False
            pygame.quit()
        
        if keys[pygame.K_q]:
            for i in range(0,1):
                Spawner.SpawnObject(grid,grid.random_vertex())
          

pygame.quit ()
    




