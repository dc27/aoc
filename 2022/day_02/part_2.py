file = 'input.txt'

# function to get game score
def rps(game_string):
	op = game_string[0]
	me = game_string[2]

	lookups = {
		'A' : 'rock', 'B' : 'paper', 'C': 'scissors',
		'X' : 'lose', 'Y' : 'draw', 'Z': 'win'
		}

	op, me = lookups[op], lookups[me]

	action_scores = {'rock' : 1, 'paper' : 2, 'scissors' : 3}
	game_scores = {'draw' : 3, 'win' : 6, 'lose': 0}

	outcomes = ['rock', 'paper', 'scissors']
	# initial score
	score = game_scores[me]

	if me == 'lose':
		me_index = outcomes.index(op) - 1
		me = outcomes[me_index]
	elif me == 'draw':
		me = op[:]
	elif me == 'win':
		me_index = outcomes.index(op) - 2
		me = outcomes[me_index]

	score += action_scores[me]    
	# print(f'op: {op}, me: {me}, score: {score}')	
	return(score)
	

TOTAL_SCORE = 0

for line in open(file):
	TOTAL_SCORE += rps(line.strip())

print(TOTAL_SCORE)
