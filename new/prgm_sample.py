"""framework={'name':'django','rating':4,'language':'python'}

if 'rating' in framework:
    framework['rating']+=1
else:
    framework['rating']=1
print(framework)



framework['architecture']='mvt'
print(framework)"""




"""word='hai hello hai hello hai'
txt=word.split(' ')
print(txt)
word_count={}

for w in txt:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1

print(word_count)
print(max(word_count,key=lambda k:word_count.get(k)))"""



#pattern='ABAAB'
#1st rec char
#most rec char


pattern='ABAAB'
l=[]
for i in pattern:
    l.append(i)

word_count={}

for w in l:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1

print("Most Recursive Character:",max(word_count,key=lambda k:word_count.get(k)))


