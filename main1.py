name = input("ENTER NAME OF THE CANDIDATE\n")
designation = input("ENTER DESIGNATION\n")
experience = input("ENTER YEARS\n")
nextRole = input("ENTER NEXT ROLE")


def check_inputs():
    if name.isalpha() and designation.isalpha() and experience.isdigit():
        show_msg()
    else:
        print("enter proper values")


def show_msg():
    print(f"{name} is a {designation}. He has {experience} of experience in IT industry. He will be promoted to {nextRole} next year")


check_inputs()