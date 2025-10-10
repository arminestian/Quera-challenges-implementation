#include <iostream>
#include <cmath>

int main() {
    int n, m;
    std::cin >> n >> m;

    double final_sum = 0;

    for (int i = -10; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            final_sum += int(std::pow(i + j, 3) / std::pow(j, 2));
        }
    }

    std::cout << final_sum << std::endl;

    return 0;
}