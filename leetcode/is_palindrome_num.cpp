#include <iostream>
#include <cstdlib>

bool isPalindromeNum(int x) {
  if (x < 0) return false;
	int div = 1;
	while (x/div >= 10) {
		div *= 10;
	}
	while (x >= 10) {
	  int l = x/div;
		int r = x%10;
		if (l != r) return false;
		x = (x%div)/10;
		div /= 100;
	}
	return true;
}

int main(int argc, char** argv) {
	if (argc < 2) {
		std::cout << "input error" << std::endl;
		return 1;
	}
	std::cout << argv[1] << " is Palindrome? "
	  << (isPalindromeNum(atoi(argv[1]))?"true":"false")
		<< std::endl;
	return 0;
}
