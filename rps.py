#paper beats rock beats scissor beats paper

def rps(p1, p2):
    if p1 == p2:
        print("Both players chose {}. It's a Tie.".format(p1))
    elif (p1 == 'rock' and p2 == 'scissor') or (p1 == 'scissor' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
        print("{} beats {}. Player 1 Won!".format(p1, p2))
    else:
        print("{} beats {}. Player 2 Won!".format(p2, p1))


rps('rock', 'rock')
rps('rock', 'paper')
rps('rock', 'scissor')
rps('scissor', 'rock')
rps('paper', 'rock')