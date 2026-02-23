## number of guests
# number_of_guests = 85

## What the guests need following the reception
# chair_needed = 1 * number_of_guests
# dinner_plate_needed = 1 * number_of_guests
# side_plate_needed = 1 * number_of_guests
# knife_needed = 1 * number_of_guests
# fork_needed = 1 * number_of_guests
# bowls_needed = 2 * number_of_guests
# servietts_needed = 2 * number_of_guests
# spoons_needed = 2 * number_of_guests
# wine_glasses_needed = 2 * number_of_guests
# drink_glases_nedded = 3 * number_of_guests

## formula to calculate how many marques we need
# marque_needed = number_of_guests / 20

## print line that prints what we need in a nice formated way
# print(f"There are {number_of_guests} guests coming, we will need {chair_needed} chairs, {dinner_plate_needed} dinner plates, {side_plate_needed} side plates, {knife_needed} knifes, {fork_needed}, forks, {bowls_needed} bowls, {servietts_needed} servietts, {spoons_needed} spoons, {wine_glasses_needed} wine glasses, {drink_glases_nedded} drink glasses, and {marque_needed} marque(s).")



## number of guests
# number_of_guests = 85

## What the guests needfollowing reception
# chair_needed = 1 * number_of_guests
# dinner_plate_needed = 1 * number_of_guests
# side_plate_needed = 1 * number_of_guests
# knife_needed = 1 * number_of_guests
# fork_needed = 1 * number_of_guests
# bowls_needed = 2 * number_of_guests
# servietts_needed = 2 * number_of_guests
# spoons_needed = 2 * number_of_guests
# wine_glasses_needed = 2 * number_of_guests
# drink_glases_nedded = 3 * number_of_guests

## formula to calculate how many marques we need
# marque_needed = round(number_of_guests / 20)

## print line that prints what we need in a nice formated way
# print(f"There are {number_of_guests} guests coming, we will need {chair_needed} chairs, {dinner_plate_needed} dinner plates, {side_plate_needed} side plates, {knife_needed} knifes, {fork_needed}, forks, {bowls_needed} bowls, {servietts_needed} servietts, {spoons_needed} spoons, {wine_glasses_needed} wine glasses, {drink_glases_nedded} drink glasses, and {marque_needed} marque(s).")



import math
# number of guests
number_of_guests = 85

## What the guests needfollowing reception
chair_needed = 1 * number_of_guests
dinner_plate_needed = 1 * number_of_guests
side_plate_needed = 1 * number_of_guests
knife_needed = 1 * number_of_guests
fork_needed = 1 * number_of_guests
bowls_needed = 2 * number_of_guests
servietts_needed = 2 * number_of_guests
spoons_needed = 2 * number_of_guests
wine_glasses_needed = 2 * number_of_guests
drink_glases_nedded = 3 * number_of_guests

marque_needed = math.ceil(number_of_guests / 20)

print(f"There are {number_of_guests} guests coming, we will need {chair_needed} chairs, {dinner_plate_needed} dinner plates, {side_plate_needed} side plates, {knife_needed} knifes, {fork_needed}, forks, {bowls_needed} bowls, {servietts_needed} servietts, {spoons_needed} spoons, {wine_glasses_needed} wine glasses, {drink_glases_nedded} drink glasses, and {marque_needed} marque(s).")