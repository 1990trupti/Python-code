"""Tuple:
     very similar to lists
     Index based opertaions allowed
     Holds homogeneous + hetrogeneous data elements( for
     immutable cannot be changed
     sequence order is preserved
     Duplicated are aloowed
     multiple None Type Allowed

Inbuilt methods: count, index

how to use:
reference_name = (val1, val2, val3, val4)
reference_name = tuple([val1,val2,val3])


e.g:
weakdays =("Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturady","Sunday")

vowels = tuple(['a','e','i','o','u'])

Nesting tuples is possible """

#_____________________________________

weakdays =("Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturady","Sunday")
print(weakdays)

vowels = tuple(['a','e','i','o','u'])
print(vowels)

#__________________________
#count - return count of given element
print(weakdays.count("sunday"))


#index - return index of element
print(weakdays.index("Thursday"))

print(weakdays[5])
print(weakdays[-2])
# print(len(tuple))
print(len(weakdays))
