def f(player1, player2):
    player1val = 0
    player2val = 0
    for i in player1:
        if i == "A" or i == "K" or i == "Q" or i == "J" or i == "T":
            player1val += 10
        else:
            player1val += int(i)
    for i in player2:
        if i == "A" or i == "K" or i == "Q" or i == "J" or i == "T":
            player2val += 10
        else:
            player2val += int(i)
    if player1val > player2val:
        return True
    else:
        return False