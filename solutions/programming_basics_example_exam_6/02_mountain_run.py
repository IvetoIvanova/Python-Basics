import math

record_in_sec = float(input())
distance_in_meters = float(input())
seconds_per_one_meter = float(input())

total_seconds_without_delay = distance_in_meters * seconds_per_one_meter
delay_in_seconds = math.floor(distance_in_meters / 50) * 30

total_seconds = total_seconds_without_delay + delay_in_seconds

if record_in_sec > total_seconds:
    print(f'Yes! The new record is {total_seconds:.2f} seconds.')
else:
    needed_seconds = total_seconds - record_in_sec
    print(f'No! He was {needed_seconds:.2f} seconds slower.')
