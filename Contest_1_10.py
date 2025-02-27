import sys


def solve(t, queries):
    results = []
    for n, m in queries:
        total_sum = n * m * (n * m + 1) // 2
        half_sum = total_sum // 2

        # Вертикальный разрез
        vertical_cut = (m * (m + 1)) // 2
        if vertical_cut >= half_sum:
            left, right = 1, m
            while left < right:
                mid = (left + right) // 2
                if (mid * (mid + 1) // 2) < half_sum:
                    left = mid + 1
                else:
                    right = mid
            results.append(f"V {left}")
            continue

        # Горизонтальный разрез
        horizontal_cut = (n * (2 * m + (n - 1) * m)) // 2
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if (mid * m * (mid * m + 1)) // 2 < half_sum:
                left = mid + 1
            else:
                right = mid
        results.append(f"H {left}")

    return results


def main():
    t = int(sys.stdin.readline().strip())
    queries = []
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().strip().split())
        queries.append((n, m))

    answers = solve(t, queries)
    print("\n".join(answers))


if __name__ == "__main__":
    main()
