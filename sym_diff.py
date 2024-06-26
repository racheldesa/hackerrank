# read length of set 1
M = int(input())
# read items in set 1
a = input()
l1 = a.split()  # split the string into a list
set1 = set(map(int, l1)

# read length of set 2
N = int(input())
# read items in set 2
b = input()
l2 = b.split()  # split the string into a list
set2 = set(map(int, l2))

symmetric_diff = set1.symmetric_difference(set2)

# handle negative values
final = list(symmetric_diff).sort()

for x in final:
  print(x)
