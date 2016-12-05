import hashlib

input = "ffykfhsq"
found = 0
i = 0
keylist = ['?','?','?','?','?','?','?','?']

while found < 8:
    code = input + str(i)
    hashout = hashlib.md5(code.encode('utf-8')).hexdigest()
    
    if hashout[:5] == '00000':
        if hashout[5] in ['0','1','2','3','4','5','6','7'] and keylist[int(hashout[5])] == '?':
            keylist[int(hashout[5])] = hashout[6]
            print("found one at : " + code)
            print("hash is: " + hashout)
            print("Current password is: ")
            print(keylist)
            found += 1
    i += 1
    
print(keylist)
