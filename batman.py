class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")


batsman1 = Batsman()
bowler1 = Bowler()


batsman1.play()  
bowler1.play()   
