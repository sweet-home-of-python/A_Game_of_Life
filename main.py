


from LifeData import *


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


pers = Person("Yarik", persData,10,"1")
pers2 = Person("Ya", persData,10, "2")

pesosus = []


Play = True # Запуск

drawer = Drawer()

print(Objects.objects)

i =x =0

    



while Play:
    sc.fill(game.colors['white'])# Заливка

    cell_visualisator(sc,cells.cells,2) # Работает медленно, нужно отображение переделывать/ Курю документацию
    
    drawer.drawObjects(Objects.objects,sc)
    
    
    for obj_tag in Objects.objects: # обработка всех объектов
        Objects.objects[obj_tag].movenment()
        while x != 10:
            if Objects.objects[0].position == Objects.objects[0].position:
                if pers.gender != pers2.gender:
                    pesosus.append(Person(str(i),persData,10,"loh"))
        #Objects.objects[obj_tag].find_cells_pos()
        #cells.cells[Objects.objects[obj_tag].pos_in_cell].fill = True
    
    
            
    game.refresh_screen(10) # Обновляет экран 

    




