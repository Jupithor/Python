#https://open.kattis.com/problems/securedoors
import sys

cases = int(sys.stdin.readline())
log={}

for case in range(cases):
    status , name = sys.stdin.readline().split()

    if status == "entry":
        status = "entered"
    else:
        status = "exited"

    if (name not in log and status == "exited") or (name in log and log[name]==status):
        print(name, status, "(ANOMALY)")
    else:
        print(name, status)
    log[name]=status