# Morosan Eric (252) and Patranjel David (251)
import random as r
import matplotlib.pyplot as plt
cards = ['11', '2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10'] * 24  # sunt 4 de 10 pt ca sunt si K Q J
i = 0


def decide(score, score_type, dealer_score):
    if score_type == "HARD":
        if score <= 8:
            return ("HIT", "HIT")
        if score == 9:
            if dealer_score == 2 or dealer_score > 6:
                return ("HIT", "HIT")
            else:
                return ("DOUBLE", "HIT")
        if score == 10:
            if dealer_score > 9:
                return ("HIT", "HIT")
            else:
                return ("DOUBLE", "HIT")
        if score == 11:
            return ("DOUBLE", "HIT")
        if score == 12:
            if 3 < dealer_score < 7:
                return ("STAND", "STAND")
            else:
                return ("HIT", "HIT")
        if 12 < score < 17:
            if dealer_score < 7:
                return ("STAND", "STAND")
            else:
                return ("HIT", "HIT")
        if score > 16:
            return ("STAND", "STAND")

    if score_type == "SOFT":
        if score == 13 or score == 14:
            if dealer_score == 5 or dealer_score == 6:
                return ("DOUBLE", "HIT")
            else:
                return ("HIT", "HIT")
        if score == 15 or score == 16:
            if 3 < dealer_score < 7:
                return ("DOUBLE", "HIT")
            else:
                return ("HIT", "HIT")
        if score == 17:
            if 2 < dealer_score < 7:
                return ("DOUBLE", "HIT")
            else:
                return ("HIT", "HIT")
        if score == 18:
            if 2 < dealer_score < 7:
                return ("DOUBLE", "STAND")
            if dealer_score > 8:
                return ("HIT", "HIT")
            else:
                return ("STAND", "STAND")
        if score >= 19:
            return ("STAND", "STAND")

    if score_type == "PAIR":
        if score == 4 or score == 6:
            if dealer_score > 7:
                return ("HIT", "HIT")
            else:
                return ("SPLIT", "HIT")
        if score == 8:
            if dealer_score == 5 or dealer_score == 6:
                return ("SPLIT", "HIT")
            else:
                return ("HIT", "HIT")
        if score == 10:
            if dealer_score < 10:
                return ("DOUBLE", "HIT")
            else:
                return ("HIT", "HIT")
        if score == 12:
            if dealer_score < 4:
                return ("SPLIT", "HIT")
            if 3 < dealer_score < 7:
                return ("SPLIT", "STAND")
            else:
                return ("HIT", "HIT")
        if score == 14:
            if dealer_score == 7:
                return ("SPLIT", "HIT")
            if dealer_score < 7:
                return ("SPLIT", "STAND")
            else:
                return ("HIT", "HIT")
        if score == 16:
            if dealer_score < 7:
                return ("SPLIT", "STAND")
            else:
                return ("SPLIT", "HIT")
        if score == 18:
            if dealer_score == 7 or dealer_score > 9:
                return ("STAND", "STAND")
            else:
                return ("SPLIT", "STAND")
        if score == 20:
            return ("STAND", "STAND")
        if score == 22:
            return ("SPLIT", "HIT")


def split(player, dealer):
    global i
    aces_player = 0
    first_round = True
    double = False
    if cards[i] == '11':
        aces_player += 1
        player = (player[0] + 11, 'SOFT')
    else:
        player = (player[0] + int(cards[i]), player[1])
    i += 1
    status = decide(player[0], player[1], dealer[0])
    while (status[0] != 'STAND' and first_round) or status[1] != 'STAND':
        actual_status = status[0]
        if first_round:
            first_round = False
            if actual_status == 'HIT':
                if cards[i] == '11':
                    aces_player += 1
                    player = (player[0] + 11, 'SOFT')
                else:
                    player = (player[0] + int(cards[i]), player[1] if player[1] != 'PAIR' else 'HARD')
                i += 1

                if player[0] > 21:
                    if player[1] == 'HARD':
                        return -1
                    else:
                        aces_player -= 1
                        if aces_player == 0:
                            player = (player[0] - 10, 'HARD')
                        else:
                            player = (player[0] - 10, 'SOFT')
            elif actual_status == 'DOUBLE':
                if cards[i] == '11':
                    aces_player += 1
                    player = (player[0] + 11, 'SOFT')
                else:
                    player = (player[0] + int(cards[i]), player[1] if player[1] != 'PAIR' else 'HARD')
                i += 1


                if player[0] > 21:
                    if player[1] == 'HARD':
                        return -1
                    else:
                        aces_player -= 1
                        if aces_player == 0:
                            player = (player[0] - 10, 'HARD')
                        else:
                            player = (player[0] - 10, 'SOFT')

                double = True
        else:
            if cards[i] == '11':
                aces_player += 1
                player = (player[0] + 11, 'SOFT')
            else:
                player = (player[0] + int(cards[i]), player[1])
            i += 1


            if player[0] > 21:
                if player[1] == 'HARD':
                    return -1
                else:
                    aces_player -= 1
                    if aces_player == 0:
                        player = (player[0] - 10, 'HARD')
                    else:
                        player = (player[0] - 10, 'SOFT')

        status = decide(player[0], player[1], dealer[0])
        if actual_status == 'DOUBLE':
            status = ('STAND', 'STAND')

    return (player, double)


def win_round():
    aces_player_flag = False
    global i
    first_round, double = True, False
    dealer, player = (0, ''), (0, '')  # scor type
    aces_player, aces_dealer = 0, 0
    flag_pair = False
    ret1, ret2 = (0, ''), (0, '')
    # player picks card
    if cards[0] == '11':
        player = (11, 'SOFT')
        aces_player += 1
    else:
        player = (int(cards[0]), 'HARD')

    # dealer picks card
    if cards[1] == '11':
        aces_dealer += 1
        dealer = (11, 'SOFT')
    else:
        dealer = (int(cards[1]), 'HARD')

    # player picks another card
    if cards[0] == '11' and cards[2] == '11':
        scor1 = int(cards[0]) + int(cards[4])
        scor2 = int(cards[2]) + int(cards[5])
        if scor1 > 21:
            scor1 -= 10
        if scor2 > 21:
            scor2 -= 10
        i = 6
        flag_pair = True
        aces_player_flag = True
        ret1 = ((scor1, 'SOFT'), False)
        ret2 = ((scor2, 'SOFT'), False)

    if cards[2] == '11':
        aces_player += 1
        player = (player[0] + 11, 'SOFT')
    else:
        if player[0] == int(cards[2]):
            player = (player[0] + int(cards[2]), 'PAIR')
        else:
            player = (player[0] + int(cards[2]), player[1])

    # blackjack 4 player
    if player[0] == 21:
        # case
        if int(cards[3]) + int(cards[1]) == 21:
            return 0
        else:
            return 1.5

    # blackjack 4 dealer
    if int(cards[3]) + int(cards[1]) == 21:
        return -1

    i = 4

    status = decide(player[0], player[1], dealer[0])
    while ((status[0] != 'STAND' and first_round) or status[1] != 'STAND') and not aces_player_flag:
        actual_status = status[0]
        if first_round:
            first_round = False
            if actual_status == 'HIT':
                if cards[i] == '11':
                    aces_player += 1
                    player = (player[0] + 11, 'SOFT')
                else:
                    player = (player[0] + int(cards[i]), player[1] if player[1] != 'PAIR' else 'HARD')
                i += 1
                if player[0] > 21:
                    if player[1] == 'HARD':
                        return -1
                    else:
                        aces_player -= 1
                        if aces_player == 0:
                            player = (player[0] - 10, 'HARD')
                        else:
                            player = (player[0] - 10, 'SOFT')
            elif actual_status == 'DOUBLE':
                if cards[i] == '11':
                    aces_player += 1
                    player = (player[0] + 11, 'SOFT')
                else:
                    player = (player[0] + int(cards[i]), player[1] if player[1] != 'PAIR' else 'HARD')
                i += 1

                if player[0] > 21:
                    if player[1] == 'HARD':
                        return -1
                    else:
                        aces_player -= 1
                        if aces_player == 0:
                            player = (player[0] - 10, 'HARD')
                        else:
                            player = (player[0] - 10, 'SOFT')

                double = True
            elif actual_status == 'SPLIT':
                player = (player[0] // 2, 'HARD')
                ret1 = split(player, dealer)
                ret2 = split(player, dealer)
                flag_pair = True
                break
        else:
            if cards[i] == '11':
                aces_player += 1
                player = (player[0] + 11, 'SOFT')
            else:
                player = (player[0] + int(cards[i]), player[1] if player[1] != 'PAIR' else 'HARD')
            i += 1

            if player[0] > 21:
                if player[1] == 'HARD':
                    return -1
                else:
                    aces_player -= 1
                    if aces_player == 0:
                        player = (player[0] - 10, 'HARD')
                    else:
                        player = (player[0] - 10, 'SOFT')

        status = decide(player[0], player[1], dealer[0])
        if actual_status == 'DOUBLE':
            status = ('STAND', 'STAND')

    # am iesit din while fara return, inseamna ca jucatorul a dat stand si nu are mai mult de 21 scor
    if cards[3] == '11':
        aces_dealer += 1
        dealer = (dealer[0] + 11, 'SOFT')
    else:
        dealer = (int(cards[3]) + dealer[0], dealer[1])

    if dealer[0] > 21:
        if dealer[1] == 'HARD':
            if double:
                return 2
            else:
                return 1
        else:
            aces_dealer -= 1
            if aces_dealer == 0:
                dealer = (dealer[0] - 10, 'HARD')
            else:
                dealer = (dealer[0] - 10, 'SOFT')

    while dealer[0] < 17:
        if cards[i] == '11':
            aces_dealer += 1
            dealer = (dealer[0] + 11, 'SOFT')
        else:
            dealer = (int(cards[i]) + dealer[0], 'HARD')

        i += 1

        if dealer[0] > 21:
            if dealer[1] == 'HARD':
                if double:
                    return 2
                else:
                    return 1
            else:
                aces_dealer -= 1
                if aces_dealer == 0:
                    dealer = (dealer[0] - 10, 'HARD')
                else:
                    dealer = (dealer[0] - 10, 'SOFT')

    if flag_pair:
        cost = 0
        if type(ret1) == type(-1):
            cost += ret1
        else:
            player1, double1 = ret1
            if dealer[0] == player1[0]:
                cost += 0
            elif dealer[0] < player1[0]:
                if double1:
                    cost += 2
                else:
                    cost += 1
            else:
                if double1:
                    cost += -2
                else:
                    cost += -1
        if type(ret2) == type(-1):
            cost += ret2
        else:
            player1, double1 = ret2
            if dealer[0] == player1[0]:
                cost += 0
            elif dealer[0] < player1[0]:
                if double1:
                    cost += 2
                else:
                    cost += 1
            else:
                if double1:
                    cost += -2
                else:
                    cost += -1
        return cost
    else:
        if dealer[0] == player[0]:
            return 0
        elif dealer[0] < player[0]:
            if double:
                return 2
            else:
                return 1
        else:
            if double:
                return -2
            else:
                return -1


win_count = 0
game_length_history = []
def play_blackjack(m, M):
    game_length = 0
    while 0 < m < M:
        game_length += 1
        # print(f"JOC {cont}:")
        r.shuffle(cards)
        # print(cards[:10])
        w = win_round()
        # print(w)
        # print("---------------------------------------------")
        m += w

    if m >= M:
        return True, game_length
    return False, game_length


start = int(input())
stop = int(input())
N =int(input())
for i in range(N):
    result = play_blackjack(start, stop)
    if result[0]:
        win_count += 1
        game_length_history.append(result[1])
    else:
        game_length_history.append(result[1])


print(f"Sansa de a castiga {stop} lei cu {start} lei dupa simularea a {N} jocuri este {win_count/N}")

plt.figure()
plt.hist(game_length_history, bins=100)
