from collections import defaultdict

file = "input.txt"

input_stream = [line.strip() for line in open(file, "r")]

# based on someone else's Dart code. still not 100% how the logic works.
def count_permutations(springs:list[str], conditions:list[int])->int:
    
    spring_permutation_counts = defaultdict(int)
    spring_permutation_counts[(0, 0)] = 1
    
    springs_checked = 0

    for spring in springs:
        # extract existing spring permutations
        spring_permutations = [
            (k[0], k[1], v) for k, v in spring_permutation_counts.items()
        ]

        spring_permutations_updated = []

        # update spring permutations based on current char
        if spring != '?':
            for p in spring_permutations:
                # case: # -> increment amount if conditions allow
                if spring == '#' and p[0] < len(conditions) and p[1] < conditions[p[0]]:
                    spring_permutations_updated.append((p[0], p[1] + 1, p[2]))
                # case: . , a == 0 keep existing permutation if amount is 0
                elif spring == '.' and p[1] == 0:
                    spring_permutations_updated.append(p)
                elif spring == '.' and p[1] == conditions[p[0]]:
                    spring_permutations_updated.append((p[0] + 1, 0, p[2]))
            spring_permutations = spring_permutations_updated.copy()
        else:
            for p in spring_permutations:
                if p[0] < len(conditions) and p[1] < conditions[p[0]]:
                    spring_permutations_updated.append((p[0], p[1] + 1, p[2]))
                if p[1] == 0:
                    spring_permutations_updated.append(p)
                elif p[1] == conditions[p[0]]: 
                    spring_permutations_updated.append((p[0] + 1, 0, p[2]))
            spring_permutations = spring_permutations_updated.copy()

        springs_checked += 1
        springs_left = len(springs[springs_checked:])

        # filter out impossible configs
        spring_permutations = [
            p for p in spring_permutations
            if (p[0] > len(conditions) and p[1] == 0)
            or (p[0] <= len(conditions) and springs_left + p[1] >= sum(conditions[p[0]:]))
            ]

        spring_permutation_counts.clear()
        for spring_permutation in spring_permutations:
            g, a, p = spring_permutation
            spring_permutation_counts[(g, a)] += p

    return sum(p[2] for p in spring_permutations)

# needed for p2
def unfold(springstr:str, raw_conditions:str)->tuple:

    springs_unfolded = (springstr + "?") * 5
    conditions_unfolded = (raw_conditions + ",") * 5

    groups = [int(i) for i in conditions_unfolded[0:-1].split(",")]
    return (list(springs_unfolded[0:-1]), groups)


p1 = 0
p2 = 0

for line in input_stream:
    all_springs, spring_condition = line.split(' ')

    conditions = list(map(int, spring_condition.split(',')))
    springs = list(all_springs)
    unfolded_springs, unfolded_conditions = unfold(all_springs, spring_condition)

    n_permutations =  count_permutations(springs, conditions)
    unfolded_n_permutations = count_permutations(unfolded_springs, unfolded_conditions)
    p1 += n_permutations
    p2 += unfolded_n_permutations

print(p1)
print(p2)