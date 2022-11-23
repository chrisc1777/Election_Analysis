#voting list
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

#add new county "El Paso" and registered vorters, 461149 to second position in voting_data
voting_data.insert(1, {"county" : "El Paso", "registered_voters": 461149})

#Remove “Arapahoe” and its registered voters from voting_data. 
voting_data.pop(0)
#print(voting_data)


#Make “Denver” and its registered voters the third item in voting_data, 
# but keep “Jefferson” and its registered voters as the second item.   
voting_data[2] = {"county":"Denver", "registered_voters": 463353}
voting_data[1] = {"county":"Jefferson", "registered_voters": 432438}
print(voting_data)

#Add “Arapahoe” and its registered voters to voting_data.
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

#for loop dictionary iteration
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)