#!/usr/bin/env python3

import json
import os
import subprocess
import sys
import time
import random
import numpy as np
from datetime import datetime
import csv
import pandas as pd

if '-h' in sys.argv or '--help' in sys.argv:
    print('usage:', file=sys.stderr)
    print('echo GET http://localhost:8080/ | %s' % sys.argv[0], file=sys.stderr)
    sys.exit(1)

target = sys.stdin.read().strip()


data_path = './get_requests_july_res.xlsx'
data_df = pd.read_excel(data_path)
data_series = data_df['GET Requests Count'].values

print(data_series)
print(len(data_series))
print(data_series[0])
print(data_series[1])
print(data_series[2])

# print(new_time_list)
# Re-defining the given data
data = {
    "latencies": {
        "total": 836104751293,
        "mean": 24591316214,
        "50th": 26195544451,
        "90th": 29355367720,
        "95th": 29669880644,
        "99th": 29916766613,
        "max": 29916766613,
        "min": 1670014433
    },
    "bytes_in": {"total": 102, "mean": 3},
    "bytes_out": {"total": 0, "mean": 0},
    "earliest": "2023-08-23T17:43:12.741597185+08:00",
    "latest": "2023-08-23T17:43:17.691525015+08:00",
    "end": "2023-08-23T17:43:45.226749165+08:00",
    "duration": 4949927830,
    "wait": 27535224150,
    "requests": 34,
    "rate": 6.868787014213902,
    "throughput": 1.046632012709457,
    "success": 1,
    "status_codes": {"200": 34},
    "errors": []
}

# Define the latency keys
latency_keys = ["total", "mean", "1th", "5th", "10th", "25th", "50th", "75th", "90th", "95th", "99th", "max", "min"]

# Convert latencies from nanoseconds to seconds again
# converted_latencies_retry = {key: data["latencies"][key] / 1e9 for key in latency_keys}  # 1e9 nanoseconds = 1 second

# print(converted_latencies_retry["total"])

from datetime import datetime

now = datetime.now()

print("현재 : ", now)

learning_count = 0
isLearningState = False
duration = 30
# for i in range(len(data_list_retry)):
for i in range(len(data_series)):
    rate = int(data_series[i])
    filename='baseline_log/results_%d.json' % (i)
    if rate < 1:
        rate = 1
    cmd = 'vegeta attack -timeout 2s -duration %is -rate %i/60s | vegeta report -type=json>>%s' % (duration, rate, filename)
    subprocess.run(cmd, shell=True, input=target, encoding='utf-8')
    # cmd2 = 'curl -X GET "http://192.168.171.169/post?date={0}&req={1}"'.format(data_list_retry[i][0].replace(' ', '+'), (rate))
    # # cmd3 = 'curl -X GET "http://192.168.171.169/getwindowsize?date={0}"'.format(data_list_retry[i][0].replace(' ', '+'))
    # print(data_list_retry[i][0])
    print('processing... : ', (round((i / len(data_list_retry)) * 100 , 2)))
    # subprocess.run(cmd, shell=True, input=target, encoding='utf-8')
    # time.sleep(1)
    # islearn = subprocess.run(cmd2, shell=True, encoding='utf-8', capture_output=True).stdout
    # print('islearn : ', islearn, flush=True)
    # if islearn == "exit":
    #     exit(0)
    
    # # learning check
    # # 학습중에는 실제 학습시간 고려하여 request 주도록 변환
    # # learncheckcmd = 'curl -X GET "http://192.168.171.169/learningstate"'
    # # alreadylearning = subprocess.run(learncheckcmd, shell=True, encoding='utf-8', capture_output=True).stdout
    # if islearn == "True" or islearn == True or islearn == "true":
    #     print("learning now..")
    #     isLearningState = True
    #     duration = 60
    #     learning_count += 1
    # elif isLearningState is True and learning_count < 2:
    #     duration = 60
    #     learning_count += 1
    # else:
    #     isLearningState = False
    #     duration = 15
    #     learning_count = 0
    
    #     # if islearn == "True" or islearn == True or islearn == "true":
    #     #     learncmd = 'curl -X GET "http://192.168.171.169/learn"'
    #     #     subprocess.Popen(learncmd, shell=True, encoding='utf-8')
    #     #     isLearningState = True
    #     #     duration = 60

    # # std = subprocess.run(cmd3, shell=True,encoding='utf-8', capture_output=True)
    # # threshold = std.stdout
    # # print('threshold : ', threshold, flush=True)
    # # if threshold == "exit":
    # #     exit(0)
    # # if threshold == None or threshold == 'None' or threshold == '' or threshold == 'null':
    # #     continue
    # # cmd4 = 'go run ~/./go/src/github.com/kdgyun/k8s-hpa-go-client/main.go {0}'.format(threshold)
    # # subprocess.run(cmd4, shell=True, encoding='utf-8', cwd='/home/ubuntu/go/src/github.com/kdgyun/k8s-hpa-go-client')
    # # time.sleep(2)
    
# killcmd = 'kill 1951'
# subprocess.run(killcmd, shell=True, encoding='utf-8', capture_output=True)
print("끝난시간 : ", now)