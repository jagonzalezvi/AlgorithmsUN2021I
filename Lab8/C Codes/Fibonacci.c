#include<stdio.h>

long long inefficientAlgorithm(int n);
long long fibonacciEfficient(int n);


int main(){

	int num;
	scanf("%d",&num);

	printf("\n %lld",fibonacciEfficient(num));

}


long long inefficientAlgorithm(int n){
        if(n<= 1)
                return n;
        else
                return inefficientAlgorithm(n-1)+inefficientAlgorithm(n-2);
};


long long fibonacciEfficient(int n){
        int f[n];
        f[0] = 0;
        f[1] = 1;

        for(int i = 2; i<=n; i++){
                f[i] = f[i-1]+f[i-2];
        }
        return f[n];
};
