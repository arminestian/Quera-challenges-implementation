#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

long double tavan(long double base, long long exp) {
    if (base == 0 && exp > 0)
        return 0;
    if (exp == 0)
        return 1;
    if (exp == 1)
        return base;
    if (exp == 2)
        return base * base;
    if (exp < 0)
        return 1 / (base * tavan(base, abs(exp) - 1));
    return base * tavan(base, exp - 1);
}

int main() {
    long double Base;
    long long exp;

    cin >> Base;
    cin >> exp;

    long double result = tavan(Base, exp);

    cout << fixed << setprecision(3) << result << endl;

    return 0;
}
