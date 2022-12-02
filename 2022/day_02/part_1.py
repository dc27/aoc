file = 'input.txt'

# function to get game score
def rps(game_string):
	op = game_string[0]
	me = game_string[2]

	lookups = {
		'A' : 'rock', 'B' : 'paper', 'C': 'scissors',
		'X' : 'rock', 'Y' : 'paper', 'Z': 'scissors'
		}

	op, me = lookups[op], lookups[me]

	action_scores = {'rock' : 1, 'paper' : 2, 'scissors' : 3}
	outcomes = ['rock', 'paper', 'scissors']
	# initial score
	score = action_scores[me]

	if outcomes.index(op) == outcomes.index(me):
		score += 3
	elif outcomes.index(op) - outcomes.index(me) in [-1, len(outcomes) -1]:
		score += 6

	# print(f'op: {op}, me: {me}, score: {score}')	
	return(score)
	

TOTAL_SCORE = 0

for line in open(file):
	TOTAL_SCORE += rps(line.strip())

print(TOTAL_SCORE)
