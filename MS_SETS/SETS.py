#create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set2.add(8)
set1.add(9)
print('set1 has'+ str(len(set1))+ 'elements')

#union of two sets
union_result = set1.union(set2)
print('union:',union_result)

#intersection of two sets
intersection_result = set1.intersection(set2)
print('intersection: ',intersection_result)

#difference betwee two sets (elements in set1 but not in set2)
difference_result = set1.difference(set2)
print('difference: ',difference_result)

#symmetric difference (elements in either set1 or set2, but not in both)
symmetric_difference_result = set1.symmetric_difference(set2)
print("symmetric:", symmetric_difference_result)

#check if set1 is a subset of set2
is_subset = set1.issubset(set2)
print("is set1 a subset of set2?", is_subset)

#check if set1 is a superset of set2
is_superset = set1.issuperset(set2)
print("is set1 a superset of set2? ", is_superset)

