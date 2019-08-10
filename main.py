


from lifeData import *


game = Game() # Класс настроек



######### Инициализация сетки #########
cells = Cells(20) # Создаем сетку
cells.cells_generator(game.resolution)
#######################################


pygame.init()
sc = pygame.display.set_mode(game.resolution, display=1)
pygame.display.set_caption('A Game of Life')


#celsc = pygame.display.set_mode(game.resolution, display=0)
#clock = pygame.time.Clock()

persData = cells


pesosus = []


Play = True # Запуск

drawer = Drawer()


for i in range(0,20):
    pesosus.append(Person(str(i),persData,10))

count = 1000

while Play:
    sc.fill(game.colors['white'])# Заливка



    cell_visualisator(sc,cells.cells,2) # Работает медленно, нужно отображение переделывать/ Курю документацию
    
    drawer.drawObjects(Objects.objects,sc)
    
    count = 0
    tag_list = []

    for obj_tag in Objects.objects: # обработка всех объектов
        Objects.objects[obj_tag].movenment()
        for obj_tag_2 in Objects.objects:
            if Objects.objects[obj_tag].position == Objects.objects[obj_tag_2].position:
                if Objects.objects[obj_tag].gender != Objects.objects[obj_tag_2].gender:
                    count +=1
                elif Objects.objects[obj_tag].gender == Objects.objects[obj_tag_2].gender and obj_tag != obj_tag_2:
                    tag_list.append(obj_tag)


    for tag in tag_list:
        if tag in Objects.objects:
            del Objects.objects[tag]
    


        
     
    for i in range(0,count):
        pesosus.append(Person(str(i),persData,10))
    tagg = []
    for tag
    
    print(len(Objects.objects))
            
    game.refresh_screen(10) # Обновляет экран 

    




