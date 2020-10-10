#!/usr/bin/env python
# coding: utf-8

import os
import csv

csvpath = os.path.join('.','Resources','election_data.csv')

csvfile=open(file=csvpath,newline='')
csvfile.close

total = 0

candidates = []
candidate_votes = {}

winner = ""
winner_count = 0

with open(file=csvpath,newline='') as election_data:
    reader=csv.DictReader(election_data)
    
    for i in reader:
        #total votes
        total = total + 1
        
        candidate_name = i["Candidate"]
        
        #adding candidates as we go
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
        
analysis_path = os.path.join('.','Analysis','election_analysis.txt')

with open(analysis_path,"w") as txt_file:
    election_results = (
    f'\nElection Results\n'
    f'-------------------------\n'
    f'Total Votes: {total}\n'
    f'-------------------------\n'
    )
    print(election_results,end="")
    
    txt_file.write(election_results)
    
    #voter percentages
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total) * 100
        
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
            
        voter_analysis = f'{candidate}: {vote_percentage:.3f}% ({votes})\n'
        print (voter_analysis,end='')
        
        txt_file.write(voter_analysis)
        
    #final winner
    winner_summary = (
        f'-------------------------\n'
        f'Winner: {winner}\n'
        f'-------------------------\n')
    print(winner_summary)
    
    txt_file.write(winner_summary)




