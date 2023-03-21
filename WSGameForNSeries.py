# Name: Arav Bhagwati
# Simulates one game for multiple series. It is similar to the class for one series, but the difference is that this one doesn't send the playbyplay to an output file


from WSPlayer import Player
import random

class gameNSeries:
    """This is a Game object for multiple series."""
    def __init__(self, game_number):
        # Rays lineup/stats
        self.Choi = Player("J. Choi", 0.23, 28, 13, 0, 3)
        self.Arozarena = Player("R. Arozarena", 0.281, 18, 2, 0, 7)
        self.Meadows = Player("A. Meadows", 0.205, 27, 8, 1, 4)
        self.Lowe = Player("B. Lowe", 0.269, 52, 9, 2, 14)
        self.Margot = Player("M. Margot", 0.269, 39, 9, 0, 1)
        self.Wendle = Player("J. Wendle", 0.286, 48, 9, 2, 4)
        self.Adames = Player("W. Adames", 0.259, 48, 15, 1, 8)
        self.Kiermaier = Player("K. Kiermaier", 0.217, 30, 5, 3, 3)
        self.Zunino = Player("M. Zunino", 0.147, 11, 4, 0, 4)
        self.rays = [self.Choi, self.Arozarena, self.Meadows, self.Lowe, self.Margot, self.Wendle, self.Adames, \
                     self.Kiermaier, self.Zunino]

        self.game_number = game_number

        # Dodgers lineup/stats
        self.Betts = Player("M. Betts", 0.292, 64, 9, 1, 16)
        self.Seager = Player("C. Seager", 0.307, 65, 12, 1, 15)
        self.Turner = Player("J. Turner", 0.307, 46, 9, 1, 4)
        self.Muncy = Player("M. Muncy", 0.192, 39, 4, 0, 12)
        self.Smith = Player("W. Smith", 0.289, 33, 9, 0, 8)
        self.Bellinger = Player("C. Bellinger", 0.239, 51, 10, 0, 12)
        self.Taylor = Player("C. Taylor", 0.27, 50, 10, 2, 8)
        self.Pollock = Player("A. Pollock", 0.276, 54, 9, 0, 16)
        self.Barnes = Player("A. Barnes", 0.244, 21, 3, 0, 1)
        self.dodgers = [self.Betts, self.Seager, self.Turner, self.Muncy, self.Smith, self.Bellinger, self.Taylor, \
                        self.Pollock, self.Barnes]
        
        # next player up for rays (this, along with other stuff below, helps save who is up to bat next after each inning)
        self.rays_batterUp = 0
        # next player up for rays (this, along with other stuff below, helps save who is up to bat next after each inning)
        self.dodgers_batterUp = 0

        # empty scores list for each team
        self.raysScore = []
        self.dodgersScore = []

    # Not sure if I need the 'scored' lists in this siminning method
    def simInning(self, team): # simming one inning method
        "Simulates one inning"
        outs = 0
        nobody = Player("",1,1,1,1,1) # initializing a 'nobody' to put on the bases so that it is easier to move the bases around
        bases = [nobody, nobody, nobody] # [ nobody on 1st base, nobody on 2nd base, nobody on 3rd base]
        team_score = 0
        while outs < 3: # 3 since there are 3 outs in an inning
            player = Player("",1,1,1,1,1)
            if (team[0].getName() == "J. Choi"): # if Rays are hitting, then it keeps track of who is hitting on the Rays
                if (self.rays_batterUp > (len(self.rays)-1)):
                    self.rays_batterUp = 0
                player = team[self.rays_batterUp]
            else:  # if Dodgers are hitting, then it keeps track of who is hitting on the Dodgers
                if (team[0].getName() == "M. Betts"):
                    if (self.dodgers_batterUp > (len(self.dodgers)-1)):
                        self.dodgers_batterUp = 0
                    player = team[self.dodgers_batterUp]
            
            hit = player.swing() # player swings
            if hit == 0: # player gets out
                types_of_outs = ["struck out", "grounded out", "flied out", "lined out"] # I wanted to make it so that theres multiple types of outs and not just strikeout, so I had it choose randomly
                msg = types_of_outs[random.randrange(0,4)]
                outs = outs + 1
            # player hits single
            if hit == 1:
                if bases[2].getName() != "":  # if somebody is on third, then they score. Nobody else can score; just if someone is on third
                    team_score = team_score + 1
                bases[2] = bases[1] # moving the bases around
                bases[1] = bases[0]
                bases[0] = player
            
            if hit == 2: # player hits double
                msg = ""
                if bases[2].getName() != "": # if somebody is on third, they score
                    team_score = team_score + 1
                if bases[1].getName() != '':  # if somebody is on second, they score, nobody from first can score on a double
                    team_score = team_score + 1
                bases[2] = bases[0] # moving the bases around
                bases[1] = player
                bases[0] = nobody
                    
            if hit == 3: # player hits triple
                if bases[2].getName() != "": # if somebody is on third, they score
                    team_score = team_score + 1
                if bases[1].getName() != "":  # if somebody is on second, they score
                    team_score = team_score + 1
                if bases[0].getName() != "": # if somebody is on first, they score
                    team_score = team_score + 1
                bases[2] = player # move bases around
                bases[0] = nobody
                bases[1] = nobody
        
            if hit == 4: # player hits homer
                if bases[2].getName() != "":  # if somebody is on third, they score
                    team_score = team_score + 1
                if bases[1].getName() != "": # if somebody is on second, they score
                    team_score = team_score + 1
                if bases[0].getName() != "": # if somebody is on first, they score
                    team_score = team_score+ 1
                team_score = team_score + 1
                bases[0] = nobody # moving the bases around
                bases[1] = nobody
                bases[2] = nobody

            if team[0].getName() == "J. Choi": # if Rays are hitting, the next batter is up
                self.rays_batterUp = self.rays_batterUp + 1
            else: # if Dodgers are hitting, the next batter is up
                self.dodgers_batterUp = self.dodgers_batterUp + 1

            if outs == 3: # if the outs are 3, get the score of that inning and append it to the score list and end the inning
                if team[0].getName() == "J. Choi":
                    self.raysScore.append(team_score)
                elif team[0].getName() == "M. Betts":
                    self.dodgersScore.append(team_score)
                break

                
    def runGame(self): # simming one game method
        "Simulates one game."
        # loop simulates game
        for i in range(1,10):  # since there are 9 innings, we do range(1,10) since 10 in not included in the range
            self.simInning(self.rays)
            self.simInning(self.dodgers)
    
        if sum(self.raysScore) == sum(self.dodgersScore): # going into extra innings
            i = 9
            while sum(self.raysScore) == sum(self.dodgersScore): # while the scores are equal, keep going
                i = i + 1
                self.simInning(self.rays)
                self.simInning(self.dodgers)
                if sum(self.dodgersScore) != sum(self.raysScore): # once the scores don't equal each other after an inning is completed, the game is over 
                    break
        
    def getRaysScore(self):
        "Returns the Rays score"
        return sum(self.raysScore)

    def getDodgersScore(self):
        "Returns the Dodgers score."
        return sum(self.dodgersScore)

   
        
