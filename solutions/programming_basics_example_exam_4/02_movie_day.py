snapshot_time = int(input())
scenes_number = int(input())
scene_duration = int(input())

field_preparation_time = round(snapshot_time * 0.15)
total_time = (scenes_number * scene_duration) + field_preparation_time

if snapshot_time >= total_time:
    time_left = snapshot_time - total_time
    print(f'You managed to finish the movie on time! You have {time_left} minutes left!')
else:
    time_needed = total_time - snapshot_time
    print(f'Time is up! To complete the movie you need {time_needed} minutes.')
