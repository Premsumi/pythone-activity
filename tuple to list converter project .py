# Step 1: Define a tuple
my_tuple = (10, 20, 30, 40, 50)

# Step 2: Convert the tuple to a list
my_list = list(my_tuple)

# Step 3: Print the tuple and list
print("Original Tuple:", my_tuple)
print("Converted List:", my_list)

# Step 4: Modify the list
my_list.append(60)
print("List after appending 60:", my_list)

# Step 5: Convert back to tuple
my_new_tuple = tuple(my_list)
print("Converted Back to Tuple:", my_new_tuple)
