"""
This class is responsible for storing info about current state of game, also responsible for determining legal
moves, keeps track of moves
"""



p1=input("Input Player 1 name")
p2=input("Input player 2 name")


p1_score=0
p2_score=0
print("The Game is about to begin: \n Here are the rules")
print("Each player gets a chance to guess the correct word alternatively."
        "\nIf the player is able to guess correctly,he/she gains 10 points"
        "\nIf the guess is wrong, you lose 2 points"
        "\nAfter 2 chances, the game ends."
        "\nThe player with maximum points wins"
      "                                                            ")
game="active"

a1=input(print( "player 1 enter a word starting with 'a'"))
if a1=="apple":
    p1_score+=10
    print("Correct answer!")
else:
     p1_score-=2
     print("Wrong answer!")


