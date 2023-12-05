#include<stdio.h>

void main()
{
    int x, *y;
    float a, *b;
    x = 20;
    b = &x;
    printf("%d is stored at addr %u.\n", x, &x);
    printf("%f is stored at addr\n", b);
}