#Author: JTI 9/28/21

team_1 = input("Enter number of wins for team 1: ")
team_1a = input("Enter number of ties for team 1: ")
team_2 = input("Enter number of wins for team 2: ")
team_2a = input("Enter number of ties for team 2: ")

win = 3
tie = 1 

team_1_total = int(team_1) + int(team_1a)
team_2_total = int(team_2) + int(team_2a)

difference = team_1_total - team_2_total

if team_1_total > team_2_total:
    print("team 1 scored more points then Team 2")
else:
    print("Team 2 score more points than Team 1")
