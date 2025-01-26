control_minutes = int(input())
control_seconds_input = int(input())
chute_length_in_meters = float(input())
seconds_to_100_meters = int(input())

control_in_seconds = (control_minutes * 60) + control_seconds_input
decrease_time = (chute_length_in_meters / 120) * 2.5
marin_time_in_seconds = ((chute_length_in_meters / 100) * seconds_to_100_meters) - decrease_time

if marin_time_in_seconds <= control_in_seconds:
    print('Marin Bangiev won an Olympic quota!')
    print(f'His time is {marin_time_in_seconds:.3f}.')
else:
    missing_seconds = marin_time_in_seconds - control_in_seconds
    print(f'No, Marin failed! He was {missing_seconds:.3f} second slower.')
