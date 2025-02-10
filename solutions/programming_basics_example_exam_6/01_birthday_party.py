rent = float(input())

cake = rent * 0.20
drinks = cake * 0.55
animator = rent / 3

needed_budget = rent + cake + drinks + animator

print(f"{needed_budget:.1f}")
