startingYear = 1950
k = [0.2, 0.2, 0.2, 0.2, 0.2]
lengthyYear = len(k)
pop = 50
years = range(startingYear, startingYear + 50)
d = dict(zip(years, k))

#print(d)

for year in range(lengthyYear):
    print(startingYear + year)
    print(d[startingYear + year] * 50)

#one child


#two children

    

##friendships = [(0,1), (0,2), (1,2), (2,3)]
##
##for user in users:
##    user["friends"] = []
##
##for i, j in friendships:
##    # this is a comment sign
##    users[i]["friends"].append(users[j])
##    users[j]["friends"].append(users[i])
