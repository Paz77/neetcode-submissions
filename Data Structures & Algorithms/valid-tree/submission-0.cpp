class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if(edges.size() != n - 1) return false;

        unordered_map<int, vector<int>> graph;
        vector<bool> visited(n, false);

        for(auto& edge : edges){
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        dfs(0, graph, visited);

        for(int i = 0; i < n; i++){
            if(!visited[i]) return false;
        }

        return true;
    }

    void dfs(int node, unordered_map<int, vector<int>>& graph, vector<bool>& visited){
        visited[node] = true;
        for(int neighbor : graph[node]){
            if(!visited[neighbor]){
                dfs(neighbor, graph, visited);
            }
        }
    }
};
