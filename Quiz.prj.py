import random
def read_file(file_path):
    currencies={}
    with open(file_path,"r") as file:
        for line in file:
            try:
                symbol,name=line.strip().split(":")
                currencies[symbol]=name
            except ValueError:
                print(f"Invalid line in file:{line.strip()}")
    return currencies

def ask_questions(currencies,num_questions):
    correct_answers=0

    for _ in range(num_questions):
        symbol,correct_name=random.choice(list(currencies.items()))
        options=[correct_name]

        while len(options)<4:
            random_currency=random.choice(list(currencies.values()))
            if random_currency not in options:
                options.append(random_currency)
        random.shuffle(options)
        print(f"what is the currency of the '{symbol}'?")
        for i, option in enumerate(options,1):
            print(f"{i}.{option}")
        user_answer=int(input("Enter the number of your choice:").strip())-1
        if options[user_answer]==correct_name:
            print("CORRECT\n")
            correct_answers+=1
        else:
            print(f"WRONG! the correct answer is:{correct_name}\n")
    return correct_answers
if __name__ == "__main__":
        file_path="currencies.txt"
        currencies=read_file(file_path)
        num_questions=int(input("Enter the number of questions you want to answer:"))
        correct_answers=ask_questions(currencies,num_questions)
        accuracy=(correct_answers/ num_questions)*100
        print(f"\n you answerd {correct_answers} out of {num_questions} questions correctly.")
        print(f"Accuracy:{accuracy:.2f}%")


ask_questions(currencies, num_questions)










