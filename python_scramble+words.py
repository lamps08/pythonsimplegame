
# coding: utf-8

# In[1]:

with open("C:/Users/lamps08/Downloads/words.txt", 'r' ) as f:
    r = f.read()
    #print (type(r))
    t = r.split("\n")
    lst1 = []
    lst2 = []
    for q in t :
        w = q.split(":")[0]
        t  = q.split(":")[1]
        lst1.append(w)
        lst2.append(t)


# In[2]:

print (lst1)


# In[3]:

import random
rnd_lst = []
for key in lst1:
    s = "".join(random.sample(key, len(key)))
    rnd_lst.append(s)
t = (len(rnd_lst)-1)


# In[10]:

str2 = str()
str3 = str()
while (str2 != "no" ):
    from random import randint
    i = randint(0,t)
    #print (i)
    print ("\nThe word is",rnd_lst[i])
    str1 = input("Unscramble the letters to form a word.\n\nType '?' for the meaning of the unscrambled word\n\n")

    if str1 == lst1[i]:
        print ('correct')
        str2 = input("do you want to continue\n")
    while( str1 == "?" ):
        print ("the word means:",lst2[i])
        print (rnd_lst[i])
        str1 = input("guess the word :")
        if str1 == lst1[i]:
            print ('correct')
            str2 =  input("do you want to continue\n")
        elif str1 != '?' and str2!= 'no':
            print ('wrong')
            str2 = input("do you want to continue\n")
            
    else :
        #str2 = 'no'
        if str1 != lst1[i] :
            print ('wrong')
            str2 = input("do you want to continue\n")   
        elif str2 != 'no' and str2 != 'yes':
            str2 = input("do you want to continue\n")            
        #else :
          #  str2 = input("do you want to continue\n")
        



    
    
    


# In[5]:

from random import randint
print(randint(0, 11))


# In[ ]:




# In[ ]:



