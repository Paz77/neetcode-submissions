class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        int const INF = 2147483647;
        int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        int rows = grid.size(), cols = grid[0].size();
        queue<pair<int, int>> q;

        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                if(grid[r][c] == 0){
                    q.push({r, c});
                }
            }
        }

        while(!q.empty()){
            auto [r, c] = q.front();
            q.pop();

            for(int i = 0; i < 4; i++){
                int newR = r + directions[i][0];
                int newC = c + directions[i][1];

                if(newR >= 0 && newC >= 0 && newR < rows && newC < cols && grid[newR][newC] == INF){
                    grid[newR][newC] = grid[r][c] + 1;
                    q.push({newR, newC});
                }
            }
        }
    }
};