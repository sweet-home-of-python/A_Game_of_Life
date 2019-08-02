import random as rand


with open('data/m_names.txt') as f:
    m_names = f.read().splitlines()
with open('data/f_names.txt') as f:
    f_names = f.read().splitlines()
with open('data/podlezg.txt') as f:
    podlezg = f.read().splitlines()
with open('data/sush.txt') as f:
    sush = f.read().splitlines()



#for i in range(0,200):
    #print('{} {} {}'.format((rand.choice(m_names)),(rand.choice(podlezg)).lower(),(rand.choice(sush)).lower()))




def new_name(name1,name2):
    ''' создает новое имя из двух''' 
    dl1 = len(name1)
    sym1 = dl1 // 2
    dl2 = len(name2)
    sym2 = dl2 // 2
    name1 = name1[:sym1]
    name2 = name2[sym2:]
    name2 = name2.lower()
    result = (name1+name2)
    return result



for i in range(0,20):
    mn = rand.choice(m_names)
    fn = rand.choice(f_names)
    cn = new_name(fn,mn)

    #print('{} + {} = {}'.format(mn,fn,cn))

    print('{} {} {}'.format(cn,(rand.choice(podlezg)).lower(),(rand.choice(sush)).lower()))