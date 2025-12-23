def GiveResult(s1,s2,s3):
    if(s1<s2):
        print("good")
    elif(s1>=s2 and s1<=s3):
        print("best")
    else:
        print("can do better")

s1=int(input("s1 : "))
s2=int(input("s2 : "))
s3=int(input("s3 : "))
GiveResult(s1,s2,s3)


