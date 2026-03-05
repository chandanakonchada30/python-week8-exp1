#24331A05E2
#to create a list of tuples with the first element as the number and the second element as the square of the first element.
tup=(1,2,3,4,5)
lst=[(x,x**2)for x in tup]
print(lst)
