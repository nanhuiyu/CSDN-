#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m, horse_x, horse_y;
    cin >> n >> m >> horse_x >> horse_y;
    
    // 创建dp数组，大小为(n+1) x (m+1)，初始化为0
    vector<vector<long long>> dp(n+1, vector<long long>(m+1, 0));
    // 标记马的控制点：使用一个二维数组，如果点是控制点则标记为true
    vector<vector<bool>> obstacle(n+1, vector<bool>(m+1, false));
    
    // 马的控制点偏移量
    int dx[] = {0, 1, 1, -1, -1, 2, 2, -2, -2};
    int dy[] = {0, 2, -2, 2, -2, 1, -1, 1, -1};
    
    // 标记马的控制点
    for (int i = 0; i < 9; i++) {
        int nx = horse_x + dx[i];
        int ny = horse_y + dy[i];
        if (nx >= 0 && nx <= n && ny >= 0 && ny <= m) {
            obstacle[nx][ny] = true;
        }
    }
    
    // 初始化起点(0,0)
    if (!obstacle[0][0]) {
        dp[0][0] = 1;
    }
    
    // 动态规划遍历
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= m; j++) {
            if (obstacle[i][j]) {
                continue; // 控制点，路径数为0
            }
            if (i > 0 && !obstacle[i-1][j]) {
                dp[i][j] += dp[i-1][j]; // 从上方来
            }
            if (j > 0 && !obstacle[i][j-1]) {
                dp[i][j] += dp[i][j-1]; // 从左方来
            }
        }
    }
    
    cout << dp[n][m] << endl;
    return 0;
}