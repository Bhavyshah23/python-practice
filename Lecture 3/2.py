# Write a program to check if a list contains a palindrome of elements.(Hint : Use Copy() method.)

list1 = [1, 2, 3, 2, 1]
list2 = [1, 2, 3, 4, 5]

copy_list2 = list2.copy()
copy_list2.reverse()

if (list2 == copy_list2):
    print("List 2 is a palindrome.")
else:
    print("List 2 is not a palindrome.")