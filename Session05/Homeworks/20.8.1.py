str_input=input("String : ").lower()
alphabet=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
count={}
for char in str_input:
    if char in alphabet:
        
        if char in count:
            count[char]=count[char]+1
        
        else:
            count[char]=1

countkeys=sorted(count)
for key in countkeys:
    print(key,count[key])
            