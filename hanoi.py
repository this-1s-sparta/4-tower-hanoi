#the "show" function prints the current situation of the towers
#it is printed after each move
def show():
    for i in range (4):
        print(first[i], second[i] , third[i])
    print('   1       2       3   ')
    
#the "possible" function checks if the move can be done
#according to the game's rules
#possible(int(number_of_tower_we_want_to_move_to), the_first_empty_possition_of_that_tower_given_by_the_place_function)
def possible(x,y):
    if x<y:
        return True
    return False
    

#the "place" function finds the list's place that we will move from/to
#we always place at/ move from the first available possition 
#for x=1 (from) we check from top to bottom for the first NOT empty possition
#for x=2 (to) we check from bottom to top for the first empty possition
#place( 1_or_2_based_on_action , towers_number)
def place(x,check):
    #from
    if x==0:
        if check==1:
            for i in range (4):
                if first[i]!=empty:
                    return i
        if check==2:
            for i in range (4):
                if second[i]!=empty:
                    return i
        if check==3:
            for i in range (4):
                if third[i]!=empty:
                    return i
    #to
    if x==1:
        if check==1:
            for i in range (3,-1,-1):
                if first[i]==empty:
                    return i
        if check==2:
            for i in range (3,-1,-1):
                if second[i]==empty:
                    return i
        if check==3:
            for i in range (3,-1,-1):
                if third[i]==empty:
                    return i
bottom="*******"
middle_bottom=" ***** "
middle_top="  ***  "
top="   *   "
empty="       "
first=[top,middle_top,middle_bottom,bottom]
#first is tower 1
second=[empty]*4
#second is tower 2
third=[empty]*4
#third is tower 3

show()
print('RULES')
print('1. Only one disk may be moved at a time.')
print('2. Each move consists of taking the upper disk from one of the stacks')
print('   and placing it on top of another stack or on an empty rod.')
print('3. No disk may be placed on top of a disk that is smaller than it.', '\n')
print('Chose the number of the tower you want to move from/to when asked to')
end=False

#we repeat the while loop until the third tower is as it should be
while third!=[top,middle_top,middle_bottom,bottom] and end==False:
    start = input('from tower:')
    to = input('to tower:')
    p1 = place(0,int(start))
    p2 = place(1,int(to))
    if start=='1':
        if to=='2':
            first[p1],second[p2]=second[p2],first[p1]
            if p2!=3:
                if possible(second[p2],second[p2+1])==False:
                    end=True
        elif to=='3':
            first[p1],third[p2]=third[p2],first[p1]
            if p2!=3:
                if possible(third[p2],third[p2+1])==False:
                    end=True
    elif start=='2':
        if to=='1':
            second[p1],first[p2]=first[p2],second[p1]
            if p2!=3:
                if possible(first[p2],first[p2+1])==False:
                    end=True
        elif to=='3':
            second[p1],third[p2]=third[p2],second[p1]
            if p2!=3:
                if possible(third[p2],third[p2+1])==False:
                    end=True
    elif start=='3':
        if to=='1':
            third[p1],first[p2]=first[p2],third[p1]
            if p2!=3:
                if possible(first[p2],first[p2+1])==False:
                    end=True
        elif to=='2':
            third[p1],second[p2]=second[p2],third[p1]
            if p2!=3:
                if possible(second[p2],second[p2+1])==False:
                    end=True
    else:
        print('wrong input')
    show()
if end==True:
    print("you lost")
else:
    print('well played')