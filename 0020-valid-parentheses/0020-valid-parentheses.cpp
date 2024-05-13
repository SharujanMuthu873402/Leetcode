class Solution {
public:
    bool isValid(string s) {
        vector<int> brackets;

        for(int i = 0; i < s.length(); i++){
            if(s[i] == '(' || s[i] == '[' || s[i] == '{'){
                brackets.push_back(s[i]);
            }

            else if(s[i] == ')'){
                if(brackets.size() > 0 && brackets.back() == '('){
                    brackets.pop_back();
                }
                
                else{
                    return false;
                    }
            }

            else if(s[i] == ']'){
                if(brackets.size() > 0 && brackets.back() == '['){
                    brackets.pop_back();
                }

                else{
                
                return false;
                
                }
            }

            else if(s[i] == '}'){
                if(brackets.size() > 0 && brackets.back() == '{'){
                    brackets.pop_back();
                }

                else{
                    return false;
                }
            }
        }
        return(brackets.size() == 0);
        
    }
};