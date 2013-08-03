class Solution {
public:
  typedef string::const_iterator it_t;
  string
  convert(string s, int nRows) {
    if (nRows == 1) return s;

    string temp[nRows];
    bool down = true;
    int index = 0;
    for (it_t p = s.begin(); p != s.end(); ++p) {
      temp[index].push_back(*p);
      if (down) {
        if (index != nRows - 1) ++index;
        else {
          down = false;
          --index;
        }
      } else {
        if (index != 0) --index;
        else {
          down = true;
          ++index;
        }
      }
    }

    string result;
    for (int i = 0; i < nRows; ++i) {
      result.append(temp[i]);
    }
    return result;
  }
};
