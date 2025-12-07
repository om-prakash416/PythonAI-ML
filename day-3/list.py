marks =[99,89,100,65,92]

print(marks[1])
print(marks[5:])
print(marks[2:4])


nums =[1,2,33,34]
print(nums)
nums.append(5)
print(nums)
nums.insert(2,100)
print(nums)
nums.remove(100)
print(nums)
nums.pop()
print(nums)
nums.sort()
print(nums) 
nums.sort( reverse=True)
print(nums) 
nums.reverse()
print(nums) 

#loops on list

nums =[1,2,33,34,45,56,67 ,78,89,90]

x = 67
idx = 0
for val in nums:
    if val == x:
        print(f"{x} at found at index ", idx)
        break
    idx += 1
  