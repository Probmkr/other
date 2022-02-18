#include <stdio.h>
#include <string.h>

int main()
{
  char *onestring = "test5";
  // printf("%s\n", onestring);
  // printf("%lu\n", sizeof(onestring));
  // printf("%s\n", onestring*);
  // printf("%lu\n", sizeof(char*));
  printf("%lu", strlen(onestring));
}