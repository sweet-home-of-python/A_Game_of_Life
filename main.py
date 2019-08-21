


from gameData import *
from pygame.locals import *

game = Game() # Класс настроек



######### Инициализация сетки #########
cells = Cells(10,game.resolution) # Создаем сетку
cells.cells_generator()
#######################################


pygame.init()
sc = pygame.display.set_mode(game.resolution, display=1)
pygame.display.set_caption('A Game of Life')


#celsc = pygame.display.set_mode(game.resolution, display=0)
#clock = pygame.time.Clock()сааывафвафывафыв

#persData = cells


pesosus = []


Play = True # Запуск

drawer = Drawer()


#for i in range(0,10):
#    pesosus.append(Person(str(i)))

count = 1000
Play = True
while Play:
    
    sc.fill(game.colors['white'])# Заливка


    cell_visualisator(sc,cells.cells,2) # Работает медленно, нужно отображение переделывать/ Курю документацию
    
    drawer.drawObjects(Objects.objects,sc)
    
    count = 0
    dead_list = []
    
    # Поиск позиции в ячейках
    for key in Objects.objects:
        Objects.objects[key].pos_in_cell = find_cell_pos(cells,Objects.objects[key])


    for key1 in Objects.objects: # обработка всех объектов

        
        Objects.objects[key1].movenment(cells)
        if Objects.objects[key1].pos_in_cell in cells.cells:

            Objects.objects[key1].position = cells.cells[Objects.objects[key1].pos_in_cell].pos


            cells.cells[Objects.objects[key1].pos_in_cell].object = Objects.objects[key1];


        if  Objects.objects[key1].death()==True:
            dead_list.append(key1)


        for key2 in Objects.objects:
             if key1 != key2:
                if Objects.objects[key1].position == Objects.objects[key2].position:
                    if Objects.objects[key1].gender != Objects.objects[key2].gender:
                        if  Objects.objects[key1].age > 1:
                            count +=1
                    elif Objects.objects[key1].gender == Objects.objects[key2].gender:
                        dead_list.append(key1)



    # Убирает список персов
    for tag in dead_list:
        if tag in Objects.objects:
            del Objects.objects[tag]
    


    if count>0:
        for co in range(0,count):
            Spawner.SpawnObject(random_cell_pos(cells)) # Спавнит пидорков 



    
    per_limit = 100

    if (len(Objects.objects)) > per_limit:
        tagg = list(Objects.objects.keys())
        rand.shuffle(tagg)
        tagg = tagg[per_limit:]
        for tag in tagg:
            if tag in Objects.objects:
                del Objects.objects[tag]

   
    for cell in cells.cells:
        cells.cells[cell].object = None




    game.refresh_screen(15) # Обновляет экран 

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type==QUIT:
            Play = False
        if keys[pygame.K_ESCAPE]:
            Play = False
            pygame.quit()
        
        if keys[pygame.K_q]:
            Spawner.SpawnObject(random_cell_pos(cells))

                    

pygame.quit ()
    




