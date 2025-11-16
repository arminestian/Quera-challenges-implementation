countries = int(input())

for _ in range(countries):
    days_in_season = int(input())
    temps = list(map(int, input().split()))
    n = 4 * days_in_season
    temp_days = temps + temps[:days_in_season - 1]

    window_sum = sum(temp_days[:days_in_season])
    sums = [window_sum]
    for i in range(1, n):
        window_sum += temp_days[i + days_in_season - 1] - temp_days[i - 1]
        sums.append(window_sum)

    max_sum = max(sums)
    min_sum = min(sums)

    found = False
    for start in range(n):
        spring = sums[start % n]
        summer = sums[(start + days_in_season) % n]
        autumn = sums[(start + 2 * days_in_season) % n]
        winter = sums[(start + 3 * days_in_season) % n]
        if summer == max_sum and winter == min_sum:
            found = True
            break

    print("Yes" if found else "No")
