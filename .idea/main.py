import json

print("hello world\n")

f = open('venv/leaders.json')

data = json.load(f)



for i in data['Province List']:
    print(i['Province'])
    for j in i['Settlements']:
        print(j)#


#for i in data['leaders']:
#    print(i)
#test commit
f.close()
