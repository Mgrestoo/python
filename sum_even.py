numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
# initialise sum variables
sum_even = 0
# iterate over each number in alist
for number in numbers:
    if number % 2 == 0: #CHECKING IF A NUMBER IS EVEN
        sum_even += number

print("Sum of even numbers: ", sum_even)