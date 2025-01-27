hall_rent = int(input())

statuettes = hall_rent * 0.70
catering = statuettes * 0.85
voiceover = catering / 2

total_sum = hall_rent + statuettes + catering + voiceover
print(f'{total_sum:.2f}')
