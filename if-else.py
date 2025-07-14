# Simple calculator, learning with if-else statements

print("""
    Welcome to our simple math calculator!!!
    Choose your options:
    1. multiplication
    2. subtraction
    3. division
    4. addition
    5. exit calculator
      """)
loop_decider = True

while loop_decider:

    answer_1 = input("What you want: ")

    if answer_1 == "1":
        print("ok, you have selected multiplication")
        num1 = input("first number: ")
        num2 = input("now enter your 2nd number: ")

        num1 = int(num1)
        num2 = int(num2)

        final_answer = num1 * num2

        print("your answer is: ", final_answer)
    elif answer_1 == "2":
        print("ok, you have selected subtraction")
        num1 = input("first number: ")
        num2 = input("now enter your 2nd number: ")

        num1 = int(num1)
        num2 = int(num2)

        final_answer = num1 - num2

        print("your answer is: ", final_answer)
    elif answer_1 == "3":
        print("ok, you have selected division")
        num1 = input("first number: ")
        num2 = input("now enter your 2nd number: ")

        num1 = int(num1)
        num2 = int(num2)

        final_answer = num1 / num2

        print("your answer is: ", final_answer)
    elif answer_1 == "4":
        print("ok, you have selected addition")
        num1 = input("first number: ")
        num2 = input("now enter your 2nd number: ")

        num1 = int(num1)
        num2 = int(num2)

        final_answer = num1 + num2

        print("your answer is: ", final_answer)
    elif answer_1 == "5":
        print("Thanks for using our calculator!")
        loop_decider = False
    else:
        print ("sorry, that input isnt an option")