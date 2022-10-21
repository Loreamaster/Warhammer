import json

print("hello world\n")

f = open('provinceList.json')

data = json.load(f)



for i in data['Province List']:
    print(i['Province'])
    for j in i['Settlements']:
        print(j)
    print('\n')


#for i in data['leaders']:
#    print(i)
#test commit
f.close()
