size = int(input("enter number  : "))
import random

list =[]
list_x = []
list_y = []
answer = []

for i in range(size) :
    help_list = []
    for j in range(size) :
        if j==0 and i==0 :
            help_list.append(0)   
        else:
            help_list.append(random.randint(0, 1))
        
    # print(len(help_list))
    list.append(help_list)
    print(help_list)



def Method(x,y,number):
    # print("the begining of method x = {} , y = {} , number = {}".format(x,y,number)  )

    # out of range list
    if x<0 or y<0 or x>size-1 or y>size-1:
        # print("out of range")
        return 1

    # divar
    if list[x][y] == 1 :
        # print("divar")
        return 1

    # masir tekrari
    for i in range(number):
        if list_x[i] == x and list_y[i] == y :
            # print("masir tekrari")
            return 1

    # save masir
    list_x.insert(number,x)
    list_y.insert(number,y)

    if x == size-1 and y == size-1 :
        print("answer found",end = "")
        help_array = []
        # fill array answer
        for i in range(number):
            help_array.append(list_x[i])
            help_array.append(list_y[i])
            print(" ({},".format(list_x[i]), end =" ")
            print("{}) ".format(list_y[i]), end =" ")
        # payan masir
        help_array.append(size-1)
        help_array.append(size-1)
        print(" ({},".format(size-1), end =" ")
        print("{}) ".format(size-1))

        answer.append(help_array)



    Method( x+1, y,   number+1)
    Method( x+1, y+1, number+1)
    Method( x+1, y-1, number+1)
    Method( x-1, y,   number+1)
    Method( x-1, y-1, number+1)
    Method( x-1, y+1, number+1)
    Method( x,   y+1, number+1)
    Method( x,   y-1, number+1)


Method(0,0,0)
if not answer:
    print("No Answer Fo xund !")
if answer :
    print(f"count answers : {len(answer)}")

input('press Enter ...')
