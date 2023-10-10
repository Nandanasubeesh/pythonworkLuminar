#include<stdio.h>
#include<stdlib.h>
 int main (void)
 {
    int num;
    printf("Enter a number");
    scanf("%d",&num);
    if (num<0)
    {
        printf("The given number is negative");
    }   
    else
    {
        printf("The given number is positive");
    }
    return EXIT_SUCCESS;
 }