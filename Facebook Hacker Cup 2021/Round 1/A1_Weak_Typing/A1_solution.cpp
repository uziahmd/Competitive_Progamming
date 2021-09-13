#include <fstream>
#include <vector>
#include <iostream>
using namespace std;

ofstream output("output.txt");
ifstream input("input.txt");

int main()
{
int N, T;
input >> T;
for (int t = 1; t<=T; t++){
    input >> N;
    int count = 0;
    char current;
    std::vector<char> arr; 
    
    for (int x = 0; x < N; x++){
        char temp;
        input >> temp;
        if (temp != 'F'){arr.push_back(temp);}
    }

    if ((N <= 1) || (arr.size()== 0)){count = 0;}
    else{
        current = arr[0];
        for (int a = 0; a < arr.size(); a++){
            if(current != arr[a]){
                count++;
                current = arr[a];
            }
        }
    }
    output << "Case #" << t << ": " << count << "\n";
    cout << "Case #" << t << ": " << count << "\n";
}

return 0;
}