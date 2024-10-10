#include <stdio.h>

int global_i = 2;

void hello(){
    printf("hello, world. It's Tushar Viradiya\n");
}

int sum(int y, int z){
    int a;
    a = z + y + global_i;
    return a;
}

int main(){
    hello();
    int s = sum(3,4);
    printf("sum of values is : %i\n", s);
}