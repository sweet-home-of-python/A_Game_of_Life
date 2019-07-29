

from LifeData import *


game = Game() # Класс настроек


cells = Cells() # Создаем сетку

cells.cells_generator(game.resolution)

pygame.init()
sc = pygame.display.set_mode(game.resolution)
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
#sc.fill(game.colors['white']) # Заливка

Play = True # Запуск

drawer = Drawer()

while Play:
    sc.fill(game.colors['white'])# Заливка
    drawer.drawObjects(Objects.objects,sc)
        
    for obj_tag in Objects.objects: # обработка всех объектов
        Objects.objects[obj_tag].movenment()
        #Objects.objects[obj_tag].draw(sc)
    
    time.sleep(0.1)
    
    game.refresh_screen() # Обновляет экран



