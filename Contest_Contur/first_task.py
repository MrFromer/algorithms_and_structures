import sys

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
mastei = ['C', 'D', 'H', 'S']

r1, s1, r2, s2 = map(int, sys.stdin.readline().split())

gray_podmnozhestva = [sys.stdin.readline().strip() for _ in range(r1 + s1)]

white_podmnozhestva = [sys.stdin.readline().strip() for _ in range(r2 + s2)]

def parse(s):

    podmnozh_ranks = []
    podmnozh_mastei = []

    for char in s:
        if char in ranks:
            podmnozh_ranks.append(char)
        elif char in mastei:
            podmnozh_mastei.append(char)

    if not podmnozh_ranks:
        podmnozh_ranks = ranks.copy()

    if not podmnozh_mastei:
        podmnozh_mastei = mastei.copy()

    cards = set()
    for r in podmnozh_ranks:
        for podmnozh in podmnozh_mastei:
            cards.add((r, podmnozh))
    return cards

def poisk_ver(r, s, podmnozhestva):

    deck = {(r, s) for r in ranks for s in mastei}
    to_remove = set()

    for i in range(r):
        podmnozh = parse(podmnozhestva[i])
        to_remove.update(podmnozh)

    deck -= to_remove

    if not deck:
        return 0
    win_cards = set()

    for i in range(r, r + s):
        podmnozh = parse(podmnozhestva[i])
        win_cards.update(podmnozh)
    win_in_deck = deck & win_cards

    if not win_in_deck:
        return 0
    return len(win_in_deck) / len(deck)


prob_gray = poisk_ver(r1, s1, gray_podmnozhestva)
prob_white = poisk_ver(r2, s2, white_podmnozhestva)

print("{0:.10f}".format(max(prob_gray, prob_white)))