#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass
    
class RandomPlayer(Player):
    def move(self):
        throw = random.choice(moves)
        return (throw)
    
class ReflectPlayer:

    def __init__(self):

        Player.__init__(self)
        self.learn_move = None

    def move(self):
        if self.learn_move is None:
            throw = moves[0]                 
        else:
            throw = self.learn_move               
            return (throw)                        

    def learn(self, learn_move):

        self.learn_move = learn_move    

    def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class HumanPlayer:

    def move(self):

        throw = input('rock, paper, scissors? >')

        while throw != 'rock'and throw != 'paper'and throw != 'scissors':
            print('Sorry try again')
            throw = input('rock, paper, scissors? >')
        return (throw)
  
 class Cycles:

    def __init__(self):

        Player.__init__(self)
        self.step = 0

    def move(self):
        throw = None
        if self.step == 0:
            throw = moves[0]
            self.step = self.step + 1
        elif self.step == 1:
            throw = moves[1]
            self.step = self.step + 1
        else:
            throw = moves[2]
            self.step = self.step + 1
        return throw

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    answer = [Player(), RandomPlayer(), ReflectPlayer(), Cycles()]
    p2 = input('Select the RPS game you would like to play or just hit any\
 key and enter for random game: [1]Rock, [2]Random,\
[3]Reflective, or [4]Cycles: >')

    while p2 != 1 or p2 != 2 or p2 != 3 or p2 != 4:
        p2 = random.choice(answer)
        break

    if p2 == '1':
        p2 = Player()
    elif p2 == '2':
        p2 = RandomPlayer()
    elif p2 == '3':
        p2 = ReflectPlayer()
    elif p2 == '4':
        p2 = Cycles()
