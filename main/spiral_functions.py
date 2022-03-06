import numpy as np
primes=np.array([])
pos = [0,0]
scale_ = 0
dir = 3
rots = 0
cur_dist=-1
move_length=0

def change_dir():
    global rots
    global dir
    rots+=1
    dir = (dir+1)%4
def increase_length(cur_length):
    return cur_length+1

def move():
    if dir==0:
        pos[0]+=scale_
    if dir==1:
        pos[1]-=scale_
    if dir==2:
        pos[0]-=scale_
    if dir==3:
        pos[1]+=scale_

def compositeness(n):
    return primes[n]

def initialize(res,scale):
    global pos
    global scale_
    scale_ = scale
    pos = [res*scale//2+1,res*scale//2]
    global primes
    primes = np.zeros(res*res)
    for i in range(2,res*res):
        primes[i]+=1
        j = i*i
        while j<res*res:
            primes[j] +=1
            j+=i
    primes +=1

def get_pos():
    return pos
    
def get_next_point():
    global cur_dist
    global move_length
    if cur_dist<move_length:
            cur_dist+=1
    else:
        change_dir()
        if rots%2==0:
            move_length = increase_length(move_length)
        cur_dist = 0