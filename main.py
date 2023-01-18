#1) Use enumerate function which adds a count to iterables.

my_list = [1,-3,13,4,9,0]

#Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object
for i in enumerate(my_list):
    print(i)

for ind,num in enumerate(my_list):
    print(ind,num)


#2) Use list comprehension instead of raw loops

#Let's make a list of square of even numbers between 1 and 10

#naive way
even_squares = []
for i in range(10):
    if i%2 == 0:
        even_squares.append(i*i)

print(even_squares)
#efficient way
even_squares = [i*i for i in range(10) if i%2==0]
print(even_squares)



#3) Sort complex iterables with sorted()
data = [1,3,-4,5,0]
sorted_data = sorted(data,reverse=True)
print(sorted_data)
