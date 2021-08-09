# Uses python3
import sys

def get_change(m):
    n = 0;
    moneys = [10,5,1];
    while(m!=0):
        while(m-10>=0):
            m-=10;
            n+=1;
        while(m-5>=0):
            m-=5;
            n+=1;
        while(m-1>=0):
            m-=1;
            n+=1;	
    return n

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))