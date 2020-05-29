
def square_numbers(nums):
    # result = []
    for i in nums:
        yield (i*i)
        # result.append(i*i)
    # return result

# my_nums = [x*x for  x  in [1,2,3,4,5]] # this comprehension is the same as square_numbers()
# print(my_nums) # [1, 4, 9, 16, 25]


my_nums = (x*x for  x  in [1,2,3,4,5])
print(my_nums) # <generator object <genexpr> at 0x7f53e0e5e360>
               # a generator retrieves each value at a time
               # not everything in one shot

print(list(my_nums)) # [1, 4, 9, 16, 25], makes the generator a list,
                     # not optimal since a generator help to save mem

# my_nums = square_numbers([1,2,3,4,5])

for num in my_nums:
    print(num)