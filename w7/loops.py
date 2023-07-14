#!/usr/bin/env python3




# (pythonic) -> writing python that looks like python

our_list = ["alpha", "beta", "gamma"]
# for i in range(len(our_list)):
#     # print(i)
#     print(our_list[i])

# better
# for elem in our_list:
#     print(elem)

# suppose we needed the index
# for i in range(len(our_list)):
#     # print(i)
#     print(f"{i} --> {our_list[i]}")

# our_list = ["alpha", "beta", "gamma"]
# enumerate(our_list) -> (0,"alpha"), (1,"beta"),...

# better
# for (index,elem) in enumerate(our_list): 
#     print (f"{index} --> {elem}")

# for i in range(len(our_list), -1, -1)

#better
# for elem in reversed(our_list):
#     print(elem)

our_dict = {"alpha": 1, "beta":2, "gamma": 3}

# our_dict["alpha"] += 1
# dont mutate while iterating!
# for k in our_dict:
#     print(k)

# # creates a 'copy' of keys
# for k in our_dict.keys():
#     print(k) 

# for k in our_dict.keys():
#     print(f"{k} --> {our_dict[k]}")

# our_dict.items() = (alpha,1) , ...

# better
# for (key, val) in our_dict.items():
#     print(f"{key} --> {val}")


our_list = ["alpha", "beta", "gamma", "alpha", "alpha", "beta"]
# counting
# return {"alpha": 3}
counts = dict()

# for elem in our_list:
#     if elem in counts.keys():
#         counts[elem] += 1
#     else:
#         counts[elem] = 1

# better
for elem in our_list:
    counts[elem] = counts.get(elem, 0) + 1

# 2 other better ways:
#   - default_dict(int)
#   - Counter (import collections.Counter)

print(counts)

# guido --> dictator