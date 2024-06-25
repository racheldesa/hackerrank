# read total number of stamps to be entered
N = int(input())

# populate set
stamps_set = set(input() for i in range(N-1))

# print set length (number of unique values)
print(len(stamps_set))
