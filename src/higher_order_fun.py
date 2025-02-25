import time

def square(x):
    return x ** 2
def double(x):
    return x * 2

#print(nums)
#def num_square(nums):
    #start_time = time.time()
    #return ([i**2 for i in nums])
    #print([square(x) for x in nums])
    #end_time = time.time()
    #print(end_time - start_time)

#result = num_squqre(nums)
#print(result)

#def num_double(nums):
    #return ([i*2 for i in nums])
#result = num_double(nums)
#print(result)


def num_cal(nums,fun):
    start_time = time.time()
    result = ([fun(x) for x in nums])
    end_time = time.time()
    print(end_time - start_time)
    return result

nums = [1,2,3,4,5]
test1= num_cal(nums,square)
print(test1)