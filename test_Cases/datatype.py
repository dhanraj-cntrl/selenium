# Reverse a string.
st = "Welcome"
rev=""
for i in st:
    rev = i + rev
print(rev)

print(st[::-1])
# Reverse each word in a string.
st = "Dhanraj Lahu Rajmane"
re=[]
for i in st.split():
    if i == "Lahu":
        re.append(i)
    else:
        re.append(i[::-1])
print(" ".join(re))

print(" ".join(i[::-1]for i in st.split()))
# Reverse the order of words in a string.
# Check whether a string is a palindrome.
st = "level"
if st[::-1]==st:
    print("palindrome")
# Find the length of a string without using len().

# Count the occurrence of a particular character in a string.
st = "Welcome to India"
freq={}
for i in st:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

# Count the occurrence of every character in a string.
st = "Welcome to India"
freq={}
for i in st.split():
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

# Find duplicate characters in a string.
# Find the first non-repeated character in a string.
# Find the first repeated character in a string.
# Check whether two strings are anagrams.
# Remove duplicate characters from a string.
# Find vowels and consonants in a string.
st = "Welcome"
vwls=[]
cntw=0
for i in st:
    if i.lower() in "aeiou":
        vwls.append(i)
        cntw += 1
print(vwls)
print(cntw)
# Remove spaces from a string.

# Count the number of words in a string.
# Find the longest word in a string.
st = "Dhanraj Lahu Rajmane"
longest=""
for i in st.split():
    if len(i) > len(longest):
        longest = i
print(longest)
# Find the shortest word in a string.

# Check whether a string contains only digits.
st = "asdfgh123456asdfvgbhn1234"
cntw=0
for i in st:
    if i.isdigit():
        cntw += 1
print(cntw)
#############################################
# Find the largest number in a list.
ilist = [12,22,2222,23,34,444,4555]
largest=ilist[0]
sec=ilist[0]
for i in ilist:
    if i > largest:
        sec = largest
        largest = i
    elif i > sec and i != largest:
        sec = i
print(largest)
print(sec)
# Find the second-largest number in a list.

# Find the second-smallest number in a list.
# Reverse a list without using reverse().
ilist = [12,22,2222,23,34,444,4555]

rev=[]
for i in ilist:
    rev = [i] +rev
print(rev)

# Remove duplicates from a list.
ilist = [12,22,2222,23,34,23,34,444,4555]
org=[]
dupl=[]
for i in ilist:
    if i not in org:
        org.append(i)
    else:
        dupl.append(i)
print(org)
print(dupl)

# Find common elements between two lists.
l1= [1,2,3]
l2= [3,4,5]
cmn=[]
for i in l1:
    if i in l2:
        cmn.append(i)
print(cmn)

# Merge two lists.# Sort a list in descending order.
# # Move all zeros to the end of a list.
# # Move all zeros to the beginning of a list.
l1 = [1,2,3,3,4,4,5,6,0,0,0,2,3,4]
ze=[]
nonze=[]
for i in l1:
    if i == 0 :
        ze.append(i)
    else:
        nonze.append(i)
re=ze+nonze
print(re)

# Sort a list without using sort().
ilist = [12,22,2222,23,34,444,4555]

for i in range(len(ilist)):
    for j in range(i+1,len(ilist)):
        if ilist[i] > ilist [j]:
            ilist[i],ilist[j] = ilist[j],ilist[i]
print(ilist)
# Sort a list in ascending order.

# Separate even and odd numbers from a list.
# Find the sum of all elements in a list.

ilist = [12,22,2222,23,34,444,4555]
print(list(filter(lambda x:x%2==0,ilist)))
print(list(filter(lambda x:x%2!=0,ilist)))
from functools import reduce
print(reduce(lambda x,y :x+y,ilist))

# Find the frequency of each element in a list.
# Find elements occurring more than once.
# Find elements occurring exactly once.
ilist = [12,22,2222,23,34,34,34,444,4555]

def is_freq():
    freq={}
    for i in ilist:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq
ob1=is_freq()
print(ob1)

for i in ob1:
    if ob1[i] > 1:
        print(i)

# Check whether a number is even or odd. -covered
# Check whether a number is prime.
# Print prime numbers from 1 to 100.

prm=[]
for i in range(100):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        prm.append(i)
print(prm)
# Find the factorial of a number.
# Find factorial using recursion.

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial(n-1)
ob1=factorial(5)
print(ob1)

# Print Fibonacci series.
n=10
a = 0
b = 1
for i in range(n):
    print(a,end=" ")
    a,b =b, a + b
# Find the nth Fibonacci number.
# Find the sum of digits of a number. -reduce
# Count the digits in a number. -done

# Swap two numbers using a third variable.
# Swap two numbers without using a third variable

ilist = [12,22,2222,23,34,4444,4555]

temp = ilist[2]
ilist[2] = ilist[5]
ilist[5] = temp
print(ilist)

#Print a pyramid pattern.
row=5
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()

