from collections import Counter
mylist = [1,3,4,5,3,25,64,3,2,2,21,2,34,23,2,321,1,2,1,1,3,42]
current_max = 0
current_value = None
for x in mylist:
    if mylist.count(x) > current_max:
        current_max = mylist.count(x)
        current_value = x
print(f"Value: {current_value}, Ocurrences: {current_max}")

counter = Counter(mylist)
value, frequency = counter.most_common(1)[0]    

print(f"Value: {value}, Ocurrences: {frequency}")
# using max
value = max(set(mylist), key=mylist.count)
frequency = mylist.count(value)
print(f"Value: {value}, Ocurrences: {frequency}")