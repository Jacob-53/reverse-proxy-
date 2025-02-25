import time
import random
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

import time
import random

def add_large_arrays():
    N = 10**6  # 100만 개 요소
    la, lb = gen_r_sample(N)
    # 랜덤한 1차원 배열 2개 생성

    # 실행 시간 측정 시작
    start_time = time.time()
    
    # 요소별 덧셈
    result=[]
    for i in range(len(la)):
            result.append(la[i]+lb[i])
    # 실행 시간 측정 종료
    end_time = time.time()
    
    # 수행 시간 리턴
    cal_time = end_time - start_time
    return cal_time

def gen_r_sample(N):
    la = random.sample(range(1,N+1),N)
    lb = random.sample(range(1,N+1),N)
    return la,lb



import time
import random

def add_large_arrays_choice():
    return add_arrays()

def add_arrays(N,fun):
    array_start_time = time.time()
    N = 10**6  # 100만 개 요소
    a,b = gen_arrays_choice(N)
    array_end_time = time.time()
    
    add_start_time = time.time()
    
    # 요소별 덧셈
    result=[]
    for x,y in zip(a,b):
        result.append(x+y)
    # 실행 시간 측정 종료
    add_end_time = time.time()
    
    
    array_creation_time = array_end_time - array_start_time
    execution_time = add_end_time - add_start_time
    return array_creation_time, execution_time

def gen_arrays_choice(N):
    a = random.choices(range(101),k=N)
    b = random.choices(range(101),k=N)
    return a,b

def d_list(fun):
    distinct_list = set(fun())
    return distinct_list


a= d_list(add_large_arrays_choice)
print(a)