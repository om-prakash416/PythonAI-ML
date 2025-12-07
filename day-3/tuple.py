tup =(2,233,5,6,3,32,2,5,2)

print(tup[1])
print(tup[2:4])
print(tup[-2:])
print("Length of tuple is ", len(tup))
print(tup.count(2))
print(tup.index(2))

#;loops on tuple

sum =0
for val in tup:
    print(val)
    sum += val
    
print(f"sum of tuple is {sum}")