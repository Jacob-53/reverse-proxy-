python3 <<EOF
import requests
import csv
import time
import os

res = requests.get("http://localhost:8949/nginx_status")

def res_list(text):
    return text.replace("Active connections","ac").replace(":", " ").replace("server ","").replace("\n", "").lower().split()

def list_to_dict(lst):
    result = {}
    for i in range(len(lst)):
        if not lst[i].isdigit():
            if lst[i] == "ac":
                result[lst[i]]=int(lst[i+1])
            elif lst[i] == "reading":
                result[lst[i]]=int(lst[i+1])
            elif lst[i] == "writing":
                result[lst[i]]=int(lst[i+1])
            elif lst[i] == "waiting":
                result[lst[i]]=int(lst[i+1])
            elif lst[i] == "accepts":
                result[lst[i]]=int(lst[i+3])
            elif lst[i] == "handled":
                result[lst[i]]=int(lst[i+3])
            elif lst[i] == "requests":
                result[lst[i]]=int(lst[i+3])
    return result

csv_file = "nginx_status.csv"

if not os.path.exists(csv_file):
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "ac", "accepts", "handled", "requests", "reading", "writing", "waiting"])

while True:
    try:
        res = requests.get("http://localhost:8949/nginx_status")
        res_text = res.text.strip()

        res_list_output = res_list(res_text)
        result_dict = list_to_dict(res_list_output)

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        with open(csv_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                timestamp,
                result_dict.get("ac", 0),
                result_dict.get("accepts", 0),
                result_dict.get("handled", 0),
                result_dict.get("requests", 0),
                result_dict.get("reading", 0),
                result_dict.get("writing", 0),
                result_dict.get("waiting", 0)
            ])

        
        time.sleep(10)  

    except Exception as e:
        print("Error:", e)
        time.sleep(10) 
EOF