number_of_problem = int(input())

able_to_solve_problem = 0

for i in range(number_of_problem):
    a, b, c = map(int, input().split())
    if a+b+c >= 2:
        able_to_solve_problem += 1

print(able_to_solve_problem)
