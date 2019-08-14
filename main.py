


from gameData import *
from pygame.locals import *

game = Game() # Класс настроек



######### Инициализация сетки #########
cells = Cells(20,game.resolution) # Создаем сетку
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


for i in range(0,20):
    pesosus.append(Person(str(i)))

count = 1000
Play = 1
while Play ==1:
    running = True
    
    sc.fill(game.colors['white'])# Заливка


    cell_visualisator(sc,cells.cells,2) # Работает медленно, нужно отображение переделывать/ Курю документацию
    
    drawer.drawObjects(Objects.objects,sc)
    
    count = 0
    tag_list = []

    for key1 in Objects.objects: # обработка всех объектов

        #Objects.objects[key1].pos_in_cell = find_cell_pos(cells,Objects.objects[key1])

        Objects.objects[key1].movenment()
        if  Objects.objects[key1].death()==True:
            tag_list.append(key1)


        for key2 in Objects.objects:
            if key1 in Objects.objects or key2 in Objects.objects:
                if Objects.objects[key1].position == Objects.objects[key2].position:
                    if Objects.objects[key1].gender != Objects.objects[key2].gender:
                        if  Objects.objects[key1].age > 1:
                            count +=1
                    elif Objects.objects[key1].gender == Objects.objects[key2].gender and key1 != key2:
                        tag_list.append(key1)


    for tag in tag_list:
        if tag in Objects.objects:
            del Objects.objects[tag]
    


        
     
    for i in range(0,count):
        pesosus.append(Person(str(i)))
    
    per_limit = 300

    if (len(Objects.objects)) > per_limit:
        tagg = list(Objects.objects.keys())
        rand.shuffle(tagg)
        tagg = tagg[per_limit:]
        for tag in tagg:
            if tag in Objects.objects:
                del Objects.objects[tag]

   


   
    for event in pygame.event.get():
        if event.type==QUIT:
            Play = 0
                  
    game.refresh_screen(15) # Обновляет экран 
pygame.quit ()
    




