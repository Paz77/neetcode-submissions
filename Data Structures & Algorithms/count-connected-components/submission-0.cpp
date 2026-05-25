class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        unordered_map<int, vector<int>> graph;
        vector<bool> visited(n, false);

        for(auto const& edge : edges){
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        int ans = 0;
        for(int i = 0; i < n; i++){
            if(!visited[i]){
                bfs(i, graph, visited);
                ans++;
            }
        }

        return ans;
    }

    void bfs(int node, unordered_map<int, vector<int>>& graph, vector<bool>& visited){
        queue<int> q;
        q.push(node);
        visited[node] = true;

        while(!q.empty()){
            int curr = q.front();
            q.pop();

            for(int neighbor : graph[curr]){
                if(!visited[neighbor]){
                    q.push(neighbor);
                    visited[neighbor] = true;
                }
            }
        }
    }
};
