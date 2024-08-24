def isUnique (word):
    freq = {}
    
    for char in word:
        if char in freq:
            freq[char] += 1
            return False
        else:
            freq[char] = 1
    
    return True


print(isUnique("Pabbi"))

# This has a O(n) time complexity, since we iterate through every single element of the word. 
# This has O(n) space complexity also, since a new hashmap is being utilised. 



# How can you solve it without a data structure ?
# Answer: Can solve using nested loops in O(n^2) time complexity. 
