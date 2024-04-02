import random
names=["nick","junny","eliza","aran"]

selected_name=random.choice(names)

geuss_count=len(selected_name)
geussted_list=["-"]*len(selected_name)
while geuss_count>0:
    geuss=input("entre the char that you choicied:\n")
    if geuss.isalpha():
        if geuss in selected_name:
            if geuss in geussted_list:
                print("you havee geussted this char before, try a new charecter")
            else:
                for indx,char in enumerate(selected_name):
                    if char==geuss:
                         geussted_list[indx]=geuss
                current_guess=" ".join(geussted_list)
                print(f"perfect => {current_guess}")
                  
                if not "-" in geussted_list:
                    print("you won!")
                    break
        else:
            geuss_count-=1 
            print(f"wrong! => remaind geusses {geuss_count}")  
    else:
        print("please enter a valid character!")