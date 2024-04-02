import random
import time
def question_generator():
    a=random.randint(1,9)
    b=random.randint(1,9)
    x=["-","+","*"]
    x_choice=random.choice(x)
    question=print(f"{a} {x_choice} {b} = ?")
    if x_choice=="+":
        return a+b
    elif x_choice=="-":
         return a-b        
    else:
         return a*b
        
question_numberLimit=5
question_number=0
score=0
time_limit=5

while question_number<question_numberLimit:
    result=str(question_generator())
    time_start=time.time()
    repons=input("enter your answer:")
    time_end=time.time()
    time_dif=time_end-time_start
    if time_dif<time_limit:
            if result==repons:
                print("perfect it was correct")
                question_number+=1
                score+=1
            else:
                print(f"not correct! repons is {result}")
                question_number+=1
    else:
         print("is too late your time is over!")
            
if question_number==question_numberLimit:
    print(f"Game is over! your score is:{score} out off {question_numberLimit}")   
   

