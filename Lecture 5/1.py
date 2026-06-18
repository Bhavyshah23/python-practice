# print number 1 to 100
# i = 1;

# while i <= 100:
#     print(i)
#     i = i+1;

# print number 100 to 1

# i = 100;

# while i >= 1:
#     print(i)
#     i =  i - 1;

# Print the multiplication table of a number
# i= 1;
# n = int(input("Enter a number: "));
# while i <= 10:
#     print(n*i);
#     i = i + 1;

# Print the element of the list using while loop

# numbers= [1,4,9,16,25,36,49,64,81,100];

# i = 0;
# while i < len(numbers):
#     print(numbers[i]);
#     i = i + 1;

# Search for a number x in this tuple using loop.

numbers = (1,4,9,16,25,36,49,64,81,100);

i = 0;

x = int(input("Enter a number to search: "));
while i < len(numbers):
    if numbers[i] == x:
        print("Found", x);
        break;
    i = i + 1;