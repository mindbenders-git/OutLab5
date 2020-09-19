import operator

n =int(input())
match = []
inputs = []
outputDict = {}
dictInValue = {}
totalPlayers = {}
for i in range(n):
	a = input()
	inputs.append(a)
	
for a in inputs:	
	a = a.split(":")
	key = a[0]
	value = a[1]
	players = value.split(",")
	for player in players:
		player = player.split("-")
		dictInValue[player[0]] = int(player[1])
		if player[0] in totalPlayers:
			totalPlayers[player[0]] = int(totalPlayers[player[0]]) + int(player[1])
		else:
			totalPlayers[player[0]] = int(player[1])
	outputDict[key] = dictInValue
	dictInValue = {}

print(outputDict)
totalPlayers = dict(sorted(totalPlayers.items(), key=lambda x: x[1],reverse=True))

count = 0
finalPlayers = {}
helperDict = {}
for k,v in totalPlayers.items():
	if count==0:
		prevValue = v
		helperDict[k] = v
		count+=1
		continue
	if prevValue != v:
		helperDict = dict(sorted(helperDict.items(), reverse=True))
		finalPlayers.update(helperDict)
		helperDict = {}
		helperDict[k] = v;
		prevValue = v
	else:
		helperDict[k] = v;
		

helperDict = dict(sorted(helperDict.items(), reverse=True))
finalPlayers.update(helperDict)
match = [(k, v) for k, v in finalPlayers.items()] 


print(match)
