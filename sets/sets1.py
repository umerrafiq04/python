set1={1,2,3,4,5,6,7,8}
set2={6,7,8,9,10}
# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.add(77))
# print(set1.difference(set2))
# set3=set1.copy()
# set3=set1.difference_update(set2)
set3=set1.isdisjoint(set2)
# set1.add(334)
print(set3)
# print(set1)
