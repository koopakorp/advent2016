import hashlib

input = "ffykfhsq"
found = 0
i = 0
keylist = []

while found < 8:
    code = input + str(i)
    hashout = hashlib.md5(code.encode('utf-8')).hexdigest()
    #print(hashout)
    
    if hashout[:5] == '00000':
        print("found one at : " + code)
        print("hash is: " + hashout)
        found += 1
        keylist.append(hashout[5])
    i += 1
    
print(keylist)
