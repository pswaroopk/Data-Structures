str1="hellello"


def pal(str1):
    k=0
    strr=""
    for i in range (len(str1)+1):
        for j in range(i, len(str1)+1):
            strr=str1[i:j]
            if strr is not "" and strr==strr[::-1]:
                k=k+1
    print(k)
pal(str1)

