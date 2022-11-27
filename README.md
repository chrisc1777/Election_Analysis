# Election_Analysis

## Overview of Election Audit:
A Python script was executed to process the candidate election results for the election commission of Colorado. The commission requested three new tasks in retrieving a voter turnout for each county, the percentage of votes for each county, and the county with the highest turnout.

## Election Audit Results
- How many votes were cast in this congressional election?
    There was a total of 369,711 votes in this election.

- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
    Jefferson county had a total of 38,855 votes making up 10.5%.
    Denver county had a total of 306,055 votes making up 82.8%.
    Arapahoe county had a total of 24,801 votes making up 6.7%.

- Which county had the largest number of votes?
    The largest turnout was Denver county with 306,055 votes and a percentage of 82.8%.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
    Charles Casper Stockham received 85,213 votes making up 23% of the votes.
    Diana DeGette received 272,892 votes making up 73.8% of the votes.
    Raymon Anthony Doane received 11,606 votes making up 3.1% of the votes.

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
    Candidate Diana DeGette won the election with a total of 272,892 votes making up 73.8%. 
    
## Election-Audit Summary
This Python script can be used in the future by modifying the list for any type of election using the list variable "county_list = []." If the dataset has more fields, for example, "states" in a federal poll can be analyzed by changing the extraction variable "= row[2]."