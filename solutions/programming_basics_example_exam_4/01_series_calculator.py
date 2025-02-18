import math

series_name = input()
seasons_number = int(input())
episodes_number = int(input())
episode_duration_without_ads = float(input())

ads_duration_per_episode = episode_duration_without_ads * 0.20
episode_duration_with_ads = episode_duration_without_ads + ads_duration_per_episode
extra_time = seasons_number * 10

total_time = math.floor((episode_duration_with_ads * episodes_number * seasons_number) + extra_time)

print(f'Total time needed to watch the {series_name} series is {total_time} minutes.')
