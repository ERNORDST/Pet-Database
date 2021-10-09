#A program by Eric Nordstrom 10/3/2021

"""This program will create a database that the user can use to keep track off their pets. 
The use will be prompted to enter information about a series of attributes related
to their pets."""

pets = {}
pet_attributes = {}
attributes = ["Breed", "Color", "Sex", "Age", "DOB"]

print("Welcome to the Pet Info Database.")
returnmain_menu()
print("Thanks for using the pet database. Come back soon.")
#Haven't fleshed out this menu yet but this will be the first user input menu that lets them choose what part of
#the program they want to run

'''Have every part\function asking to quit to main menu they will be able to quit thte program and '''

def main_menu():
    ok = False
    while not ok:
        response = input("Press 1 to enter new pet. Press 2 to update database. Press 3 to search for information. Press 4 to quit. ")
        if response == "1":
            return new_pet()
        elif response == "2":
            return database_update()
        elif response == "3":
            return database_search()
        elif response=="4":
            break
        print("You have choosen to quit. Good-bye.")

def new_pet():
    ok = False
    while not ok:
        print("You have choosen to update the database.")
        prompt = "Press 1 to continue or Press 0 to quit. "
        response_prompt = input(prompt)
        if response_prompt in ("1", "0"):
            ok = True
        else: 
            print(response_prompt, "is not a valid response")
        if response_prompt == "1":
            print("You chose to continue.")
            ok = False 
            while not ok:
                pet_name = input("What is your pets name? ").upper()
                print("Your pets name is", pet_name)
                pet_breed = input("Please enter your pets breed. ").upper()
                print("Your pets breed is", pet_breed)
                pet_color = input("Please enter the color of your pet. ").upper()
                print("The color of you pet is", pet_color)
                pet_sex = input("Please enter the sex of your pet. Use m for male or f for female. ").upper()
                if pet_sex == "M":
                    print("Your pet is Male.")
                elif pet_sex == "F":
                    print("Your pet is Female.")
                pet_age = input("Please enter your pets age. ")
                print("Your pet is", pet_age, "years old.")
                pet_dob = input("Please enter your pets date of birth. Use month/day/year ")
                print("Your pets DOB is", pet_dob)
                pets.update({pet_name: {"Breed": pet_breed, "Color": pet_color, \
                     "Sex": pet_sex, "Age": pet_age, "DOB": pet_dob}}) 
                print(pets)
                response_return = input("Press 0 to return to start or any other key to continue. ")
                if response_return == "0":
                    break
        else:
            print("You chose to quit.")
            print("Bye.")
            break

def database_update():
    pet_to_update = pet_name
    pet_name = input("Enter the name of the pet whose information you wish to update. ")
    ok = False
    while not ok:
        info_to_update = input("Press 1 to update pets breed. Press 2 to update the color of the pet. Press 3 to update the sex of your pet. Press 4 to update your pets age. Press 5 to update your pets dob. Press 6 to quit. ")
        if info_to_update == "1":
           new_breed = input("Enter the pets breed. ")
           pets.update({pet_name: {"Breed" : new_breed}})
        elif info_to_update == "2":
            new_color = input("Enter the pets color. ")
            pets.update({pet_name: {"Color": new_color}})
        elif info_to_update == "3":
            new_sex = input("Enter the sex of your pet. ")
            pets.update({pet_name: {"Sex": new_sex}})
        elif info_to_update == "4":
            new_age = input("Enter your pets age. ")
            pets.update({pet_name: {"Age": new_age}})
        elif info_to_update == "5":
            new_dob = input("Enter the pets dob. Use month/day/year. ")
            pets.update({pet_name: {"DOB": new_dob}})
        elif info_to_update == "6":
            break

def database_search():
    pet_to_search = input("Enter the name of the pet you wish to search for. ")
    pet_name = pet_to_search
    info_to_search = input("Press 1 to find the pets breed. Press 2 to find the pets color. Press 3 to find the pets sex. Press 4 to find pets age. Press 5 to find pets dob. Press 6 to quit. ")
    ok = False
    while not ok:
        if info_to_search == "1":
            return 
        elif info_to_search == "2":
            return
        elif info_to_search == "3":
            return
        elif info_to_search == "4":
            return
        elif info_to_search == "5":
            return
        elif info_to_search == "6":
            break

