"""
sets:


"""

set1 = {1, 2, 3, 4 ,5}

set2 = set([40, 50, 60, 70, 80])
set3 = {"data","the", 5,(1,1)}

print(set1)
print(set2)
print(set3)

#Sets Methods
#________________________________________________________________________
# Add() - add an element to the set
set2.add(45)
print(set2)

#________________________________________________________________________
#clear() - removes all the elements from the set

#______________________________________________________________________
#copy() - return a copy of the set


#___________________________________________________________________
#discard() - remove the specified item
print("discard")
print(set1.discard(70))

#____________________________________________________________________
#pop() - remove an random element from the set
print(set1.pop())

#_____________________________________________________________
#remove() - removes the specified element


#________________________________________________________________________
#update() - update the set with another set, or any other iterable
set1.update({1,2,3,4,50})
print(set1)


#____________________________________
#unioun() - returns a set containing the union of sets

unioun_set = set1.union(set2)
print("unioun_set:", unioun_set)

#____________________
# intersection - returns a set, that is the intersection of two or more sets

intr_set = set1.intersection(set2)
print(("intr_set:", intr_set))

#intersection update - removes the items in this set that are not present in other, specified set(s)

# set1.intersection_update(set2)
# print("set1",set1)

#difference() - returns a set containing the difference between two or more sets
#difference (A-B),(B-A)
a_b = set1.difference(set2)
b_a = set2.difference(set1)
print("a-b:",a_b)
print("b-a:",b_a)

#difference_update() - removes the items in this set that are also included in another, specified set
# print(set1)
# set1.difference_update(set2)
# print(set1)

#symmetric_difference() - returns a set with the symmetric differences of two sets
#(aub) - (anb)

symm_diff = set1.symmetric_difference(set2)
print("symm_diff",symm_diff)


#symm_diff_update() - inserts the symmetric differences from this set and another


#issubset() - returns whether another set contains this set or not
# return true if the called set is a subset of present

temp = {10,20,30}

print("set1", set1)
print("set2",set2)
print(temp.issubset(set1))
print(({50,60}.issubset(set2)))

#issuperset() - returns whether this set contains another set or not
temp = {40,10,50,20,30,5,8,9,0}

print(temp.issuperset(set1))

#isdisjioint() - returns whether two sets have a intersection or not

s1 = {10,20,30}
s2 = {40,50,60}

online_users = {"user1","user2","user5"}
premium_users = {"user3","user4", "user5"}
logged_in_users = {"user3", "user9", "user2"}

print("disjoint", s1.isdisjoint(s2))
print(logged_in_users.intersection(online_users))

print(online_users.isdisjoint(premium_users))



