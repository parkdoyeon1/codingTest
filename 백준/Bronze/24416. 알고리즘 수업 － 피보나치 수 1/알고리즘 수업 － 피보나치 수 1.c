#include <stdio.h>
int count1 = 0;
int count2 = 0;
int f[100] = {1,1};

int fib(int n) {
    if (n == 1 || n == 2) {
        count1++;
        return 1;
    } else {
        return (fib(n-1)+ fib(n-2));
    }
}

int fibonacci(int n) {
    for(int i = 3; i<=n; i++) {
        count2++;
        f[i] = f[i-1]+f[i-2];
    }
    return f[n];
}


int main() {

    int n;
    int a;
    scanf("%d", &n);
    a = n;
    fib(n);
    fibonacci(a);
    printf("%d %d", count1, count2);
    return 0;
}