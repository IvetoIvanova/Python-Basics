number_of_groups = int(input())

musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for _ in range(number_of_groups):
    num_of_climbers = int(input())

    if num_of_climbers <= 5:
        musala += num_of_climbers
    elif num_of_climbers <= 12:
        monblan += num_of_climbers
    elif num_of_climbers <= 25:
        kilimandjaro += num_of_climbers
    elif num_of_climbers <= 40:
        k2 += num_of_climbers
    elif num_of_climbers >= 41:
        everest += num_of_climbers

total_climbers = musala + monblan + kilimandjaro + k2 + everest
percent_of_musala_climbers = (musala * 1.00 / total_climbers) * 100
percent_of_monblan_climbers = (monblan * 1.00 / total_climbers) * 100
percent_of_kilimandjaro_climbers = (kilimandjaro * 1.00 / total_climbers) * 100
percent_of_k2_climbers = (k2 * 1.00 / total_climbers) * 100
percent_of_everest_climbers = (everest * 1.00 / total_climbers) * 100

print(f'{percent_of_musala_climbers:.2f}%')
print(f'{percent_of_monblan_climbers:.2f}%')
print(f'{percent_of_kilimandjaro_climbers:.2f}%')
print(f'{percent_of_k2_climbers:.2f}%')
print(f'{percent_of_everest_climbers:.2f}%')
