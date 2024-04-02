import random
def game():
    name=input("enter your name please! \n")
    x=5
    geussUser=0
    while geussUser<x:
          geussUser+=1
          options=["stone","paper","scissors"]
          print("s:stone","p:paper","s:scissors")
          user_choice=input("what is your first choice? \n")
          pc_choice=random.choice(options)
          print(pc_choice)

          if user_choice=="paper" and pc_choice=="scissors":
               print("PC is wins!")
         
          elif user_choice=="paper" and pc_choice=="stone":
               print(f"{name} is wins!")

          elif user_choice=="paper" and pc_choice=="paper":
                print("It's a tie!")

          elif user_choice=="scissors" and pc_choice=="paper":
                print(f"{name} is wins!")
          

          elif user_choice=="scissors" and pc_choice=="stone":
            print("PC is wins!")
           

          elif user_choice=="scissors" and pc_choice=="scissors":
               print("It's a tie!")

          elif user_choice=="stone" and pc_choice=="paper":
            print("PC is wins!")
            

          elif user_choice=="stone" and pc_choice=="scissors":
                print(f"{name} is wins!")
     

          elif user_choice=="stone" and pc_choice=="stone":
                print("It's a tie!")

          else:
               print("sorry! this is not possible")
    if x==geussUser:
          print("you're loser!!")

game()
    
