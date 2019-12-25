test_board=['@',' ',' ',' ',' ',' ',' ',' ',' ',' ']
list1=[1,2,3]
list2=[1,4,7]
flag=0
count=1

def print_board():

    print('        |         |         ')
    print('   {}    |    {}    |    {}   '.format(test_board[1],test_board[2],test_board[3]))
    print('        |         |         ')
    print('----------------------------')
    print('        |         |         ')
    print('   {}    |    {}    |    {}   '.format(test_board[4],test_board[5],test_board[6]))
    print('        |         |         ')
    print('----------------------------')
    print('        |         |         ')
    print('   {}    |    {}    |    {}   '.format(test_board[7],test_board[8],test_board[9]))
    print('        |         |         ')
def player_input_marker():
    p1_c=input('Player 1: X or O?')
    while p1_c not in 'XO':
        p1_c=input('Player 1: X or O?')
    return p1_c
def place_marker(p_c,posn_c1):
    test_board[posn_c1]=p_c
def check_if_occupied(posn_c2):
    if(test_board[posn_c2] in 'XO'):
        return True
    else:
        return False
def check_if_win():
    for x in list1:
        if(test_board[x]==test_board[x+3]==test_board[x+6] in 'XO'):
            return True
    for x in list2:
        if(test_board[x]==test_board[x+1]==test_board[x+2] in 'XO'):
            return True
    if(test_board[1]==test_board[5]==test_board[9] in 'XO'):
        return True
    elif(test_board[3]==test_board[5]==test_board[7] in 'XO'):
        return True
    return False
print_board()
p1=player_input_marker()
if(p1=='X'):
    p2='O'
else:
    p2='X'
while(count<=9 and flag==0):
        posn=int(input('Choose position'))
        while(check_if_occupied(posn)):
            posn=int(input('Choose position'))
        if count%2==1:
            place_marker(p1,posn)
        else:
            place_marker(p2,posn)
        print_board()
        if(check_if_win()):
            if count%2==1:
                print('Congratulations Player 1 won!')
            else:
                print('Congratulations Player 2 won!')
            flag=1
        count+=1
