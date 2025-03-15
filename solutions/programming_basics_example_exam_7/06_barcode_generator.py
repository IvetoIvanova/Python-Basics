first_number = input()
second_number = input()

n1, n2, n3, n4 = first_number
x1, x2, x3, x4 = second_number

for num1 in range(int(first_number[0]), int(second_number[0]) + 1):
    for num2 in range(int(first_number[1]), int(second_number[1]) + 1):
        for num3 in range(int(first_number[2]), int(second_number[2]) + 1):
            for num4 in range(int(first_number[3]), int(second_number[3]) + 1):
                if num1 % 2 != 0 and num2 % 2 != 0 and num3 % 2 != 0 and num4 % 2 != 0:
                    print(f'{num1}{num2}{num3}{num4}', end=' ')
