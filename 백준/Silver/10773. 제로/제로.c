#include <stdio.h>
int top = -1;

int main() {
    int num;
    int sum = 0;
    int size;

    scanf("%d", &size);
    int stack[100000] ={0, };
    for(int i = 0; i<size; i++) {
        scanf("%d", &num);
        if(num == 0) {
            if (top == -1) {
                continue;
            }
            stack[top--] = 0;
        }else {
            stack[++top] = num;
        }
    }

    for(int i= 0; i<=top; i++) {
        sum += stack[i];
    }

    printf("%d", sum);
    return 0;
}



