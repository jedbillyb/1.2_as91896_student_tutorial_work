import math

## rounding practice

# eggs = int(57)
# cases = math.ceil(eggs / 12)
# print(f"We need {cases} cases for {eggs} eggs")


# fudge = int(12400)
# bag = math.floor(fudge / 500)
# print(f"Sally will need {bag} bag(s) ")

# bag_weight = round(fudge / bag)
# print(f"Each bag will weigh {bag_weight} grams")


# jason_weight = 55
# rounded_jason_weight = round(jason_weight)
# print(f"If you round Jasons weight you get {rounded_jason_weight}Kg")


# cat_or_dog = input("Do you own a cat or a dog? ")
# animal_input_question = "What is the name of your " + cat_or_dog + " "
# animal_name = input(animal_input_question)
# print("The name of your", cat_or_dog, "is", animal_name)

# cat_or_dog = input("Do you own a cat or a dog? ")
# animal_input_question = "What is the name of your ", cat_or_dog, " "
# animal_name = input(animal_input_question)
# print("The name of your" + cat_or_dog + "is" + animal_name)



# number_one = int(input("Choose a number for number one: "))
# number_two = int(input("Choose a number for number two: "))
# number_combined = number_one + number_two
# print(f"{number_one} + {number_two} = {number_combined}")



# name = input("What is your name? ")
# country = input("What country were your born in? ")
# hemisphere = input(f"Is {country} in the northern or southern hemisphere? ")
# print(f"{name} is from {country} which is in the {hemisphere} hemisphere")



# name = input("What is your name? ")
# print(f"Hi {name}")



# jed_favourite_colour = "blue"
# favourite_colour_input = input("What is your favourite colour? ")
# print(f"Your favourite colour is {favourite_colour_input} and my favourite is {jed_favourite_colour}!")



name_input = input("What is your name? ")
food_input = input("What is favourite food? ")
vegetarian_input = input(f"Is {food_input} vegetarian? ").title
country_input = input("What country were your born in? ")
hemisphere_input = input(f"Is {country_input} in the northern or southern hemisphere? ")

if vegetarian_input in ["Yes", "Y"]:
    vegetarian_yes_no = ""
else:
    vegetarian_yes_no = "not "

print(vegetarian_yes_no)
print(f"{name_input} favourite food is {food_input} which is {vegetarian_yes_no}vegatarian, {name_input} is from {country_input} which is in the {hemisphere_input} hemisphere")