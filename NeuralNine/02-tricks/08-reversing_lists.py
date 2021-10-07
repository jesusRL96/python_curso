values = [1,2,4,5,6,8,10]

rev_list = []
for index, value in enumerate(values):
    rev_list.append(values[len(values) - index - 1])
print(rev_list)

# 
values.reverse()    # save the values 
print(values)
values = [1,2,4,5,6,8,10]
print(list(reversed(values)))  # doesn't affect the values
print(values)
print(values[::-1])            # doesn't affect the values