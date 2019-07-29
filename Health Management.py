# coding = utf-8

'''
create a program which will take inputs from the user to log or retrieve exercise or food intake by the client
have to use specified functions

'''
# print("Welcome to Health Management System \n")
# client_name = input("Enter the first name of your client \n")
# client_name = client_name.lower()
# action = input("Would you like to log the entry or retrive the entry? \n")
# action2 = input("Would you like to log exercise or food intake? \n")
# action3 = input("Please enter : \n")
# if client_name == "harry":
#     if action == "log" and action2 == "food intake":
#         health = open("Harry_food.txt", "a")
#         health.write(action3)
#         print(getdate(), end = "")
#         health.readline()
# b = ["Hammad_food.txt", "Rohan_food.txt", "Harry_food.txt"]
# f = open(b[0], "w")
# f.write("Alpha")

# client_list = ["Harry", "Rohan", "Hammad"]
# food_files = ["Harry_food.txt", "Hammad_food.txt", "Rohan_food.txt"]
# exercise_files = ["Harry_exercise.txt", "Hammad_exercise.txt", "Rohan_exercise.txt"]
# client  = input("Enter client's name : \n")
# action1 = input("Enter if you want to input'Exercise' or 'Food' : \n")
from typing import TextIO


def getdate():
    import datetime
    return datetime.datetime.now()
print("Welcome to Health Management System \n")
client_list = ["Harry", "Rohan", "Hammad"]
d1 = {"Harry" : "Harry_food.txt" , "Rohan" : "Rohan_food.txt" , "Hammad" : "Hammad_food.txt" }
d2 = {"Harry" : "Harry_exercise.txt" , "Rohan" : "Rohan_exercise.txt" , "Hammad" : "Hammad_exercise.txt" }
def name():
    client = input("Enter client's name : \n")
    client = client.lower()
    client = client.capitalize()
    if client in client_list:
        gg(client)
    else:
        print("Incorrect name! Try again!")
        name()

def gg(client):
    act = input("Enter if you want to 'log' or 'retrive' : \n")
    if act == "log":
        action1 = input("Enter if you want to input'Exercise' or 'Food' : \n")
        action1 = action1.lower()
        action1 = action1.capitalize()
        if action1 == "Food":
            print("You're now accessing ", client, "'s", "file and are now going to add the food he took.\n")
            e = input("Please enter the food intake : \n")
            with open(d1[client], "a") as d:
                d.write(str([str(getdate())]) + " : " + e + "\n")
        elif action1 == "Exercise":
            print("You're now accessing ", client, "'s", "file and are now going to add the exercise he did.\n")
            e = input("Please enter the exercise he did : \n")
            with open(d2[client], "a") as d:
                d.write(str([str(getdate())]) + " : " + e + "\n")
        else:
            print("Invalid Input! Try again!")
            gg(client)
        again(client)
    else:
        action1 = input("Enter if you want to retrive 'Exercise' or 'Food' : \n")
        if action1 == "Food" or action1 == "food":
            print("You're now accessing ", client, "'s", "file and are now going to check the food he took.\n")
            with open(d1[client]) as d:
                for i in d:
                    print(i)
                again(client)
        elif action1 == "Exercise" or action1 == "exercise":
            print("You're now accessing ", client, "'s", "file and are now going to check the food he took.\n")
            with open(d2[client]) as d:
                for i in d:
                    print(i)
                again(client)


def again(client):
    entry = input("\n Press N to go to next log entry or press R to retrive the data or press any key to exit \n")
    if entry == "N" or entry == "n":
        gg(client)
    elif entry == "R" or entry == "r":
        gg(client)
    else:
        exit()
        print("Bye!")
name()
again(client)




# def again():
#     entry = input("\n Press N to go to next log entry or press R to retrive the data or press e to exit \n")
#     if entry == "N":
#         gg()
#     elif entry == "R":
#         retrive()
#     else:
#         exit()
# again()