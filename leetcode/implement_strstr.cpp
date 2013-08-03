/*class Solution {
public:
  char *
  strStr(char *haystack, char *needle) {
    if (!*needle) return haystack;
    for (;*haystack;++haystack) {
      if (*haystack == *needle) {
        if (match(haystack, needle)) return haystack;
      }
    }
    return NULL;
  }
  bool match(char *h, char *n) {
    while (*n) {
      if (*(n++) != *(h++)) return false;
    }
    return true;
  }
};*/

class Solution {
public:
  char *
  strStr(char *haystack, char *needle) {
    if (!*needle) return haystack;
    char *hAdv = haystack;
    for (char *n = needle + 1; *n; ++n) {
      ++hAdv;
    }
    for (; *hAdv; ++haystack, ++hAdv) {
      if (match(haystack, needle)) return haystack;
    }
    return NULL;
  }

  bool
  match(char *h, char *n) {
    while (*n) {
      if (*(n++) != *(h++)) return false;
    }
    return true;
  }
};
