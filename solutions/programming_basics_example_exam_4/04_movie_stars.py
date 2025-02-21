budget = float(input())

while True:
    data = input()

    if data == 'ACTION':
        break

    if len(data) > 15:
        budget -= budget * 0.20
        continue
    else:
        payment = float(input())

        if budget < payment:
            budget -= payment
            break

        budget -= payment

if budget >= 0:
    print(f'We are left with {budget:.2f} leva.')
else:
    print(f'We need {abs(budget):.2f} leva for our actors.')
