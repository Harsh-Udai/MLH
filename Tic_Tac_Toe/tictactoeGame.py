# This is the simple implementation of the Tic Tac Toe game.
# Proper instructions will be given, when running this python script.
# written by: Harsh Udai.
class Tic_Tac:
    
    def __init__(self):
        self.board=[['-','-','-'],
                    ['-','-','-'],
                    ['-','-','-']]
        self.check=0
        self.dic={1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2]}
        
    def Board(self):
        for i in self.board:
            print(i)
        return "See!!"
    
    def possible_states(self):
        print("possible states")
        master=[]
        l=[]
        for i in self.board:
            l.append(i)
            
        for i,j in enumerate(l):
            for f in range(0,len(j)):
                if(j[f]=='-'):
                    master.append([i,f])
                    
        for i in range(len(master)-1):
            print(master[i],master[i+1])
            te1,te2=master[i]
            ye1,ye2=master[i+1]
            l[te1][te2]='X'
            l[ye1][ye2]='O'
            print('----------------------')
            for i in l:
                print(i)
            print('----------------------')
            
            l[te1][te2]='O'
            l[ye1][ye2]='X'
            for i in l:
                print(i)
            print("-----------------------")
            l[te1][te2]='-'
            l[ye1][ye2]='-'
        print("-------------------------")
            
    def win_check(self):
        
        a,b,c=self.dic[1],self.dic[5],self.dic[9]
        a1,b1,c1=self.dic[3],self.dic[5],self.dic[7]
        a2,b2,c2=self.dic[1],self.dic[4],self.dic[7]
        a3,b3,c3=self.dic[2],self.dic[5],self.dic[8]
        a4,b4,c4=self.dic[3],self.dic[6],self.dic[9]
        a5,b5,c5=self.dic[1],self.dic[2],self.dic[3]
        a6,b6,c6=self.dic[4],self.dic[5],self.dic[6]
        a7,b7,c7=self.dic[7],self.dic[8],self.dic[9]
        xx=self.board[a[0]][a[1]] # diagonal 1
        yy=self.board[b[0]][b[1]] # diagonal 5
        zz=self.board[c[0]][c[1]] # diagonal 9
        xx1=self.board[a1[0]][a1[1]] # diagonal 3
        yy1=self.board[b1[0]][b1[1]] # diagonal 5
        zz1=self.board[c1[0]][c1[1]] # diagonal 7
        xx2=self.board[a2[0]][a2[1]] # Straight 1
        yy2=self.board[b2[0]][b2[1]] # Straight 4
        zz2=self.board[c2[0]][c2[1]] # Straight 7
        xx3=self.board[a3[0]][a3[1]] # Straight 2
        yy3=self.board[b3[0]][b3[1]] # Straight 5
        zz3=self.board[c3[0]][c3[1]] # Straight 8
        xx4=self.board[a4[0]][a4[1]] # Straight 3
        yy4=self.board[b4[0]][b4[1]] # Straight 6
        zz4=self.board[c4[0]][c4[1]] # Straight 9
        xx5=self.board[a5[0]][a5[1]] # Straight 1
        yy5=self.board[b5[0]][b5[1]] # Straight 2
        zz5=self.board[c5[0]][c5[1]] # Straight 3
        xx6=self.board[a6[0]][a6[1]] # Straight 4
        yy6=self.board[b6[0]][b6[1]] # Straight 5
        zz6=self.board[c6[0]][c6[1]] # Straight 6
        xx7=self.board[a7[0]][a7[1]] # Straight 7
        yy7=self.board[b7[0]][b7[1]] # Straight 8
        zz7=self.board[c7[0]][c7[1]] # Straight 9
        if(xx==yy==zz and ((xx=='X' and yy=='X' or zz=='O')or (xx=='O' and yy=='O' and zz=='O'))):
            return(True,xx)
        elif(xx1==yy1==zz1 and ((xx1=='X' and yy1=='X' or zz1=='O')or (xx1=='O' and yy1=='O' and zz1=='O'))):
            return(True,xx1)
        elif(xx2==yy2==zz2 and ((xx2=='X' and yy2=='X' or zz2=='O')or (xx2=='O' and yy2=='O' and zz2=='O'))):
            return(True,xx2)
        elif(xx3==yy3==zz3 and ((xx3=='X' and yy3=='X' or zz3=='O')or (xx3=='O' and yy3=='O' and zz3=='O'))):
            return(True,xx3)
        elif(xx4==yy4==zz4 and ((xx4=='X' and yy4=='X' or zz4=='O')or (xx4=='O' and yy4=='O' and zz4=='O'))):
            return(True,xx4)
        elif(xx5==yy5==zz5 and ((xx5=='X' and yy5=='X' or zz5=='O')or (xx5=='O' and yy5=='O' and zz5=='O'))):
            return(True,xx5)
        elif(xx6==yy6==zz6 and ((xx6=='X' and yy6=='X' or zz6=='O')or (xx6=='O' and yy6=='O' and zz6=='O'))):
            return(True,xx6)
        elif(xx7==yy7==zz7 and ((xx7=='X' and yy7=='X' or zz7=='O')or (xx7=='O' and yy7=='O' and zz7=='O'))):
            return(True,xx7)
        else:
            return(False,0)
            
    def game_over(self,l):
        if 0 not in l:
            return True
        else:
            return False
        
    def X(self,l):
        c=0
        c1=0
        for i in range(0,len(l)):
            for j in range(0,len(i)):
                if(l[i][j]=='X'):
                    c+=1
                if(l[i][j]=='O'):
                    c1+=1
        if(c==c1):
            return "Draw"
        elif(c>c1):
            return "X"
        else:
            return 'O'
        
        
    def insert(self,x,y):
        print("-----------------------------")
        f_a,f_b=self.dic[x]
        g_a,g_b=self.dic[y]
        self.board[f_a][f_b]='X'
        self.board[g_a][g_b]='O'

    def play(self):
        print("Welcome to the Game")
        print("Player 1 is assigned with X")
        print("Player 2 is assigned with O")
        print("Okay, Initially the game will look like this")
        self.Board()
        while(True):
            if(self.check>8):
                print("Game Over")
                break
            player_1=int(input("Enter the position where you want to apply the X, Type: 1,2,3,4,5,6,7,8,9: "))
            self.check+=1
            if(self.check>8):
                print("Game Over")
                break
            if(self.win_check()[0]):
                print(self.win_check()[1],"is the winner")
                break
            player_2=int(input("Enter the position where you want to apply the X, Type: 1,2,3,4,5,6,7,8,9: "))
            self.check+=1
            self.insert(player_1,player_2)
            print(self.Board())
            
            if(self.win_check()[0]):
                print(self.win_check()[1],"is the winner")
                break
            print("-----------------------------")
            if(self.check>8):
                print("Game Over")
                break
            

if __name__ == "__main__":
    game=Tic_Tac()
    game.play()
        