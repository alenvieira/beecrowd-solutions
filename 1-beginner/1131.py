winner_inter = 0
winner_gremio = 0
tie_game = 0
n_game = 0
user_input = ''
while user_input != '2':
    user_input = input()
    inter, gremio = [int(i) for i in user_input.split(' ')]
    if inter == gremio:
        tie_game += 1
    elif inter < gremio:
        winner_gremio += 1
    elif inter > gremio:
        winner_inter += 1
    n_game += 1
    print('Novo grenal (1-sim 2-nao)')
    user_input = input()
print('{} grenais'.format(n_game))
print('Inter:{}'.format(winner_inter))
print('Gremio:{}'.format(winner_gremio))
print('Empates:{}'.format(tie_game))
if winner_inter == winner_gremio:
    print('Nao houve vencedor')
elif winner_inter < winner_gremio:
    print('Gremio venceu mais')
elif winner_inter > winner_gremio:
    print('Inter venceu mais')