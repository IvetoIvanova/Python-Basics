import math

number_of_cozonacs = int(input())

sugar_per_pack = 950
flour_per_pack = 750

total_sugar_used = 0
total_flour_used = 0
max_sugar_used = 0
max_flour_used = 0

for _ in range(number_of_cozonacs):
    sugar_used = int(input())
    flour_used = int(input())

    total_sugar_used += sugar_used
    total_flour_used += flour_used

    if sugar_used > max_sugar_used:
        max_sugar_used = sugar_used
    if flour_used > max_flour_used:
        max_flour_used = flour_used

sugar_packs_needed = math.ceil(total_sugar_used / sugar_per_pack)
flour_packs_needed = math.ceil(total_flour_used / flour_per_pack)

print(f"Sugar: {sugar_packs_needed}")
print(f"Flour: {flour_packs_needed}")
print(f"Max used flour is {max_flour_used} grams, max used sugar is {max_sugar_used} grams.")
