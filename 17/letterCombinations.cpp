#include<iostream>
#include<unordered_map>
#include<string>
#include<vector>

using namespace std;
const unordered_map<char, string> myMap {
  {'2', "abc"}, 
  {'3', "def"}, 
  {'4', "ghi"},
  {'5', "jkl"},
  {'6', "mno"},
  {'7', "pqrs"},
  {'8', "tuv"},
  {'9', "wxyz"}
};

class Solution {
public:
  vector<string> letterCombinations(string digits) {
    vector<string> combinations;
    if (digits.empty())
      return combinations;
    
    string combination;
    drawback(combinations, digits, 0, combination);
    return combinations;
  }

  void drawback(vector<string>& combinations, const string& digits, int index, string& combination) {
    if (digits.length() == index) {
      combinations.push_back(combination);
    }
    else {
      const string& letter = myMap.at(digits[index]);
      for (const char& ch : letter) {
        combination.push_back(ch);
        drawback(combinations, digits, index + 1, combination);
        combination.pop_back();
      }
    }
  }
};

int main() {
  Solution solution;
  string digits = "4328";
  vector<string> combinations = solution.letterCombinations(digits);
  for (const string& combination : combinations) {
    cout << combination << endl;
  }
}
