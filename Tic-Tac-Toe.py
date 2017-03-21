
global Board,a,Score,steps,k,moveno  

moveno=0

Board=['0','0','0','0','0','0','0','0','0']  # The actual Game Board Situation

w, h = 2, 9

a= [[0 for x in range(w)] for y in range(h)] # DD list to Store the Score of Each move i.e a[0][0]-Score of 0th move...and a[0][1] is the total no of moves
print(0)
Score=steps=k=0 		  					 #initialization

											 #7506002060

def IsEmpty(b):						    	 # function to check if bth position is Empty or not 
	
	if ( not Board[b] == 'O') and ( not Board[b] == 'X'):
	
		return True
	
	else:
		
		return False

		
def IsFull():			 					  #function to check if the Board is full or not
	
	i=0
	
	while i<=8:
	
		if IsEmpty(i):
			
			return False
		
		i+=1
	
	return True		

def TicTacToe_Board():   					  # function to print the board 
	
	print("	._______._______._______.")
	
	i=0
	
	while i<9:
		
		if Board[i]=='0':
		
			print("	| ",end="")
		
		elif Board[i]=='X':
		
			print("	|   X",end="")
		
		elif Board[i]=='O':
			
			print("	|   O",end="")
		
		if i==2 or i==5:
			
			print("	|\n",end="")
			
			print("	|_______|_______|_______|")
		
		i+=1
	
	print("	|")
	
	print("	|_______|_______|_______|")
					
def IsWin(chr):			 # function to check if player with given chr('X' or 'O') has Won
	
	if (Board[0]==chr and Board[1]==chr and Board[2]==chr) or (Board[3]==chr and Board[4]==chr and Board[5]==chr) or (Board[6]==chr and Board[7]==chr and Board[8]==chr) or (Board[0]==chr and Board[3]==chr and Board[6]==chr) or (Board[1]==chr and Board[4]==Board[7]==chr) or (Board[2]==chr and Board[5]==chr and Board[8]==chr) or (Board[0]==chr and Board[4]==chr and Board[8]==chr) or (Board[2]==chr and Board[4]==chr and Board[6]==chr):  
		
		return True
	
	else:
		
		return False


def IsLost(chr):		 # function to check if player with given chr('X' or 'O') has lost
	
	if chr=='X':
		
		chr='O'
	
	elif chr=='O':
		
		chr='X'
	
	if IsWin(chr):
		
		return True
	
	else:
		
		return False


		
def IsDraw(chr):		 # function to check if the current Board situation is a draw
	
	if (not IsWin('X')) and (not IsLost('X')) and IsFull():
		
		return True
	
	else:
		
		return False
		
def CompMove(m=0,l=8):   # function to determine tentative move of the System
	
	global temp,Score,moveno,Board
	
	i=m
	
	while i<=l and (not IsFull()):
		
		if IsEmpty(i):
				
			Board[i]='X'
			
			moveno+=1
					
			if IsWin('X'):
			
				Board[i]='0'
				
				Score+=10
				
				return				   # once there is a win or loss or even draw further playing is useless as the system or the player will choose this move(if it gets this far)
			
			elif IsLost('X'):
				
				Board[i]='0'			
				
				Score-=10
				
				return
			
			elif IsDraw('X'):
				
				Board[i]='0'
				
				Score+=0
				
				return
			
			else:
				
				Player_TentativeMove()
				
				Board[i]='0'
						
		i+=1	
		
	
def Player_TentativeMove():		  # function to determine tentative player move once the system chooses a particular move
	
	global temp,Score,moveno,Board
	
	i=0
	
	while i<=8 and (not IsFull()):
			
		if IsEmpty(i):
				
			Board[i]='O'
				
			moveno+=1
						
			if IsLost('O'):
				
				Board[i]='0'
				
				Score+=10
				
				return
			
			elif IsWin('O'):
				
				Board[i]='0'
				
				Score-=10
				
				return
			
			elif IsDraw('O'):
				
				Board[i]='0'
				
				Score+=0
				
				return
			
			else:
				
				CompMove()
				
				Board[i]='0'
				
		i+=1
		
		
def MiniMax():

	k=l=s=i=j=0
	
	global a,moveno,Score
	
	moveno=Score=bestscore=bestmove=0
	
	
	for i in range(9):
		
		for j in range(2):
			
			a[i][j]=0			# initializing the DD list with value 0
	
	i=0
	for i in range(9):			    #checking if the player wins from one move at ith position. if true then the bestmove is i to prevent him/her from winning 
		
		if IsEmpty(i):
			
			Board[i]='X'
			
			if IsLost('O'):
				
				Board[i]='0'
				
				return	i
			
			Board[i]='0'
		
		i+=1
	i=0
	
	for i in range(9):			    #checking if the player wins from one move at ith position. if true then the bestmove is i to prevent him/her from winning 
		
		if IsEmpty(i):
			
			Board[i]='O'
			
			if IsLost('X'):
				
				Board[i]='0'
				
				return	i
			
			Board[i]='0'
		
		i+=1
	
		
	while k<=8:					# each k denotes the move that the System can play
		
		if IsEmpty(k):
			
			CompMove(k,l)		#first time the loop in CompMove() should run only one time and i in that should be the actual move the System can play
			
			a[k][0]=Score		# Storing Score for move at kth position	
				
			a[k][1]=moveno  	# Storing Score for move at kth position	
			
		else:
			
			a[k][0]="nil"		# if the Position i is not empty than the score is "nil" to avoid collision with any possible score eg if i keep it 0 then there is a chance that some move has actually score=0
		
		k+=1
		
		l+=1
			
		if moveno==1 and Score==10: 	#checking if there is a move in which the System wins just by a single move
			
			s=20
			
			break
		
		Score=moveno=0
			
	i=j=0
		
	for i in range(9):  		#giving bestscore a non "nil" value
			
		if not a[i][0]=="nil":
				
			bestscore=a[i][0]
				
			break
		
	if s==20:
	
		return k-1
	
	else:
		
		while i<=8:				#finding max possible score and its move 
			
			if (not a[i][0]=="nil") and bestscore<=a[i][0] :
				
					bestscore=a[i][0]
					
					j=i
		
			i+=1	
		
	bestmove=j
		
	print("Hmmmmm I choose Position ",bestmove)
		
	return bestmove

def Start():
	
	global steps,Board
	
	print("		WELCOME		\n")
	
	#while input("Do You Wish To Play Again??(0/1)"):
	
	c=input("	Do You Mind if I Start(Y/N)\n")
	
	print("		I am 'X' and you are 'O'\n")
	
	if c=='N':
		
		while 1:
			
			print("		I am Thinking.. . . . . . .")		
			
			move=MiniMax()
			
			Board[move]='X'
			
			steps+=1
			
			TicTacToe_Board()
			
			if IsWin('X'):
				
				print("		You Have Lost the Game")
				
				break
				
			elif IsDraw('X'):
				
				print("		Draw Game..")
				
				break
			
			elif IsLost('X'):
				
				print("		You Win!!")
				
				break
			
			else:
				
				while 1:
					
					move=int(input("		It's Your Turn----Enter your move(must be between 0 and 8)"))
					
					if move>=0 and move<9 and IsEmpty(move):
					
						steps+=1
						
						Board[move]='O'
						
						TicTacToe_Board()
						
						break
					
					else:
						
						print("		Please Enter a valid move")
						
						continue
				
				if IsWin('O'):
					
					print("		You WIN!!")
					
					break
			
				elif IsDraw('O'):
					
					print("		Draw Game..")
					
					break
			
				elif IsLost('O'):
					
					print("		You Have Lost the Game")
					
					break
				
				else:
					
					continue
	
	elif c=='Y':
		
		while 1:
				
				while 1:
					
					move=int(input("	It's Your Turn----Enter your move(must be between 0 and 8)"))
					
					if move>=0 and move<9 and IsEmpty(move):
					
						steps+=1
						
						Board[move]='O'
						
						TicTacToe_Board()
						
						break
					
					else:
						
						print("		Please Enter a valid move")
						
						continue
				
				if IsWin('O'):
					
					print("		You WIN!!")
					
					break
			
				elif IsDraw('O'):
					
					print("		Draw Game..")
					
					break
			
				elif IsLost('O'):
					
					print("		You Have Lost the Game")
					
					break
				
				else:
			
					print("		I am Thinking.. . . . . . .")
					
					move=MiniMax()
			
					Board[move]='X'
			
					steps+=1
			
					TicTacToe_Board()
			
					if IsWin('X'):
				
						print("		You Have Lost the Game")
				
						break
				
					elif IsDraw('X'):
				
						print("		Draw Game..")
				
						break
			
					elif IsLost('X'):
				
						print("		You Win!!")
				
						break
			
			
					
Start()		
		