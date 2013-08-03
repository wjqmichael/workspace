#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <queue>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

typedef unordered_multimap<string, string> Map;
typedef pair<Map::iterator, Map::iterator> PairIter;

class Solution {
public:
  // backtrack to reconstruct the path from start -> end.
  vector<vector<string> >
  print(Map &map, string s, string start, int depth = 0) {
    if (depth > 0 && s == start) {
      return vector < vector < string >> (1, vector < string > (1, s));
    }
    vector < vector < string >> ret;
    for (PairIter it = map.equal_range(s); it.first != it.second; ++it.first) {
      vector < vector < string >> temp = print(map, it.first->second, start,
          depth + 1);
      for (int i = 0; i < temp.size(); i++) {
        temp[i].push_back(s);
      }
      ret.insert(ret.end(), temp.begin(), temp.end());
    }
    return ret;
  }

  void
  printMap(Map& map) {
    for (auto it = map.begin(); it != map.end(); ++it) {
      cout << it->first << " : " << it->second << endl;
    }
  }

  vector<vector<string> >
  findLadders(string start, string end, unordered_set<string> &dict) {
    Map map, map2;
    queue<string> q, q2;
    q.push(start);
    bool goal = false;
    while (!q.empty()) {
      string word = q.front();
      q.pop();
      for (int i = 0; i < start.length(); i++) {
        string s = word;
        for (char c = 'a'; c <= 'z'; c++) {
          s[i] = c;
          if (s == word) continue;
          if (s == end) goal = true;
          if (map.find(s) == map.end() && dict.find(s) != dict.end()) {
            if (map2.find(s) == map2.end()) {
              q2.push(s);
            }
            cout << s << " " << word << endl;
            map2.insert(make_pair(s, word));
          }
        }
      }
      if (q.empty()) {
        swap(q, q2);
        map.insert(map2.begin(), map2.end());
        map2.clear();
        if (goal) {
          printMap(map);
          return print(map, end, start);
        }
      }
    }
    return vector<vector<string>>();
  }

};

int
main(int argc, char** argv) {
  Solution sol;
  unordered_set<string> dict = {"hot","dot","dog","lot","log","cog"};
  vector < vector<string> > v = sol.findLadders("hot", "dog", dict);
  for (vector<string>& p : v) {
    for (string& s : p) {
      cout << s << " ";
    }
    cout << endl;
  }
  cout << "bye" << endl;
  return 0;
}
