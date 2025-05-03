#include <iostream>
#include <vector>
#include <algorithm>
#include <cstddef>
using namespace std;

struct Plant {
    long long X, Y;
    int idx;
};

void solve_region(long long xl, long long xr, long long yb, long long yt, vector<Plant>& pts, vector<long long>& ans) {
    if (pts.empty()) return;

    if (pts.size() == 1) {
        auto& p = pts[0];
        long long L = min({p.X - xl, xr - p.X, p.Y - yb, yt - p.Y});
        ans[p.idx] = 2 * L;
        return;
    }

    long long width = xr - xl;
    long long height = yt - yb;

    if (width >= height) {
        // Разрез по X
        vector<pair<long long, int>> events;
        for (auto& p : pts) {
            long long maxL = min({p.X - xl, xr - p.X, p.Y - yb, yt - p.Y});
            events.emplace_back(p.X - maxL, +1);
            events.emplace_back(p.X + maxL + 1, -1);
        }
        sort(events.begin(), events.end());

        long long best = -1;
        int bestCount = -1, cur = 0;
        for (size_t i = 0; i < events.size(); ++i) {
            cur += events[i].second;
            if (i + 1 < events.size() && events[i].first == events[i + 1].first) continue;
            if (cur > bestCount) {
                bestCount = cur;
                best = events[i].first;
            }
        }

        long long cutX = best;
        vector<Plant> left, right;
        for (auto& p : pts) {
            long long maxL = min({p.X - xl, xr - p.X, p.Y - yb, yt - p.Y});
            if (p.X + maxL < cutX)
                left.push_back(p);
            else if (p.X - maxL > cutX)
                right.push_back(p);
            else {
                long long L = min({p.X - xl, xr - p.X, p.Y - yb, yt - p.Y});
                ans[p.idx] = 2 * L;
            }
        }

        solve_region(xl, cutX, yb, yt, left, ans);
        solve_region(cutX, xr, yb, yt, right, ans);

    } else {
        // Разрез по Y
        vector<pair<long long, int>> events;
        for (auto& p : pts) {
            long long maxL = min({p.X - xl, xr - p.X, p.Y - yb, yt - p.Y});
            events.emplace_back(p.Y - maxL, +1);
            events.emplace_back(p.Y + maxL + 1, -1);
        }
        sort(events.begin(), events.end());

        long long best = -1;
        int bestCount = -1, cur = 0;
        for (size_t i = 0; i < events.size(); ++i) {
            cur += events[i].second;
            if (i + 1 < events.size() && events[i].first == events[i + 1].first) continue;
            if (cur > bestCount) {
                bestCount = cur;
                best = events[i].first;
            }
        }

        long long cutY = best;
        vector<Plant> lower, upper;
        for (auto& p : pts) {
            long long maxL = min({p.X - xl, xr - p.X, p.Y - yb, yt - p.Y});
            if (p.Y + maxL < cutY)
                lower.push_back(p);
            else if (p.Y - maxL > cutY)
                upper.push_back(p);
            else {
                long long L = min({p.X - xl, xr - p.X, p.Y - yb, yt - p.Y});
                ans[p.idx] = 2 * L;
            }
        }

        solve_region(xl, xr, yb, cutY, lower, ans);
        solve_region(xl, xr, cutY, yt, upper, ans);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    long long W, H;
    cin >> W >> H;

    vector<Plant> pts(n);
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].X >> pts[i].Y;
        pts[i].idx = i;
    }

    vector<long long> ans(n);
    solve_region(0, W, 0, H, pts, ans);

    for (auto x : ans)
        cout << x << '\n';

    return 0;
}
