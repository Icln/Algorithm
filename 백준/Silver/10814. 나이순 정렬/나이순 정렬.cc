#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
vector <pair<int, string>>  v;
bool compare(pair<int,string> a, pair<int,string> b) {
	return a.first < b.first;
}
int main() {
	ios::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);
	int num, age;
	string name;
	cin >> num;
	for (int i = 0; i < num; i++){
		cin >> age >> name;
		v.push_back({age ,name});
	}
	stable_sort(v.begin(), v.end(),compare);
	for (auto i : v)
	{
		cout << i.first << " " << i.second << "\n";
	}

	return 0;
}