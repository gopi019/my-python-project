name = input("ENTER NAME\n")
designation = input("ENTER DESIGNATION\n")
experience = input("ENTER YEARS\n")


def check_inputs():
    if name.isalpha() and designation.isalpha() and experience.isdigit():
        show_msg()
    else:
        print("enter proper values")


def show_msg():
    print(f"{name} is a {designation}. He has {experience} of experience in IT industry")


check_inputs()