from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
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
    #result = [i+j for i,j in zip(a,b)]
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


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
