# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 16:42:29 2021
A*算法实现寻路
起始点：（4，0） 终点(0,6)
open队列中每个元素[f,(x,y),pre,gx] pre用于指向父节点
使用优先队列PriorityQueue创建quopen表
@author: cuihaoran
"""
from queue import Queue,LifoQueue,PriorityQueue
dir=[[-1,0],[0,1],[1,0],[0,-1]]#上右下左
begin=(4,0)
end=(0,6)

def Initmap(map):#初始化地图
    for i in range(7):
        map[i][4]=1
    return 0

def Show(map):
    for i in range(10):
        print(map[i])
    return 0


def Hx(x,y):#当前点到终点的曼哈顿距离
    return abs(x-0)+abs(y-6)

def Check(x,y,map):#检查该点是否越界和是否已访问该点，该点可走返回1
    if x>=0 and x<10:
        if y>=0 and y<10:
            if map[x][y]!=-1:
                return 1
            

def AStar(map):
    quclose=[]#close表，存放已扩展的点
    path=[]#存储路径
    quopen = PriorityQueue()#open表
    quopen.put((map[begin[0]][begin[1]],begin,-1,0))
    map[begin[0]][begin[1]]=-1#已访问过的点设为-1，防止再次访问
    index=-1#close表中的数据下标
    while not quopen.empty():
        w=quopen.get()     
        index=index+1
        quclose.append(w)
        if w[1][0]==0 and w[1][1]==6:#若找到终点，输出路径
            path.append(w[1])
            sear=w[2]
            while not sear==-1:#通过pre将close表中的路径点放入path中
                path.append(quclose[sear][1])
                sear=quclose[sear][2]
            path.reverse()
            for k in path:
                print(k)
            return 1    
        for i in range(4):#上右下左四个方向遍历
            if Check(w[1][0]+dir[i][0],w[1][1]+dir[i][1],map) and map[w[1][0]+dir[i][0]][w[1][1]+dir[i][1]]!=1:
                hx=Hx(w[1][0]+dir[i][0],w[1][1]+dir[i][1])
                gx=w[3]+1
                newx=w[1][0]+dir[i][0]
                newy=w[1][1]+dir[i][1]
                quopen.put((gx+hx,(newx,newy),index,gx))
                map[newx][newy]=-1#已访问过的点设为-1，防止再次访问
            
    return 0

def main():
    map=[[0]*10 for i in range(10)]
    Initmap(map)
    print("地图为：")
    Show(map)
    print("路径为：")
    AStar(map)
    return 0
if __name__ == '__main__':
    main()