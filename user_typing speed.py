from string import ascii_letters
import time
import random 

print("--------Welcome---------")

def user(): 
    while True:
        first_name = input("Enter your first_name: ")
        if first_name == "":
            print("invalid name"  )
            continue
        elif first_name.isalpha():
            break
        else:
            print("name must not contain numeric values")

    while True:
        last_name = input("Enter your last_name: ")
        if last_name == "":
            print("invalid name"  )
            continue
        elif last_name.isalpha():
            break
        else:
            print("name must not contain numeric values")

    while True:
        try:
            lenght = int(input("Enter number of characters: "))
            if lenght < 5 or lenght > 15:
                print("Number must be between 5 and 15 ")
            else:
                break
        except ValueError:
            print("Enter a valid number")
            
            
    random_chars = ''.join(random.choices(ascii_letters, k=lenght))
    print("Type in the following characters")
    print(random_chars)

    start_time = time.time()
    user_input = input("Type in the characters: ")
    end_time = time.time()

    time_taken = end_time - start_time

    score = 0

    for i in range(len(random_chars)):
        if i < len(user_input):
            if user_input[i] == random_chars[i]:
                score += 1
                
                

    print("------------------Results---------------")
    print(f"Name: {first_name} {last_name} ")
    print(F"Time taken: {time_taken:.2f} seconds")
    print(f"Charaters entered correctly; {score}")
    print("------------------------------------------")
                
                

user()