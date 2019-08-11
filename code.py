# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

# Code starts here
#  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
sc_delivery = data ['innings'] [0] ['1st innings'] ['deliveries']
counterVar = 0
for rec in sc_delivery:
    for key, val in rec.items():
        if val ['batsman'] == 'SC Ganguly':
            counterVar+=1
print ('Number of Deliveries faced by Ganguly', counterVar)

#  Who was man of the match and how many runs did he scored ?

#print(data['info']['player_of_match'][0])
runsScored = 0
for foo in sc_delivery:
    for key, val in foo.items():
        if val['batsman'] == data['info']['player_of_match'][0]:
            #print('key=',key,'val=',val['runs']['batsman'])
            runsScored = runsScored+val['runs']['batsman']
print('Man of the Match was', data['info']['player_of_match'][0], 'Number of Runs Scored', runsScored)


#  Which batsman played in the first inning?
#sc_delivery = data ['innings'] [0] ['1st innings'] ['deliveries']
l1 = []
for deliveryVal in sc_delivery:
    for key, val in deliveryVal.items():
        #if val ['batsman'] not in l1:
        l1.append (val['batsman'])
            #print(l1)
print(list(set(l1)))
# Which batsman had the most no. of sixes in first inning ?
dict1 = {}
sc_delivery
for rec in sc_delivery:
    for key, val in rec.items():
        if val['runs']['batsman'] == 6:
            if val['batsman'] in dict1:
                dict1[val['batsman']] += 1
                #print(dict1)
            else:
                dict1[val['batsman']] = 1
print (dict1)
# Find the names of all players that got bowled out in the second innings.
l3=[]
SecondInn = data ['innings'][1]['2nd innings']['deliveries']
for rec in SecondInn:
    for key, val in rec.items():
        if 'wicket' in val and val ['wicket']['kind']=='bowled':
            l3.append(val['batsman'])
print(l3)

# How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
SecondInnExtras = 0
for rec in SecondInn:
    for key, val in rec.items():
        if val.get('extras'):
            SecondInnExtras += 1
#print(SecondInnExtras)

FirstInnExtras = 0
for rec in sc_delivery:
    for key, val in rec.items():
        if val.get('extras'):
            FirstInnExtras += 1
print(SecondInnExtras-FirstInnExtras)


# Code ends here


