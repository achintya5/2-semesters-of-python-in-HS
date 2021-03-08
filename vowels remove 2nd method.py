s = input("Enter a string: ")
v = "aeiouAEIOU"
if v not in s:
    print(s)
    print(1)
else:
    for i in (0,len(s)):
        if s[n]==v:
            s1 = s[0:n-1]
            s2 = s[n+1:len(s)]
            sf = s1 + s2
print(sf)
