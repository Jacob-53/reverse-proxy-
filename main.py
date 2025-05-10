from typing import Union
from fastapi import FastAPI
import random
import time
app = FastAPI()

N = 10**4  # 100만 개 요소

@app.get("/")
def read_root():
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    #result = [i+j for i,j in zip(a,b)]
    result=[]
    for i in range(len(a)):
            result.append(a[i]+b[i])
    
    return {"Hello": result }

@app.get("/two-dimensional-array")
def two_dimensional_array():
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    b = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
   
    resulta=[]
    result=[]
    for i in range(len(a)):
        for j in range(len(a)):
            resulta.append(a[i][j]+b[i][j])
            
    resultb=resulta[0:3]
    resultc=resulta[3:6]
    resultd=resulta[6:]
    result.append(resultb)
    result.append(resultc)
    result.append(resultd)
    
    return {"Hello": result }

@app.get("/add-large-arrays")
def add_large_arrays():
    
    la = random.sample(range(1,N+1),N)
    lb = random.sample(range(1,N+1),N)
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
    return {"execution_time": end_time - start_time}


@app.get("/add-large-arrays-choice")
def add_large_arrays_choice():
    array_start_time = time.time()
    la = random.choices(range(1,N+1),k=N)
    lb = random.choices(range(1,N+1),k=N)
    array_end_time = time.time()
    
    add_start_time = time.time()
    
    # 요소별 덧셈
    result=[]
    for i in range(len(la)):
            result.append(la[i]+lb[i])
    # 실행 시간 측정 종료
    add_end_time = time.time()
    
    # 수행 시간 리턴
    return {
        "array_creation_time" : array_end_time - array_start_time,
        "execution_time": add_end_time - add_start_time
        }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
