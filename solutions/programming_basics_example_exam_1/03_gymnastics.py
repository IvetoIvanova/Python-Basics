country = input()
apparatus = input()

difficulty = 0
execution = 0

if country == "Russia":
    if apparatus == "ribbon":
        difficulty = 9.100
        execution = 9.400
    elif apparatus == "hoop":
        difficulty = 9.300
        execution = 9.800
    elif apparatus == "rope":
        difficulty = 9.600
        execution = 9.000

elif country == "Bulgaria":
    if apparatus == "ribbon":
        difficulty = 9.600
        execution = 9.400
    elif apparatus == "hoop":
        difficulty = 9.550
        execution = 9.750
    elif apparatus == "rope":
        difficulty = 9.500
        execution = 9.400

elif country == "Italy":
    if apparatus == "ribbon":
        difficulty = 9.200
        execution = 9.500
    elif apparatus == "hoop":
        difficulty = 9.450
        execution = 9.350
    elif apparatus == "rope":
        difficulty = 9.700
        execution = 9.150

total_score = difficulty + execution
missing_percentage = ((20 - total_score) / 20) * 100

print(f"The team of {country} get {total_score:.3f} on {apparatus}.")
print(f"{missing_percentage:.2f}%")
