from aocd import lines


class BingoCard:
    def __init__(self, card):
        self.card = card
        self.last_called = None
        self.marks = [[False for _ in range(5)] for _ in range(5)]

    def mark_number(self, number):
        self.last_called = number
        for row in range(5):
            for col in range(5):
                if self.card[row][col] == number:
                    self.marks[row][col] = True
                    if self.check_win_around_pos(row, col):
                        return True
        return False

    def check_win_around_pos(self, row, col):
        winning = False
        winning |= all(self.marks[row])
        winning |= all(x[col] for x in self.marks)
        return winning

    def score(self):
        unmarked = 0
        for row in range(5):
            for col in range(5):
                if not self.marks[row][col]:
                    unmarked += self.card[row][col]
        return unmarked * self.last_called

    def reset(self):
        self.last_called = None
        self.marks = [[False for _ in range(5)] for _ in range(5)]


draws = [int(x) for x in lines.pop(0).split(",")]
cards = []

board = []
for r in lines:
    if not r:
        continue
    board.append([int(x) for x in r.split()])
    if len(board) == 5:
        cards.append(BingoCard(board))
        board = []


def solution1(draws, cards):
    for d in draws:
        for c in cards:
            if c.mark_number(d):
                return c.score()


print("part a:", solution1(draws, cards))

for c in cards:
    c.reset()


def solution2(draws, cards):
    winning_cards = []
    for d in draws:
        for c in cards:
            if c not in winning_cards and c.mark_number(d):
                winning_cards.append(c)
    return winning_cards[-1].score()


print("part b:", solution2(draws, cards))
