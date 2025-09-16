#guess number using random
import random
s=1
e=100
x=random.randint(1,100)
while True:
    i=input('請輸入一個'+str(s)+'-'+str(e)+'的數字，猜一下電腦所產生的數字：')
    i = int(i)
    if i==x:
        print('正確答案：',x,'你太厲害了，竟然知道電腦的答案')
        break
    if i>x:
        print('電腦的數字小於',i)
        e=i
        
    else:
        print('電腦的數字大於',i)
        s=i
  
    print(x)

