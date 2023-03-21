#
# Name: Arav Bhagwati
# Main Module
# Contains simualtion functions for one series, multiple series, and the main function
# Also has the intro and the getInput functions

# Description of my design strategy:
# For this lab, I used bottom-up implementation and unit testing. For example, I started off with the lowest level of the simulation (one inning) and worked my way up from there, testing each part after I finished it. I tested one inning, one game, one series, and then multiple series.
# I felt like this design strategy would best help me achieve my goal of implementing this entire simulation because through unit testing, I would know if each component functions properly. 

from WSGameForOneSeries import gameOneSeries
from WSGameForNSeries import gameNSeries

def simOneSeries(): # simulates one series for the one series user option
    outputfile = open("WSplaybyplay.py", "w") # this will override the WSplaybyplay file if user wants to run the entire program multiple times (only one series will be written to that file)
    print("Results of World Series Simulation")
    print()
    # Both teams start at 0 wins
    Rays_wins = 0
    Dodgers_wins = 0
    Rays_homers = []
    Dodgers_homers = []
    series_winner = ""
    for i in range(1,8): # best of 7 series
        simGame = gameOneSeries(i) # simGame is the variable for the function that is called, so that if we keep calling it multiple times, it doesn't keep changing
        print("Game", i, end="")
        print(":", end=" ")
        simGame.runGame()
        print("Rays", simGame.getRaysScore(), "Dodgers", simGame.getDodgersScore()) # printing each score/outcome of each game of series
        if simGame.getRaysScore() > simGame.getDodgersScore(): # if Rays win, add 1 to Rays_wins
            Rays_wins = Rays_wins + 1
        elif simGame.getDodgersScore() > simGame.getRaysScore(): # if odgers win, add 1 to Dodgers_wins
            Dodgers_wins = Dodgers_wins + 1

        Rays_homers = Rays_homers + simGame.homerCountRays() # list concatenation by joining an empty list and the list in the Game class by calling the homer function
        Dodgers_homers = Dodgers_homers + simGame.homerCountDodgers()  # list concatenation by joining an empty list and the list in the Game class by calling the homer function

        # since it is a best of 7 series, which ever team gets to 4 wins first wins the series
        if Rays_wins == 4: 
            print()
            print("Rays win the series 4" + "-" + str(Dodgers_wins))
            series_winner = "Rays"
            break
        elif Dodgers_wins == 4:
            print()
            print("Dodgers win the series 4" + "-" + str(Rays_wins))
            series_winner = "Dodgers"
            break
    print()

    # Home Runs sorting and counting
    print("Home Runs:",)

    # Rays Homers
    Rays_players_dict = {"Choi":"J.","Arozarena":"R.","Meadows":"A.","Lowe":"B.","Margot":"M.","Wendle":"J.","Adames":"W.",\
                   "Kiermaier":"K.","Zunino":"M."} # Since we made a method to get the last name in the player class and used that to count the homers, this dictionary allows us to add back the first initial of each player 
    Rays_homers.sort() # sorting alphabetically
    Rays_homers2 = [] # new empty homers list
    for player in Rays_homers: # adding the players to the Rays_homers2 list through their dictionary key value and their last name. However, multiple occurrences of each name could show up based on how many homers they hit.
        Rays_homers2.append(Rays_players_dict[player] + " " + player)
    Rays_homers2 = sorted(Rays_homers2,key=Rays_homers2.count,reverse=True) # this sorts the new list based on the frequency of each player in the list (descending order)

    Rays_homers3 = [] # new empty homers list (final one)
    for player in Rays_homers2: # this will go through and see how many occurrences of each player there is in the list, then adding that number to the end of the player string
        count = Rays_homers2.count(player)
        Rays_homers3.append(player + " " + str(count))

    for i in range(3): # this for loop ensures that the list is fully filtered and the frequency of each element in the list is only 1
        for player in Rays_homers3:
            count = Rays_homers3.count(player)
            if count > 1:
                Rays_homers3.remove(player)
   
    # Dodgers Homers
    Dodgers_players_dict = {"Betts":"M.","Seager":"C.","Turner":"J.","Muncy":"M.","Smith":"W","Bellinger":"C.","Taylor":"C.",\
                            "Pollock":"A.","Barnes":"A."} # Since we made a method to get the last name in the player class and used that to count the homers, this dictionary allows us to add back the first initial of each player 
    Dodgers_homers.sort() # sorting alphabetically
    Dodgers_homers2 = [] # new empty homers list
    for player in Dodgers_homers: # adding the players to the Rays_homers2 list through their dictionary key value and their last name. However, multiple occurrences of each name could show up based on how many homers they hit.
        Dodgers_homers2.append(Dodgers_players_dict[player] + " " + player)
    Dodgers_homers2 = sorted(Dodgers_homers2,key=Dodgers_homers2.count,reverse=True)  # this sorts the new list based on the frequency of each player in the list (descending order)

    Dodgers_homers3 = [] # new empty homers list (final one)
    for player in Dodgers_homers2: # this will go through and see how many occurrences of each player there is in the list, then adding that number to the end of the player string
        count = Dodgers_homers2.count(player)
        Dodgers_homers3.append(player + " " + str(count))

    for i in range(3): # this for loop ensures that the list is fully filtered and the frequency of each element in the list is only 1
        for player in Dodgers_homers3:
            count = Dodgers_homers3.count(player)
            if count > 1:
                Dodgers_homers3.remove(player)
    
    if series_winner == "Dodgers": # if Dodgers win the series
        print("Dodgers - ", end="")
        print(*Dodgers_homers3, sep=", ")
        print("Rays - ", end="")
        print(*Rays_homers3, sep=", ")
    elif series_winner == "Rays": # if Rays win the series
        print("Rays - ", end="")
        print(*Rays_homers3, sep=", ")
        print("Dodgers - ", end="")
        print(*Dodgers_homers3, sep=", ")

def simSeriesForNSeries(): # simulates one series for the multiple series user option
    # Both teams' games wins are 0
    Rays_wins = 0
    Dodgers_wins = 0
    for i in range(1,8): # best of 7 series
        simGame = gameNSeries(i) # simGame is the variable for the function that is called, so that if we keep calling it multiple times, it doesn't keep changing
        simGame.runGame()
        if simGame.getRaysScore() > simGame.getDodgersScore(): # if Rays win
            Rays_wins = Rays_wins + 1
        elif simGame.getDodgersScore() > simGame.getRaysScore(): # if Dodgers win
            Dodgers_wins = Dodgers_wins + 1

        if Rays_wins == 4: # if Rays win, return the string below
            return "Rays win in " +  str(i)
            break
        elif Dodgers_wins == 4: # if Dodgers win, return the string below
            return "Dodgers win in " + str(i)
            break

def simNSeries(n): # simulates 'n' amount of series using the above function (simseriesForNSeries)
    outputfile = open("WSsimulations.py", "w") # open this outfile to write every series outcome to it
    print("Dodgers-Rays World Series Simulation", file=outputfile)
    print(file=outputfile)
    print("Results of", n, "World Series Simulations")
    print()
    # empty list for each possile outcome (8 possible outcomes)
    Rays_4 = []
    Rays_5 = []
    Rays_6 = []
    Rays_7 = []
    Dodgers_4 = []
    Dodgers_5 = []
    Dodgers_6 = []
    Dodgers_7 = []
    for i in range(1,n+1): # range(1,n+1) since n won't be included if the range is just (1,n)
        win_decider = simSeriesForNSeries() # variable for function so that the value returned from it doesn't change
        if win_decider == "Rays win in 4": # rays win in 4
            Rays_4.append("win")
        elif win_decider == "Rays win in 5": # rays win in 5
            Rays_5.append("win")
        elif win_decider == "Rays win in 6": # rays win in 6
            Rays_6.append("win")
        elif win_decider == "Rays win in 7": # rays win in 7
            Rays_7.append("win")
        elif win_decider == "Dodgers win in 4": # dodgers win in 4
            Dodgers_4.append("win")
        elif win_decider == "Dodgers win in 5": # dodgers win in 5
            Dodgers_5.append("win")
        elif win_decider == "Dodgers win in 6": # dodgers win in 6
            Dodgers_6.append("win")
        elif win_decider == "Dodgers win in 7": # dodgers win in 7
            Dodgers_7.append("win")

        print(str(i) + ":", win_decider, file=outputfile) # prints outcome of each series to the output file

    # Each of these below prints the percentage of results for each outcome. It is calculated based on the length of each list divided by the number of series's that were played.
    print("Rays win in 4 -", str(round((len(Rays_4) / n) * 100, 1)) + "%")
    print("Rays win in 5 -", str(round((len(Rays_5) / n) * 100, 1)) + "%")
    print("Rays win in 6 -", str(round((len(Rays_6) / n) * 100, 1)) + "%")
    print("Rays win in 7 -", str(round((len(Rays_7) / n) * 100, 1)) + "%")
    print("Dodgers win in 4 -", str(round((len(Dodgers_4) / n) * 100, 1)) + "%")
    print("Dodgers win in 5 -", str(round((len(Dodgers_5) / n) * 100, 1)) + "%")
    print("Dodgers win in 6 -", str(round((len(Dodgers_6) / n) * 100, 1)) + "%")
    print("Dodgers win in 7 -", str(round((len(Dodgers_7) / n) * 100, 1)) + "%")
    

def intro():
    # print the introduction
    print("This program simulates the last World Series between the Rays and the Dodgers. ")

def getInputs():
    # Returns how many World Series user wants to simulate
    n = int(input("How many World Series would you like to simulate? "))
    return n

def main():  # main function
    intro() # call intro
    sim_again = "yes" 
    while sim_again[0] == "y": # using the interactive loop to see if user would like to simulate multiple times
        try: # input validation
            n = getInputs()
            if n <= 0:  # create an error and address it in the except statement
                n = 1 / 0
            elif n == 1:
                simOneSeries()
            else:
                simNSeries(n)

            sim_again = input("Do you want to simulate again? ")

        except ZeroDivisionError:
            print("You must enter an integer greater than zero.")
            sim_again = input("Do you want to try again? ")
        except ValueError:
            print("You must enter an integer greater than zero.")
            sim_again = input("Do you want to try again? ")

                   
main()
    





