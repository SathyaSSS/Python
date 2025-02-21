#python object ====>>>> json object


# import json
# d={'a':[1,'sathya'],'b':[2,'python']}
# with open('m1.txt','w') as fobj:
#     content = json.dumps(d,indent=4)
#     fobj.write(content)

# D={'name':'sathya','age':22,'l':[1,2,3]}
# with open('m2.txt','w') as fobj:
#     json.dump(D,fobj,indent=4)



# json object ====>>>> python object


import json
d = '{"car":["BMW","AUDI","GTR"],"bike":["RX","RE","MT"]}'
with open('j1.json','w') as fobj:
    fobj.write(d)

with open('j1.json','r') as fobj:
    content = fobj.read()
    pythobj = json.loads(content)
    print(pythobj)
    

D='{"ipl":["MI","SRH","GT"],"cap":["Hitman","Warner","Kane mams"]}'
with open('j2.json','w') as fobj:
    fobj.write(D)

with open('j2.json','r') as fobj:
    pythobj=json.load(fobj)
    print(pythobj)