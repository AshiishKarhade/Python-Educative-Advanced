from collections import Counter

counter = Counter('Superfluous')
print(counter)
print("Count of 'u' : " + str(counter['u']))

# ELEMENTS
print("Elements")
print(list(counter.elements()))

# MOST COMMON
print("2 Most Common")
print(counter.most_common(2))
print("3 Most Common : " + str(counter.most_common(3)))


