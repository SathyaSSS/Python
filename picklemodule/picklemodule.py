# python data =====>>>>>> byte code

import pickle
d={'a':[1,'sathya'],'b':[2,'python']}
with open('m1.pkl','wb') as fobj:
    content = pickle.dumps(d)
    fobj.write(content)

with open('m1.pkl','rb') as fobj:
    pythobj=pickle.load(fobj)
    print(pythobj)





#byte code ====>>>> python data

# import pickle
# with open('p1.pkl','wb') as fobj:
#     pickle.dump(d, fobj)

# with open('p1.pkl','rb') as fobj:
#     pythobj = pickle.load(fobj)
#     print(pythobj)
