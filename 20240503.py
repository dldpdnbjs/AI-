# -*- coding: utf-8 -*-
"""20240503

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q2iUcFuOxbNblC59UHo053Bun8P2c58E
"""

import numpy as np   #한번 부르면 다시 안불러도됨
arr = np.arange(1,10,2)
print(arr)



arr = np.linspace(0,1,10)
print(arr)

zerozero = np.ones((3,4))
print(zerozero)

arr=np.arange(1,37)
arrr=arr.reshape(3,3,4)
print(arrr)

import numpy as np
ar=np.arange(1,26)
arr=ar.reshape(5,5)
print(arr)
sh=arr.shape        #모양 계산
print(sh)
print(arr[0:2,0:2])
print(arr[3:5,3:5])
print(arr[0:2,0:])  # arr[0:2]
print(arr[0:,3:5])    # 0: 로 전체행 표현