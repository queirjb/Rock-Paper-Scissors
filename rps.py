## My Rock, Paper, Scissor Project
## for Udacity Into to Programming class
## Written by: Cambron Deatherage
##Rules:
##Rock beats scissors
##Scissors beats paper
##Paper beats rock

import random

moves = ['rock', 'paper', 'scissors']

class Player():
    def __init__(self):
        self.score = 0

    def move(self):
        return moves[0]

    def learn(self, learn_move):

        pass
## Parent Player class




class RandomPlayer(Player):
    def move(self):
        throw = random.choice(moves)
        return (throw)
## This class selects a random move choice




class  ReflectPlayer(Player):

    def __init__(self):

        Player.__init__(self)
        self.learn_move = None

    def move(self):
        if self.learn_move == None:
          throw = moves[0]                      #  First move is always rock
        else:
          throw = self.learn_move               #  next move is humanplayers previous move
        return (throw)

    def learn(self, learn_move):

        self.learn_move = learn_move
## This Class reflects the human players 1st and 2nd moves



class Cycles(Player):

    def __init__(self):

        Player.__init__(self)
        self.step = 0

    def move(self):
        throw = None
        if self.step == 0:
          throw = moves[0]
          self.step = self.step +1
        elif self.step == 1:
          throw = moves[1]
          self.step = self.step +1
        else:
          throw = moves[2]
          self.step = self.step +1
        return throw
## This Class cycles through the moves list starting at rock




class HumanPlayer(Player):

    def move(self):

        throw = input('rock, paper, scissors? >')

        while throw != 'rock'and throw != 'paper'and throw != 'scissors':
          print('Sorry try again')
          throw = input('rock, paper, scissors? >')
        return (throw)
## This class requests a human player to make a selection


class Game():

    def __init__(self):
        self.p1 = HumanPlayer()
        self.p2 = RandomPlayer()



    def play_game(self):
        print("Rock Paper Scissors, Go!")
        for round in range(3):
          print (f"Round {round}:")
          self.play_round()
        if self.p1.score > self.p2.score:
            print('Player 1 won!')
        elif self.p1.score < self.p2.score:
            print('Player 2 won!')
        else:
            print('The game was a tie!')
        print('The final score ' + str(self.p1.score) + ' TO ' +
              str(self.p2.score))
  ## This class starts the game prints information and calls the playround class
  ## Also prints out the final score

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        result = Game.play(move1, move2)
        self.p1.learn(move2)
        self.p2.learn(move1)
##This class calls the play class, sets the move 1 and 2 variables
## then sets the result variable. Plus stores the players move


    def play(self, move1, move2):
            print(f"You played {move1}")
            print(f"Opponent played {move2}")
            if beats(move1, move2):
                print ("** PLAYER ONE WINS **")
                print(f"Score: Player 1: {move1}  Player 2: {move2}\n\n")
                self.p1.score += 1
                return 1
            elif beats(move2, move1):
                print ("** PLAYER TWO WINS **")
                print(f"Score: Player 1: {move1}  Player 2: {move2}\n\n")
                self.p2.score += 1
                return 2
            else:
                print ("** It's A TIE **")
                print(f"Score: Player 1: {move1}  Player 2: {move2}\n\n")
                return 0
## This class calls the beats functions


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))
## I believe beats would be considered a function and not a module because
## it not part of a class...







if __name__ == '__main__':
    #game = Game(Player(), Player())
    #game.play_game()
    Game = Game()
    Game.play_game()
