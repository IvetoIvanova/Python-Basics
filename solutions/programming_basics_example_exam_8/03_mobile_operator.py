contract_term = input()
type_of_contract = input()
mobile_internet_added = input()
number_of_months_to_pay = int(input())

fee_for_one_month = 0.0
contract_term_two_years = False

if contract_term == 'one':
    if type_of_contract == 'Small':
        fee_for_one_month = 9.98
    elif type_of_contract == 'Middle':
        fee_for_one_month = 18.99
    elif type_of_contract == 'Large':
        fee_for_one_month = 25.98
    elif type_of_contract == 'ExtraLarge':
        fee_for_one_month = 35.99
elif contract_term == 'two':
    contract_term_two_years = True
    if type_of_contract == 'Small':
        fee_for_one_month = 8.58
    elif type_of_contract == 'Middle':
        fee_for_one_month = 17.09
    elif type_of_contract == 'Large':
        fee_for_one_month = 23.59
    elif type_of_contract == 'ExtraLarge':
        fee_for_one_month = 31.79

if mobile_internet_added == 'yes':
    if fee_for_one_month <= 10:
        fee_for_one_month += 5.50
    elif fee_for_one_month <= 30:
        fee_for_one_month += 4.35
    elif fee_for_one_month > 30:
        fee_for_one_month += 3.85

total_amount_due = fee_for_one_month * number_of_months_to_pay

if contract_term_two_years:
    total_amount_due -= total_amount_due * 3.75 / 100

print(f'{total_amount_due:.2f} lv.')
