
import random as rand


with open('data/m_names.txt') as f:
    m_names = f.read().splitlines()
with open('data/f_names.txt') as f:
    f_names = f.read().splitlines()
with open('data/podlezg.txt') as f:
    podlezg = f.read().splitlines()
with open('data/sush.txt') as f:
    sush = f.read().splitlines()


class Chelovek():
    def __init__(self):
        self.name = rand.choice(m_names)

    def brosok(self):
        return rand.choice(['Орел','Решка'])
    def __str__(self):
        return self.name



people = []


for i in range(0,10000):
    people.append(Chelovek())


def otbor(people):
    lucky_people = []
    for chel in people:
        if chel.brosok() == 'Орел':
            lucky_people.append(chel)
    return lucky_people

i = 0
while len(people)>1:
    people = otbor(people)
    print(len(people))
    i+=1

if len(people)==1:
    print('\nПобедитель: {}. Продержался {} раз(а).'.format(str(people[0]),i))
else: print ('Все неудачники!')