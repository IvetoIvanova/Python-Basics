num_of_bitcoins = int(input())
num_of_chinese_yuan = float(input())
commission = float(input())

sum_of_bitcoins_in_lv = num_of_bitcoins * 1168
sum_of_chinese_yuan_in_dollars = num_of_chinese_yuan * 0.15
sum_of_chinese_yuan_in_lv = sum_of_chinese_yuan_in_dollars * 1.76

total_sum_in_euro = (sum_of_bitcoins_in_lv + sum_of_chinese_yuan_in_lv) / 1.95
commission_of_total_sum = total_sum_in_euro * commission / 100
total_sum = total_sum_in_euro - commission_of_total_sum

print(f'{total_sum:.2f}')
