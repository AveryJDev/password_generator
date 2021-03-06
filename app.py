import random
from itertools import chain
import csv

#Testing github!

upper_str = ("ABCDEFGHIJKLMNOPQRSTUVWYXZ")
lower_str = ("abcdefghijklmnopqrstuvwxyz")
number_str = ("0123456789")
special_str = ("!$%^&*()_+[]:;@'~#<>,.?/")

class Generator:

    def __init__(self, upper_amt, lower_amt, number_amt, special_amt):
        self.upper_amt = upper_amt
        self.lower_amt = lower_amt
        self.number_amt = number_amt
        self.special_amt = special_amt

    def create(self):
        passwd_list = []
        required_amts = {upper_str: self.upper_amt, lower_str: self.lower_amt, number_str: self.number_amt, special_str: self.special_amt}
        for key_string, value_amount in required_amts.items():
            for i in range(0, value_amount):
                passwd_list.append(key_string[random.randint(0,len(key_string)-1)])
        final_list = list(chain(*passwd_list))
        random.shuffle(final_list)
        final_password = "".join(final_list)
        return final_password

def gen_logic(amount):
    count = 0
    while amount % 4 != 0:
        count += 1
        amount += 1

    pass_split = amount // 4    
    if count == 3:
        a = 2
        b = 1
    elif count == 2:
        a = 1
        b = 1
    elif count == 1:
        a = 1
        b = 0
    else:
        a = 0
        b = 0
    complete = Generator(pass_split, pass_split, pass_split-b, pass_split-a)
    return complete
        

def auto_gen():
    while True:
        try:
            passwd_len = int(input("\n\nEnter desired password length (Minimum 8 characters): "))
        except ValueError:
            print("\nPlease enter a number.")
            continue
        if passwd_len < 8:
            print("\nPlease enter minimum 8 characters.")
            continue
        else:
            completed = gen_logic(passwd_len)
        print("\nYour password is: ", completed.create())
        break
    quit()


def man_gen():
    print("\nPlease enter your desired amount for the following (Minimum 8 in total): ")
    while True:
        try:
            input_length = 0
            print("\n Current Length = ", input_length)
            upper_chars = int(input(" UPPER CASE Characters: "))
            input_length += upper_chars

            print("\n Current Length = ", input_length)
            lower_chars = int(input(" lower case Characters: "))
            input_length += lower_chars
            
            print("\n Current Length = ", input_length)
            number_chars = int(input(" Numbers: "))
            input_length += number_chars
            
            print("\n Current Length = ", input_length)
            special_chars = int(input(" Special Characters: "))
            input_length += special_chars
        except ValueError:
            print("\nNumbers only, please.")
            continue
        if input_length < 8:
            print("You must enter at least 8 Characters!")
            continue
        else:
            complete = Generator(upper_chars, lower_chars, number_chars, special_chars)
            print("\nTotal Password Length = ", input_length)
            print("Your password is: ", complete.create())
            quit()  

def bulk_gen():
    print("\nPlease enter the following values to generate a .txt file.")
    while True:
        try:
            bulk_amt = int(input("\n Amount of passwords required: "))   
            range_choice = int(input("\n 1. Input password length\n 2. Mixed length within secure range (12 - 20)\n >>> ")) 
            if range_choice >= 3:
                print(" Please select 1 or 2")
                continue
            else:
                if range_choice == 1:
                    passwd_len = int(input("Enter length for passwords: "))    
            file_name = input("\n File name to save output: ")
        except ValueError:
            print(" Please enter values in the requested format")
            continue

        with open (file_name, "w") as file:
            writer = csv.writer(file)
            for i in range(bulk_amt):
                if range_choice == 2:
                    passwd_len = random.randint(12, 20)
                completed = gen_logic(passwd_len)
                file.write(completed.create())
                file.write("\n")
            print(" Complete.")
            quit()

        
def user_input():
    print("Random Password Generator. Please select auto-gen, or manual")
    while True: 
        try:
            a_m_b = int(input("\n 1. Automatic Generation - Only length required\n 2. Manual Generation - Specify individual char amounts\n 3. Bulk password creation - exported to .txt file\n\n>>> "))
        except ValueError:
            print("\nIntegers only. Try again.")
            continue
        if a_m_b == 1:
            auto_gen()
            break
        elif a_m_b == 2:
            man_gen()
            break
        elif a_m_b == 3:
            bulk_gen()
        else:
            print("\nPlease select 1, 2, or 3")
            continue



user_input()




