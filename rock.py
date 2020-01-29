rock=1
paper=2
scissor=3
s=int(input("enter a number"))
import random
t=random.randrange(1,3)
print(t)
if(s==rock and t==1):
    print("Its s draw")
elif(s==rock and t==2):
    print("paper wins")
elif(s==rock and t==3):
    print("rock wins")
elif(s==paper and t==1):
    print("paper wins")
elif(s==paper and t==2):
    print("Its a draw")
elif(s==paper and t==3):
    print("Scissor wins")
elif(s==scissor and t==1):
    print("rock wins")
elif(s==scissor and t==2):
    print("scissor wins")
elif(s==scissor and t==3):
    print("Its a draw")
     
