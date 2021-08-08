/*
input :
4

output :
43
*/

#include <iostream>
#include <algorithm>
#define MOD (1000000)
using namespace std;
using ll = long long;

// 전역 변수 선언
int N;
ll dp[1005][1005][2][3];

ll recur(int day, int attendance, int late, int absent){
    if (late == 2) return 0;
    if (absent == 3) return 0;
    if (day == N) return 1;
    if (dp[day][attendance][late][absent]) return dp[day][attendance][late][absent];

    dp[day][attendance][late][absent] = \
        recur(day + 1, attendance + 1, late, 0) + \
        recur(day + 1, attendance, late + 1, 0) + \
        recur(day + 1, attendance, late, absent + 1);

    dp[day][attendance][late][absent] %= MOD;
    return dp[day][attendance][late][absent];
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    cout << recur(0, 0, 0, 0);

    return 0;
}