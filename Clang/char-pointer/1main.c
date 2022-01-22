#include <stdio.h>
#include <string.h>

int main()
{
    char array[7];
    char *ptr;
    strcpy(array, "abcdef");
    ptr = &(array[0]);
    strcpy(ptr, "ghijkl");
    printf(" array = %s\n ptr = %s\n", array, ptr);
}