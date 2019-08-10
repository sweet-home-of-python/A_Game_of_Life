


from LifeData import *
import os

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

for i in range(0,10):
    pesosus.append(Person(str(i),persData,10))

Play = True # Запуск

drawer = Drawer()

print(Objects.objects)






while Play:
    sc.fill(game.colors['white'])# Заливка

    cell_visualisator(sc,cells.cells,2) # Работает медленно, нужно отображение переделывать/ Курю документацию
    
    drawer.drawObjects(Objects.objects,sc)
    
    
    info = ''
    for obj_tag in Objects.objects: # обработка всех объектов
        find_cells_pos(Objects.objects[obj_tag],cells)
        Objects.objects[obj_tag].movenment()
        cells.cells[Objects.objects[obj_tag].pos_in_cell].fill = True
        
        info += str(Objects.objects[obj_tag])

        print(info)
        os.system('cls')

    game.refresh_screen(10) # Обновляет экран 

    




