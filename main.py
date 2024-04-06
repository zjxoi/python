def greeting() -> int:
    name = input("What is your first name? ")
    lastname = input("What is your last name? ")

    while (True):
        try:
            age = int(input("How old are you? "))
            print("Hello", name, lastname, "of", age, "years of age!")
            break
        except ValueError:
            print("ERROR! Type your age in numbers")
    
    return age

def death_calculator(age:int):
    knowmore = input("Want to know something else? (Y/N) ")
    knowmore_lower = knowmore.lower()
    age_max = 100
    age_final = age_max - age

    if knowmore_lower == "y":
        print("You have", age_final, "years till death!")
    else:
        print("Wisdom is bliss.")

if __name__ == "__main__":
    age = greeting()
    death_calculator(age)