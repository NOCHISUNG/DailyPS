/*
input :
7
2
1
4
5
1
3
3

output :
8
*/

#include <iostream>
#include <algorithm>
#define PIV (1 << 17)
#define MAX (1 << 30)
using namespace std;
using ll = long long;

// 전역 변수 선언
int N;
int nums[100005];
int TREE[2 * PIV];

void update(int ind){
    ind += PIV;
    TREE[ind] = ind - PIV;
    while (ind >>= 1){
        if (nums[TREE[2 * ind]] <= nums[TREE[2 * ind + 1]]) TREE[ind] = TREE[2 * ind];
        else TREE[ind] = TREE[2 * ind + 1];
    }
}

int query(int l, int r){
    l += PIV; r += PIV;
    int ind_of_min_val = 0;
    while(l <= r){
        if (l & 1){
            if (nums[TREE[l]] < nums[ind_of_min_val]){
                ind_of_min_val = TREE[l];
            }
            l++;
        }
        if (!(r & 1)){
            if (nums[TREE[r]] < nums[ind_of_min_val]){
                ind_of_min_val = TREE[r];
            }
            r--;
        }
        l >>= 1; r >>= 1;
    }
    return ind_of_min_val;
}

ll divide_and_conquer(int l, int r){
    if (l > r) return 0;

    int ind_of_min_val = query(l, r);
    int ret = 0;
    ll case1 = max(ret, nums[ind_of_min_val] * (r - l + 1));
    ll case2 = max(case1, divide_and_conquer(l, ind_of_min_val - 1));
    ll case3 = max(case2, divide_and_conquer(ind_of_min_val + 1, r));
    return case3;
}
int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N;
    for (int i = 1; i <= N; i++){
        cin >> nums[i];
    }
    nums[0] = MAX;
    for (int i = 1; i <= N; i++){
        update(i);
    }

    cout << divide_and_conquer(1, N);
    return 0;
}