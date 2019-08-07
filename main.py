


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



pers = Person("Yarik", persData,100)

pesosus = []

for i in range(0,10):
    pesosus.append(Person(str(i),persData,10))

Play = True # Запуск

drawer = Drawer()

print(Objects.objects)






while Play:
    sc.fill(game.colors['white'])# Заливка

    cell_visualisator(sc,cells.cells,2) # Работает медленно, нужно отображение переделывать/ Курю документацию
    
    drawer.drawObjects(Objects.objects,sc)
    
    
    for obj_tag in Objects.objects: # обработка всех объектов
        Objects.objects[obj_tag].movenment()
        Objects.objects[obj_tag].find_cells_pos()
        cells.cells[Objects.objects[obj_tag].pos_in_cell].fill = True
    pers.golod()    
    if pers.health == 0:
        print(pers.name + " bolshe ne pridet")
    game.refresh_screen(10) # Обновляет экран 

    




