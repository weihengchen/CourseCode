import sys
import time

def Fibonacci_1(num):
    if num <= 0:
        return 0;
    if num == 1:
        return 1;
    return Fibonacci_1(num-1) + Fibonacci_1(num-2);


def Fibonacci_2(num):
    ans = [ 0 for i in range(num+1)];
    ans[1] = 1;
    for i in range(2, num+1):
        ans[i] = ans[i-1] + ans[i-2];
    return ans[num];

def Fibonacci_3(num):
    return num;

if __name__=='__main__':
    num = 70;
    start_time = time.time();
    ans = Fibonacci_1(num/2);
    end_time = time.time();
    print ( "Fibonacci_1(%d/2) = %d runing time: %s seconds" % (num, ans, end_time - start_time));

    start_time = time.time();
    ans = Fibonacci_2(num);
    end_time = time.time();
    print ( "Fibonacci_2(%d) = %d runing time: %s seconds" % (num, ans, end_time - start_time));


