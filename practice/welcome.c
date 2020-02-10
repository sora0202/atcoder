#include <stdio.h>

#define STR_MAX_LEN 100

int main(void)
{
    int a, b, c;
    char s[STR_MAX_LEN + 1];

    scanf("%d", &a);
    scanf("%d %d", &b, &c);
    scanf("%s", s);

    printf("%d %s\n", a + b + c, s);
    return 0;
}