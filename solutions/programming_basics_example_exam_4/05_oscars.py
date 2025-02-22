actor_name = input()
academy_points = float(input())
num_of_evaluators = int(input())

nominee = False

for _ in range(num_of_evaluators):
    evaluator_name = input()
    evaluator_points = float(input())

    academy_points += (len(evaluator_name) * evaluator_points) / 2

    if academy_points >= 1250.5:
        nominee = True
        break

if nominee:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')

if academy_points < 1250.5:
    needed_points = 1250.5 - academy_points
    print(f'Sorry, {actor_name} you need {needed_points:.1f} more!')
