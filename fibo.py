import sys
# get missing numbers between 1 and 10000

inline = sys.stdin.readline()

# Get input as chars, convert to integers
characters = inline.split()

integers = []
for x in characters:
    integers.append(int(x))

fibset = []

def fib(n):
   if n == 1:
      return 1
   elif n == 0:
      return 0
   else:
      return fib(n-1) + fib(n-2)

# Generates fibonacci numbers to check against
for n in range(1,20):
    fibset.append(fib(n))

# print the matches using lists
print ("The Fibonacci numbers are ",(list(set(fibset) & set(integers))))

#convert lists to sets
fibsetlist = set(fibset)
integersset = set(integers)

# print the matches and differences using sets
#print fibsetlist.symmetric_difference(integersset)
print ("The intersection of the sets are ", fibsetlist.intersection(integersset))

print map(fib,range(1,6))

# Print combinations of the 2 lists
combs = []
for x in integers:
    for y in fibset:
        if x!= y:
            combs.append((x, y))
print combs
