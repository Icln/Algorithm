#include<iostream>
using namespace std;
int main() {
	int A, B, C;

	cin >> A >> B;
	cin >> C;

	if (A >= 0 && A <= 23 && B >= 0 && B <= 59 && C >= 0 && C <= 1000) {
		if (C + B >= 60) {
			A += (C + B) / 60;
			B = (C + B) % 60;
			if (A >=24)
			{ 
				A -= 24;
			}
		}
		else {
			B += C;
		}
		cout << A << " " << B << "\n";
	}
	else {
		cout << "error" << "\n";
	}
	return 0;
}