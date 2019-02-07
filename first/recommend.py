import math

from first.models import user, dishes


def recommend():
    user1 = user.objects.filter(id=1)
    dish1 = dishes.objects.all()
    list = []
    thelist=[]
    for i in user1:
        for item in dish1:
            a = i.price * item.dishes_price + i.cuisine * item.dishes_cursine + i.taste * item.dishes_taste + i.healthy * item.dishes_healthy
            b = math.sqrt(pow(i.price, 2) + pow(i.cuisine, 2) + pow(i.taste, 2) + pow(i.healthy, 2))
            c = math.sqrt(pow(item.dishes_price, 2) + pow(item.dishes_cursine, 2) + pow(item.dishes_taste, 2) + pow(
                item.dishes_healthy, 2))
            d = b * c
            j = a / d
            pen=j*(item.dishes_hot+1)*0.05
            list.append(pen)
    for g in range(len(list)):
        thelist.append(g+1)

    for n in range(len(list)):
        for m in range(len(list)-1):
            if(list[m]<list[m+1]):
                temp=list[m]
                list[m]=list[m+1]
                list[m+1]=temp
                temp2=thelist[m]
                thelist[m]=thelist[m+1]
                thelist[m+1]=temp2
    print(list)
    print(thelist)





