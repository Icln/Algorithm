#include<string>
#include<iostream>
#include<stack>

using namespace std;
stack <char> vps;
bool answer;	
bool solution(string s)
{
    for (int j = 0; j < s.length(); j++){
		vps.push(s[j]);
	}
	int cnt = 0;
	int size = vps.size();
	int k = 0;
	for (k = 0; k < size; k++)
	{
		if (vps.top() == '(') {
			if (cnt > 0) {
				cnt--;
				vps.pop();
			}
		    else {
			    answer = false;
			    break;
		    }
	    }
	    else if (vps.top() == ')')
	    {
		    if (cnt < 0){
			    answer = false;
			    break;
		    }   
		    else {
			    cnt++;
			    vps.pop();
		    }
	    }
    }
	if (k == size){
		if (cnt > 0){
			answer = false;
		}
		else {
			answer = true;
		}
	}
    

    return answer;
}