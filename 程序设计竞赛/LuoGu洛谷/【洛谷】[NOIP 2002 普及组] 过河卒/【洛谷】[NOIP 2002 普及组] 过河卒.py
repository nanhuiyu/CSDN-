def main():
    # 读取输入数据并分割成列表
    data = input().split()
    n = int(data[0])  # 棋盘终点x坐标
    m = int(data[1])  # 棋盘终点y坐标
    horse_x = int(data[2])  # 马的位置x坐标
    horse_y = int(data[3])  # 马的位置y坐标
    
    # 创建dp数组，大小为(n+1) x (m+1)，初始化为0
    # dp[i][j]表示从起点(0,0)到达点(i,j)的路径数量
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    # 创建障碍物标记数组，初始为False
    # obstacle[i][j]为True表示该位置被马控制，不能经过
    obstacle = [[False] * (m+1) for _ in range(n+1)]
    
    # 马的控制点偏移量（相对马的位置）
    # 包括马本身的位置(0,0)和马能走到的8个日字形位置
    dx = [0, 1, 1, -1, -1, 2, 2, -2, -2]
    dy = [0, 2, -2, 2, -2, 1, -1, 1, -1]
    
    # 标记马的控制点（障碍物）
    for i in range(9):
        # 计算马控制点的坐标
        nx = horse_x + dx[i]
        ny = horse_y + dy[i]
        # 检查坐标是否在棋盘范围内
        if 0 <= nx <= n and 0 <= ny <= m:
            obstacle[nx][ny] = True  # 标记为障碍物
            
    # 初始化起点(0,0)
    # 如果起点不被马控制，则到达起点的路径数为1
    if not obstacle[0][0]:
        dp[0][0] = 1
        
    # 动态规划遍历所有点
    for i in range(n+1):
        for j in range(m+1):
            # 如果当前点是障碍物，跳过计算
            if obstacle[i][j]:
                continue
            # 如果可以从上方点(i-1,j)走到当前点，则加上方的路径数
            if i > 0 and not obstacle[i-1][j]:
                dp[i][j] += dp[i-1][j]
            # 如果可以从左边点(i,j-1)走到当前点，则加左边的路径数
            if j > 0 and not obstacle[i][j-1]:
                dp[i][j] += dp[i][j-1]
                
    # 输出到达终点(n,m)的路径数量
    print(dp[n][m])

if __name__ == '__main__':
    main()