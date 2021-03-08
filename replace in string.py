#accept string and character, create new string with no charcters
#which were provided by user
s=input("Enter a string here: ")
c=input("Enter a single character here: ")
for i in s:
    if i==c:
        b=s.find(i)
        n=s.replace(s[b],"")
print(n)
    
