import os
import csv
from collections import Counter

BOB = os.path.join("/Users/matthewpetroff/WORKSPACE/unc/02-homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")
#print("good path")

#with open(csv, 'r') as csvfile:
with open(BOB) as csvfile:

    #reader open
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)

    #Candidate list
    voter_count = Counter()
    Candidates = []
    Percent = []
    Winna = []


    for row in reader:
        Candidates.append(row[2])

    c_votes = len(Candidates)

    for name in Candidates:
        voter_count[name] += 1

    winner = max(zip(voter_count.values(), voter_count.keys())) # Defining a winner
    names = tuple(voter_count.keys())
    votes = tuple(voter_count.values())


    Winna.append('Election Results')
    Winna.append('-----------------------')
    Winna.append('Total Votes: ' + str(c_votes))
    Winna.append('-----------------------')

    for n in range(len(names)):
        Winna.append(names[n] + ': '  + '(' + str(votes[n]) + ')')

    Winna.append('-----------------------')
    Winna.append('Winner: ' + winner[1])
    Winna.append('-----------------------')

    print("\n".join((Winna)))






















#Ignore ----------------------------------------------------
#
#    #The total votes cast
#    data = list(reader)
#    row_count = len(data)
#    print("Total Votes:" ,(row_count - 1))
#
    #List of canidates who recived votes
#with open(BOB) as csvfile:
#    DataCaptured = csv.reader(csvfile)
#    Candidate_List = []
#    for row in DataCaptured:
#        if row[2] not in Candidate_List:
#            Candidate_List.append(row[2])
#    Candidate_List.remove('Candidate')
#    print(Candidate_List)
#    from collections import Counter
#    print Counter(Candidate_List)
#    myarray = np.asarray(Candidate_List)
#    #print(myarray)
#    K = myarray[0]
#    C = myarray[1]
#    L = myarray[2]
#    O = myarray[3]



#    ]
#    dictOfCand = { i : Candidate_List[i] for i in range(0, len(Candidate_List) ) }
#    #print (dictOfWords)
#    for "0" in dictOfCand:
#        characters[character] = characters.get(character, 0) + 1

#print(characters)
