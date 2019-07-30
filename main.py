

from LifeData import *


game = Game() # Класс настроек



######### Инициализация сетки #########
cells = Cells(10) # Создаем сетку
cells.cells_generator(game.resolution)
#######################################


pygame.init()
sc = pygame.display.set_mode(game.resolution, display=1)
pygame.display.set_caption('A Game of Life')


#celsc = pygame.display.set_mode(game.resolution, display=0)
#clock = pygame.time.Clock()



pers = Person("jake")# пиздюки
pers2 = Person("fin")
pers3 = Person("jake")
pers4 = Person("fin")
pers5 = Person("jake")
pers6 = Person("fin")
pers7 = Person("jake")
pers8 = Person("fin")
pers9 = Person("jake")
pers10 = Person("fin")


Play = True # Запуск

drawer = Drawer()

print(Objects.objects)






while Play:
    sc.fill(game.colors['white'])# Заливка
    cell_visualisator(sc,cells.cells,2) # Работает медленно, нужно отображение переделывать/ Курю документацию
 
    drawer.drawObjects(Objects.objects,sc)
        
    for obj_tag in Objects.objects: # обработка всех объектов
        Objects.objects[obj_tag].movenment()
    
    game.refresh_screen(30) # Обновляет экран 



