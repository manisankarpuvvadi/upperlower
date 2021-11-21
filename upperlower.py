def upper_lower(s1):
    u=0
    l=0
    for i in s1:
        if i.isupper():
            u=u+1
        if i.islower():
            l=l+1
    print("No. of Upper case characters :",u)
    print("No. of Lower case Characters :",l)
s="The quick Brow Fox"
upper_lower(s)
