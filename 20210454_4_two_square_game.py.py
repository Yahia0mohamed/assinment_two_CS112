'''
name: yahia mohamed nabil
date of finish : 3/2/2022
assignment 1 second semester
game : two square game

'''
pc=1 #player counter
lisgame=["11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"] # game list

# function of the side ways square option
def side():
    # player check
    global pc
    if pc % 2 == 1:
        print("player one")
        pc+=1
    elif pc % 2 ==0:
        print("player 2")
        pc+=1
    print("side ways")
    s1=input("enter the first no.: ")
    s2=input("enter the second no.: ")
    # check if digit or not
    if s1.isdigit() and s2.isdigit():
        #check if in list or not
        if s1 in lisgame and s2 in lisgame:
            # getting the indexes of the two no. Chosen  and replace them with the game occupation character
            ins1=lisgame.index(s1)#ins: index side 
            ins2=lisgame.index(s2) 
            if ins2==(ins1+1):
                # check if the indexes satisfy the condition of the side ways or not
                lisgame[ins1] = "x "
                lisgame[ins2] = "x "
                print("|",lisgame[0],"|",lisgame[1],"|",lisgame[2],"|",lisgame[3],"|")
                print("|",lisgame[4],"|",lisgame[5],"|",lisgame[6],"|",lisgame[7],"|")
                print("|",lisgame[8],"|",lisgame[9],"|",lisgame[10],"|",lisgame[11],"|")
                print("|",lisgame[12],"|",lisgame[13],"|",lisgame[14],"|",lisgame[15],"|")
                check()
            else:
                # else not satisfy restarts the function
                print("choose another no.")
                pc-=1
                side()
        else:
            # else the two no. or one of them are not in list restarts the function
            print("choose a no. in the list")
            pc-=1
            side()
    else:
        # else the two are not digit or one of them restarts the function
        print("choose a digit")
        pc-=1
        side()

# function of the upright square option
def upright():
    #player check
    global pc
    if pc % 2 == 1:
        print("player one")
        pc+=1
    elif pc % 2 ==0:
        print("player 2")
        pc+=1
    print("up right")
    u1=input("enter the first no.: ")
    u2=input("enter the second no.: ")
    # check if the input is digit
    if u1.isdigit() and u2.isdigit():
        # check if the input in list
        if u1 in lisgame and u2 in lisgame:
            inu1=lisgame.index(u1) #inu: index upright
            inu2=lisgame.index(u2)
            if inu2==(inu1+4):
                # check if the indexes satisfy the condition of the upright or not
                lisgame[inu1] = "x "
                lisgame[inu2] = "x "
                print("|",lisgame[0],"|",lisgame[1],"|",lisgame[2],"|",lisgame[3],"|")
                print("|",lisgame[4],"|",lisgame[5],"|",lisgame[6],"|",lisgame[7],"|")
                print("|",lisgame[8],"|",lisgame[9],"|",lisgame[10],"|",lisgame[11],"|")
                print("|",lisgame[12],"|",lisgame[13],"|",lisgame[14],"|",lisgame[15],"|")
                check()
            else:
                # else not satisfy restarts the function
                print("choose another no.")
                pc-=1
                upright()
        else:
            # else the two no. or one of them are not in list restarts the function
            print("choose a no. in the list")
            pc-=1
            upright()
    else:
        # else the two are not digit or one of them restarts the function
        print("choose a digit")
        pc-=1
        upright()

def check():
    global pc
    for i in range(0,len(lisgame)):
        if i < 12:
            if i ==3 or i == 7 or i == 11:
                if (lisgame[i] !="x "):
                    if (lisgame[i+4] != "x "):
                        i = 0
                        break
            else:
                if (lisgame[i] !="x "):
                    if (lisgame[i+4] != "x "  or lisgame[i+1]!="x "):
                        i = 0
                        break
        elif i >=12 and i<=14:
            if (lisgame[i] !="x "):
                if (lisgame[i+1]!="x "):
                    i = 0
                    break
    if i == len(lisgame)-1:
        if pc % 2 == 1:
            print("print player 2 wins")
            exit(0)
        elif pc % 2 ==0:
            print("player 1 wins")
            exit(0)

def game():
    global pc
    global code
    code=True
    while code == True:
        opp=input("for side way (>)\nfor upright (^)\nto exit (x):")
        if opp == ">":
            side()
        elif opp == "^":
            upright()
        elif opp == "x":
            code = False
        else:
            print("choose again")
            game()



if __name__=="__main__":
    print("|",lisgame[0],"|",lisgame[1],"|",lisgame[2],"|",lisgame[3],"|")
    print("|",lisgame[4],"|",lisgame[5],"|",lisgame[6],"|",lisgame[7],"|")
    print("|",lisgame[8],"|",lisgame[9],"|",lisgame[10],"|",lisgame[11],"|")
    print("|",lisgame[12],"|",lisgame[13],"|",lisgame[14],"|",lisgame[15],"|")  
    game()