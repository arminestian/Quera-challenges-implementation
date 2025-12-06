#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {

    int n = 0;
    scanf("%d", &n);

    char sheets[500];
    int numbers[1000];
    int i = 0;
    getchar();
    fgets(sheets, sizeof(sheets), stdin);
    sheets[strlen(sheets) - 1] = '\0';

    char* token = strtok(sheets, " ");
    while (token != NULL) {
        numbers[i++] = atoi(token);
        token = strtok(NULL, " ");
    }

    int ans = 0;
    for (int j = 0; j < i; j++) {
        if (numbers[j] % 2 == 0) {
            ans += numbers[j] / 2;
        } else {
            ans += (numbers[j] / 2) + 1;
        }
    }

    printf("%d", ans);

    return 0;
}