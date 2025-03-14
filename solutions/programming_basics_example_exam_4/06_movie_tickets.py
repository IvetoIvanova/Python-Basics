a1 = int(input())
a2 = int(input())
n = int(input())

for sym1 in range(a1, a2):
    for sym2 in range(1, n):
        for sym3 in range(1, n // 2):
            sym4 = sym1

            if sym4 % 2 == 1 and (sym2 + sym3 + sym4) % 2 == 1:
                print(f"{chr(sym1)}-{sym2}{sym3}{sym4}")
