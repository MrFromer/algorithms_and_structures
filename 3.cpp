#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<int> s(n);
    for (int i = 0; i < n; ++i)
        cin >> s[i];

    // last_occurrence[c] = последнее место, где цвет c должен появиться
    unordered_map<int, int> last_occurrence;
    for (int i = 0; i < n; ++i)
        last_occurrence[s[i]] = i;

    vector<tuple<int, int, int>> result; // (color, l, r)
    set<int> used_colors;

    // Вектор, который имитирует перекраску
    vector<int> painted(n, 0);

    for (int i = n - 1; i >= 0; --i) {
        int color = s[i];
        if (used_colors.count(color)) continue;

        // Где начинается отрезок этого цвета
        int l = i;
        while (l > 0 && s[l - 1] == color)
            --l;

        used_colors.insert(color);
        result.push_back({color, l + 1, i + 1}); // переводим в 1-based индексацию

        // "Применяем" краску
        for (int j = l; j <= i; ++j)
            painted[j] = color;
    }

    // Проверка: действительно ли перекрасили как нужно
    bool ok = true;
    for (int i = 0; i < n; ++i) {
        if (painted[i] != s[i]) {
            ok = false;
            break;
        }
    }

    if (!ok || result.size() > m) {
        cout << -1 << '\n';
    } else {
        cout << result.size() << '\n';
        for (auto it = result.rbegin(); it != result.rend(); ++it) {
            int c, l, r;
            tie(c, l, r) = *it;
            cout << c << " " << l << " " << r << '\n';
        }
    }

    return 0;
}
