import random
def load_data(file):
    data = dict() #id:(name,location,desc,hp,rizz,mana,height,weight,orbital_speed,egg)
    with open(file,'r') as f:
        for i in f.read().split('\n'):
            c = 0
            info = []
            for j in i.split(','):
                if c > 0:
                    info.append(j)
                else:
                    n = j
                c += 1
            data[int(n)] = info
        return data


def get_info(data,id,item):
    mast_inf = ['name','location','desc','hp','rizz','mana','height','weight','orbital_speed','egg']
    if item not in mast_inf or not(1 <= id <= 895):
        print('not valid id or item ')
        return None
    else:
        return data.get(int(id))[mast_inf.index(item)]

def comp(data,a,b,item):
    inf_a = get_info(data,a,item)
    if inf_a is None:
        return None
    if len(inf_a) > 2:
        print('Cannot compare this attribute, I need a number')
        return None
    inf_b = get_info(data,b,item)
    if int(inf_b) > int(inf_a):
        return b
    elif int(inf_b) < int(inf_a):
        return a
    else:
        return 0

def main():
    data = load_data('all_data.txt')
    while len(data) > 1:
        kys = list(data.keys())
        fighter_1 = random.choice(kys)
        fighter_2 = random.choice(kys)
        while fighter_2 == fighter_1:
            fighter_2 = random.choice(kys)
        attr = random.choice(['hp','rizz','mana','height','weight','orbital_speed','egg'])
        winner = comp(data,fighter_1,fighter_2,attr)
        name1 = get_info(data,fighter_1,"name")
        name2 = get_info(data,fighter_2,"name")
        if winner == fighter_1:
            del data[fighter_2]
            x = f'{name1} won'
        elif winner == fighter_2:
            del data[fighter_1]
            x = f'{name2} won'

        else:
            x = 'it was a draw'
        print(f'{name1} and {name2} fought in {attr} and {x}')
    print(f'The last one standing and the winner is {get_info(data,list(data.keys())[0],"name")}')

main()
