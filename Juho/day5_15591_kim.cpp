/*
input :
4 3
1 2 3
2 3 2
2 4 4
1 2
4 1
3 1

output :
3
0
2
*/


#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#define INF (1000000005)
#define SZ (5005)
using namespace std;

typedef struct w2nd{
    int w, node;
}w2nd;

// 전역 변수 선언
int N, Q;
vector<w2nd> graph[SZ];
int visited[SZ];

void bfs(int s_node){
    queue<int> que;
    que.push(s_node);
    visited[s_node] = INF - 1;

    while (!que.empty()){
        int cur = que.front(); que.pop();
        for (w2nd nxt: graph[cur]){
            if (visited[nxt.node] != INF) continue;

            visited[nxt.node] = min(visited[cur], nxt.w);
            que.push(nxt.node);
        }

    }
}

int main(){
    ios::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);
    freopen("input.txt", "r", stdin);

    cin >> N >> Q;
    for (int i = 0; i < N - 1; i++){
        int a, b, w;
        cin >> a >> b >> w;
        graph[a].push_back({w, b});
        graph[b].push_back({w, a});
    }

    for (int i = 0; i < Q; i++){
        int k, node;
        cin >> k >> node;

        fill(visited, visited + SZ, INF);
        bfs(node);

        // k 이하의 것들을 세어줌
        int cnt = 0;
        for (int i = 1; i <= N; i++){
            if (i == node) continue;

            if (visited[i] >= k) cnt += 1;
        }
        cout << cnt << '\n';
    }
    return 0;
}
