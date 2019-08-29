


from gameData import *
from pygame.locals import *

game = Game() # Класс настроек



######### Инициализация сетки #########
grid = Grid(10,game.resolution) # Создаем сетку
#######################################


pygame.init()
pygame.font.init()
sc = pygame.display.set_mode(game.resolution, display=1)
pygame.display.set_caption('A Game of Life')




Play = True # Запуск

drawer = Drawer()


count = 1000
Play = True

filling_vertlist = []

while Play:
    
    sc.fill(game.colors['white'])# Заливка
    
    #cell_visualisator(sc,grid.vertices,2) # Работает медленно, нужно отображение переделывать/ Курю документацию
    
    
   # Вспомогтельные переменные 
    count = 0
    dead_list = []
    male_list = []
    female_list = []
    
    
    per_limit = 1000 # Лимит персонажей

        
        
        #------------ Обработка всех объектов --------------#

    for key in Object.objects:
        
        #lable = Object.objects[key].textolit() 
        #sc.blit(lable,(grid.vertices[Object.objects[key].position].pos[0]-30,grid.vertices[Object.objects[key].position].pos[1]-25))

        drawer.drawObjects(Object.objects[key],grid,sc) # Новая отрисовка
        
        
        if Object.objects[key].sex_or_die():
            count += 1

        Object.objects[key].handler() # Обработчик действий
        



        # Обработка смерти
            
        if  Object.objects[key].alive == False:
            dead_list.append(key)



    # Убирает список персов
    for tag in dead_list:
        if tag in Object.objects:
            del Object.objects[tag]
    

    
    

    if (len(Object.objects)) > per_limit:
        tagg = list(Object.objects.keys())
        rand.shuffle(tagg)
        tagg = tagg[per_limit:]
        for tag in tagg:
            if tag in Object.objects:
                del Object.objects[tag]




    for i in range(0,count):
        Spawner.SpawnObject(grid,grid.random_vertex())
   

    game.refresh_screen(20) # Обновляет экран 

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type==QUIT:
            Play = False
        if keys[pygame.K_ESCAPE]:
            Play = False
            pygame.quit()
        
        if keys[pygame.K_q]:
            for i in range(0,100):
                Spawner.SpawnObject(grid,grid.random_vertex())
           
            
          

pygame.quit ()
    




