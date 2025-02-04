number_of_visitors = int(input())

training_back_counter = 0
training_chest_counter = 0
training_legs_counter = 0
training_abs_counter = 0
protein_shake_counter = 0
protein_bar_counter = 0

for _ in range(number_of_visitors):
    data = input()

    if data == 'Back':
        training_back_counter += 1
    elif data == 'Chest':
        training_chest_counter += 1
    elif data == 'Legs':
        training_legs_counter += 1
    elif data == 'Abs':
        training_abs_counter += 1
    elif data == 'Protein shake':
        protein_shake_counter += 1
    elif data == 'Protein bar':
        protein_bar_counter += 1

percent_of_working_out_people = ((training_back_counter
                                  + training_legs_counter
                                  + training_chest_counter
                                  + training_abs_counter)
                                 / number_of_visitors
                                 * 100)
percent_of_people_bought_protein = (protein_shake_counter + protein_bar_counter) / number_of_visitors * 100

print(f'{training_back_counter} - back')
print(f'{training_chest_counter} - chest')
print(f'{training_legs_counter} - legs')
print(f'{training_abs_counter} - abs')
print(f'{protein_shake_counter} - protein shake')
print(f'{protein_bar_counter} - protein bar')
print(f'{percent_of_working_out_people:.2f}% - work out')
print(f'{percent_of_people_bought_protein:.2f}% - protein')
