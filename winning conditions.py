#conditions for wining
def sum(x, y, z):
    return x + y + z

def check_for_Win(Player_1, Player_2):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(Player_1[win[0]], Player_1[win[1]], Player_1[win[2]]) == 3):
            print("P1 WINS")
            return 1 #1 for p1 and 0 for p2
        if(sum(Player_2[win[0]], Player_2[win[1]], Player_2[win[2]]) == 3):
            print("P2 WINS")
            return 0
    return - 1
