# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

#team_rankings = pd.read_csv('MDataFiles_Stage1/MMasseyOrdinals.csv')
#teams = pd.read_csv('MDataFiles_Stage1/MTeams.csv')
#cities = pd.read_csv('MDataFiles_Stage1/Cities.csv')
#reg_szn = pd.read_csv('MDataFiles_Stage1/MRegularSeasonCompactResults.csv')
#reg_szn_games = pd.read_csv('MDataFiles_Stage1/MRegularSeasonDetailedResults.csv')
#conferences = pd.read_csv('MDataFiles_Stage1/Conferences.csv')
#conference_tourney = pd.read_csv('MDataFiles_Stage1/MConferenceTourneyGames.csv')
#seed_slots = pd.read_csv('MDataFiles_Stage1/MNCAATourneySeedRoundSlots.csv.csv')
#seeds = pd.read_csv('MDataFiles_Stage1/MNCAATourneySeeds.csv')
#coaches = pd.read_csv('MDataFiles_Stage1/MTeamCoaches.csv.csv')
#tourney_results = pd.read_csv('MDataFiles_Stage1/MNCAATourneyDetailedResults.csv')
#reg_szn = pd.read_csv('MDataFiles_Stage2/MRegularSeasonDetailedResults.csv')
#dataset_two = pd.read_csv('MDataFiles_Stage2/MRegularSeasonDetailedResults.csv')

#twenty_one_results = dataset_two[dataset_two.get('Season')==2021]

MRSCResults = pd.read_csv('MDataFiles_Stage2/MRegularSeasonCompactResults.csv')


A_w = MRSCResults[MRSCResults.WLoc == 'A']\
    .groupby(['Season','WTeamID'])['WTeamID'].count().to_frame()\
    .rename(columns={"WTeamID": "win_A"})

print(A_w)




#print(twenty_one_results)

"""
reg_szn_games = reg_szn_games.groupby(['Season', 'WTeamID']).mean()

print(tourney_results)



def regression(X, y):
    #normal equations to find each feature's weight
    x = np.matmul(np.transpose(X), X)
    y = np.matmul(np.transpose(X), y)
    theta = tuple(np.linalg.solve(x, y))
    return theta




hypothesis_vec = []
design_matrix = []
features = []

for i in range(tourney_results.shape[0]):
    hypothesis_vec.append(tourney_results.get('WScore').iloc[i])
    for j in reg_szn_games.loc[tourney_results.iloc[i].get('Season'), tourney_results.iloc[i].get('WTeamID')]:
        features.append(j)
    design_matrix.append(features)
    features = []
for i in range(tourney_results.shape[0]):
    hypothesis_vec.append(tourney_results.get('LScore').iloc[i])
    for j in reg_szn_games.loc[tourney_results.iloc[i].get('Season'), tourney_results.iloc[i].get('LTeamID')]:
        features.append(j)
    design_matrix.append(features)
    features = []


predictions = regression(design_matrix, hypothesis_vec)

print(predictions)

"""

def predict(team, opponent):
    """returns predicted points"""
