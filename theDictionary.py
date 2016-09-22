'''
Created on Sep 16, 2016

@author: kiwis
'''

f = open('dic.txt', 'r')
dic = []
for word in f.read().split():
    if len(word) > 4:
        dic.append(word)
        
#print(dic[random.randint(0,len(dic))])

#print()          
            