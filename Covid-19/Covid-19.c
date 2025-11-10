#include <stdio.h>

int main() {

    int p = 0;
    int q = 0;

    scanf(" %d", &p);
    scanf(" %d", &q);

    if (p <= 50 && q <= 10) {
        printf("White\n");
    } else if (q >= 30) {
        printf("Red\n");
    } else {
        printf("Yellow\n");
    }
    
    return 0;
    
}