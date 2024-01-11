def print_items(n):
    for i in range(n):
        # O(n) since loop runs n times.
        # print(i) 
        for j in range(n):
        # O(n^2) since, inner loop runs n times for each iteration of outer loop.
            print(i, j)
    # O(n) outside for loop, inferior to O(n^2), so dropped for final time complexitiy of function.
    for k in range(n):
        print(k)

def add_items(n):
    return n+n

#def diff_input_print_items(a, b):
    # O(a)
    for i in range(a):
        print(i)
    # O(b)
    for j in range(b):
        print(j)

    # Total = O(a + b) and not O(n)
    # If they were nested, it will be O(a*b)
    
myList = [13, 14, 6, 7]
# Append in List is O(1) since no re-indexing is NOT required when adding at the back.
myList.append(20)
myList.append(35)
myList.append(45)
# Pop in List is O(1) since no re-indexing is NOT required when adding at the back.
myList.pop()
# Insert in list at any other index is O(n) since re-indexing is required.
myList.insert(1, 100)
# Remove in list at any other index is O(n) since re-indexing is required.
myList.remove(20)
# List also has O(1) in index-based access.
myList[0] = 2
for i in range(len(myList)):
    print(myList[i])
# print_items(10)
#add_items(5)



