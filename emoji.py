emo={"sad":"😞","happy":"😎","angry":"😤","love":"😘"}
res=[]
str=input("enter your emotion")

for word in str.split(" "):
    if word in emo:
        res.append(emo[word])
    else:
        res.append(" "+word)
print(" ".join(res))

