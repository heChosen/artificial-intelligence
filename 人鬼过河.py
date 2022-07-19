# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 17:47:06 2021

@author: cuihaoran
1.船出发岸不能出现0人0鬼
2.船上的人或鬼数目不能多余出发岸的人或鬼数目
3.岸上人数目大于鬼数目
er东岸上的人数，eg东岸上的鬼数，wr西岸上的人数，wg西岸上的鬼数，boat船的状态
state=[er,eg,wr,wg,boat]
       0, 1, 2, 3,  4 
"""

index=0#path中路径序号
path=[]#存储路径
state=[]#表示当前状态
er=3#三人
eg=3#三鬼
numways=0#存储路径数目
def Judge(state):#判断某状态是否满足条件
    if state[0]<0 or state[1]<0 or state[2]<0 or state[3]<0:
        return 0
    if (state[0]<state[1] and state[0]!=0) or (state[2]<state[3] and state[2]!=0):
        return 0
    for t in range(index):#判断该状态是否重复
        if state[0]==path[t][0] and state[1]==path[t][1] and state[4]==path[t][4]:
            return 0


def Find(state):
    global numways,index
    if state[2]==er and state[3]==eg:
        numways=numways+1
        print("第%d条路径" %(numways))
        print("东人 \t东鬼 \t西人 \t西鬼 \t船")
        for i in path:
            print(' ',i[0],'\t',' ',i[1],'\t',' ',i[2],'\t',' ',i[3],'\t',' ',i[4])
            print('\n')
        return 0
    
    if Judge(state)==0:
        return 0
    
    s=[0,0,0,0,0]#临时变量，存放过河操作
    
    #两个人过河
    s[0]=state[0]-2*state[4]
    s[1]=state[1]
    s[2]=state[2]+2*state[4]
    s[3]=state[3]
    s[4]=(-state[4])
    index=index+1
    path.append(s)
    Find(path[index])
    path.pop()
    index=index-1
    
    #两个鬼过河
    s[0]=state[0]
    s[1]=state[1]-2*state[4]
    s[2]=state[2]
    s[3]=state[3]+2*state[4]
    s[4]=(-state[4])
    index=index+1
    path.append(s)
    Find(path[index])
    path.pop()
    index=index-1
    
    #一个人一个鬼过河
    s[0]=state[0]-1*state[4]
    s[1]=state[1]-1*state[4]
    s[2]=state[2]+1*state[4]
    s[3]=state[3]+1*state[4]
    s[4]=(-state[4])
    index=index+1
    path.append(s)
    Find(path[index])
    path.pop()
    index=index-1
    
    #一个人过河
    s[0]=state[0]-1*state[4]
    s[1]=state[1]
    s[2]=state[2]+1*state[4]
    s[3]=state[3]
    s[4]=(-state[4])
    index=index+1
    path.append(s)
    Find(path[index])
    path.pop()
    index=index-1
    
    #一个鬼过河
    s[0]=state[0]
    s[1]=state[1]-1*state[4]
    s[2]=state[2]
    s[3]=state[3]+1*state[4]
    s[4]=(-state[4])
    index=index+1
    path.append(s)
    Find(path[index])
    path.pop()
    index=index-1
    
    return 0
    
def main():
    state=[3,3,0,0,1]
    path.append(state)
    Find(path[index])
    return

if __name__ == '__main__':
    main()
    