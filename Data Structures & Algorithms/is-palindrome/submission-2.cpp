class Solution {
public:
    bool isPalindrome(string s) {
        string something = "";
        for(int i = 0; i < s.length(); i++){
            if(isalnum((unsigned char)s[i])){ // check if its alphanumerical
                something += tolower((unsigned char)s[i]);
            }
        }
        cout << something << endl;

        int i = 0;
        int j = something.length() - 1;
        while(i < j){
            if(something[i] != something[j]){
                return false;
            }
            i++;
            j--;
        }

        return true;
    }
};
