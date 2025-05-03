#include <bits/stdc++.h>
using namespace std;

// Рекурсивный парсер: синтаксис grammar:
// Expression := signedTerm {( '+' | '-' ) signedTerm}
// signedTerm := {('+' | '-')} factor
// factor := number | '(' Expression ')'
long long parseExpression(const string &s, int &i);
long long parseSignedTerm(const string &s, int &i);
long long parseFactor(const string &s, int &i);

long long parseExpression(const string &s, int &i) {
    long long val = parseSignedTerm(s, i);
    int n = s.size();
    while (true) {
        // пропускаем пробелы
        while (i < n && s[i] == ' ') i++;
        if (i >= n || s[i] == ')') break;
        char op = s[i];
        if (op != '+' && op != '-') break;
        i++;
        long long term = parseSignedTerm(s, i);
        if (op == '+') val += term;
        else           val -= term;
    }
    return val;
}

long long parseSignedTerm(const string &s, int &i) {
    int n = s.size();
    while (i < n && s[i] == ' ') i++;
    long long sign = 1;
    // Обрабатываем несколько подряд стоящих знаков
    while (i < n && (s[i] == '+' || s[i] == '-')) {
        if (s[i] == '-') sign = -sign;
        i++;
        while (i < n && s[i] == ' ') i++;
    }
    long long factorVal = parseFactor(s, i);
    return sign * factorVal;
}

long long parseFactor(const string &s, int &i) {
    int n = s.size();
    while (i < n && s[i] == ' ') i++;
    if (i < n && s[i] == '(') {
        i++;  // пропустить '('
        long long val = parseExpression(s, i);
        while (i < n && s[i] == ' ') i++;
        if (i < n && s[i] == ')') i++;
        return val;
    } else {
        // Число
        long long num = 0;
        while (i < n && s[i] == ' ') i++;
        while (i < n && isdigit(s[i])) {
            num = num * 10 + (s[i] - '0');
            i++;
        }
        return num;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string expr;
    if (!getline(cin, expr)) return 0;
    int idx = 0;
    long long result = parseExpression(expr, idx);
    cout << result;
    return 0;
}
