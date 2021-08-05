/*
input :
3
9
1 2 3 4 5 6 7 8 9
9
9 8 7 6 5 4 3 2 1
23
23 41 13 22 -3 24 -31 -11 -8 -7
3 5 103 211 -311 -45 -67 -73 -81 -99
-33 24 56

output :
5
1 2 3 4 5
5
9 8 7 6 5
12
23 23 22 22 13 3 5 5 3 -3
-7 -3
*/

#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

// 전역 변수 선언
int T;


int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> T;
    while (T--){
        priority_queue<int, vector<int>, greater<int>> min_heap;
        priority_queue<int> max_heap;

        int N; cin >> N;
        cout << N / 2 + 1 << '\n';
        for (int i = 1; i <= N; i++){
            int num;
            cin >> num;

            if (max_heap.size() == min_heap.size()) {
                max_heap.push(num);
            }
            else{
                min_heap.push(num);
            }

            if (min_heap.size() != 0 && max_heap.top() > min_heap.top()){
                // swap
                int big = max_heap.top();
                int small = min_heap.top();
                max_heap.pop(); max_heap.push(small);
                min_heap.pop(); min_heap.push(big);
            }
            if (i & 1) cout << max_heap.top() << ' ';
            if (i % 20 == 0) cout << '\n';
        }
        cout << '\n';
    }

    return 0;
}