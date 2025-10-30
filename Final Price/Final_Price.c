#include <stdio.h>

int main() {

    int n = 0;
    scanf(" %d", &n);
    int ans = 0;
    int temp = 0;

    for (int i = 0; i < n; i++) {
        scanf(" %d", &temp);
        ans += temp;
    }
    printf("%d\n", ans);
    
    return 0;
    
}
