class Solution {
public:
    string encode(vector<string>& strs) {
        string result;
        for(int i = 0; i < strs.size(); i++){
            result += to_string(strs[i].length()) + "#" + strs[i];
        }
        return result;
    }

    vector<string> decode(string s) {
        vector<string> result;
        int i = 0;
        int j;

        while(i < s.size()){
            j = i;
            while(s[j] != '#'){
                j++;
            }
            string temp; 
            for(i; i < j; i++){
                temp += s[i];
            }
            int length = stoi(temp);
            string word = "";
            for(i = j + 1; i <  j + 1 + length; i++){
                word += s[i];
            }
            result.push_back(word);
            i = j + 1 + length;
        }

        return result;
    }
};
