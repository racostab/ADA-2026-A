ng = input().split()
n = int(ng[0])
g = ng[1]
menOrder = []
womenOrder = []
menPreferences = {}
womenPreferences = {}
for i in range(n):
  line = input().split()
  menPreferences[line[0]] = line[1:] 
  menOrder.append(line[0])

for i in range(n):
  line = input().split()
  womenPreferences[line[0]] = line[1:]
  womenOrder.append(line[0])

def getStableMatching(group1, group2):
  freePerson = list(group1.keys())
  nextPerson = {}
  nextPerson = {p:0 for p in freePerson}

  engagedPerson1 = {}
  engagedPerson2 = {}

  while(freePerson):
    #person1 = freePerson.pop(0)
    person1 = freePerson[0]
    

    if nextPerson[person1] >= n:
      freePerson.pop(0)
      continue

    person2 = group1[person1][nextPerson[person1]]
    nextPerson[person1] += 1

    if person2 not in engagedPerson2:
      engagedPerson1[person1] = person2
      engagedPerson2[person2] = person1
      freePerson.pop(0)
    else:
      currentPerson = engagedPerson2[person2]
      if group2[person2].index(person1) < group2[person2].index(currentPerson):
        engagedPerson1.pop(currentPerson, None)
        freePerson.append(currentPerson)
        engagedPerson1[person1] = person2
        engagedPerson2[person2] = person1 
        freePerson.pop(0)
      #else:
        #freePerson.append(person1)
  
  if g == 'm':
    for man in menOrder:
        print(man, engagedPerson1[man])
  else:
      for woman in womenOrder:
        print(woman, engagedPerson1[woman])

if g == 'm':
  getStableMatching(menPreferences, womenPreferences)
else:
  getStableMatching(womenPreferences, menPreferences)