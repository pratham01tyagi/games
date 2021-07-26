#                              Tipi-Tipi-top


l=['red','blue','white','purple',0]
nu=[[1,'gadha'],[2,'bewakuf'],[3,'hathi'],[4,'mental'],[5,'rich'],[6,'faku'],[7,'poor'],[8,'chor']]
print(l)
colour=input("tipi-tipi-top which colour you want\n".casefold())
print(f"you chose {colour}")

while colour in l:
    if (colour == 'red')or(colour =='white'):
        number=int(input("tipi-tipi-top which number you want - [3,4,7,8] \n".casefold()))
        print("you chosse {0} ".format(number))
        if (number == 3) or (number == 8):
            num3=int(input("tipi-tipi-top which number you want - [1,2,5,6] \n".casefold()))
            if (num3 == 1) or (num3 == 2) or (num3 == 5) or (num3 == 6):
                print("you are -{0} ".format(nu[num3][1]))
                break
            else:
                break
        elif (number == 4) or (number == 7) :
            numr=int(input("tipi-tipi-top which number you want - [3,4,7,8] \n".casefold()))
            if (numr == 3) or (numr == 4)  or (numr == 7)  or (numr == 8) :
                print("you are -{0}".format(nu[numr][1]))
                break
            else:
                break
        else:
            print("you entered wrong no start the game again")
            break

    elif (colour == 'blue') or (colour =='purple'):
        numb=int(input("tipi-tipi-top which number you want - [1,2,5,6] \n".casefold()))
        print("you chosse {0}".format(numb))
        if (numb == 1) or (numb == 2) or (numb == 6):
            num=int(input("tipi-tipi-top which number you want - [3,4,7,8] \n".casefold()))
            if (num == 3) or (num == 4) or (num == 7) or (num == 8):
                print("you are -{0}".format(nu[num][1]))
            else:
                break
        elif numb == 5:
            numq=int(input("tipi-tipi-top which number you want - [1,2,5,6] \n".casefold()))
            if (numq == 1) or (numq == 2) or (numq == 5) or (numq == 6):
               print("you are -{0}".format(nu[numq][1]))
            else:
                break
        else:
            print("you entered wrong no start the game again")
            break
    else:
        break
    