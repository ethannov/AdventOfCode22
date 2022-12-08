#include <iostream>
#include <fstream>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int main () {
    ifstream myfile;
    myfile.open ("input.txt");
    // myfile.open ("test.txt");

    if (myfile.is_open()) {
        string line;
        int nStacks = 9;
        // int nStacks = 3;
        vector<stack<char>*> stacks;

        for (int i=0; i < nStacks; i++) {
            stacks.push_back(new stack<char>);
        }
        
        int move = 0;
        int from = 0;
        int to = 0;
        while ( getline (myfile, line) )
        {
            // Populate stacks with input
            if (line.find('[') != -1) {
                for (int i=0; i < nStacks; i++) {
                    if (line.at(i*4 + 1) != ' ') {
                        stacks.at(i)->push(line.at(i*4 + 1));
                    }
                }
                continue;
            }

            if (line == "") { // reverse stacks
                for (auto e : stacks) {
                    queue<char> temp;
                    int size = e->size();
                    for (int i=0; i<size; i++) {
                        temp.push(e->top());
                        e->pop();
                    }
                    for (int i=0; i<size; i++) {
                            e->push(temp.front());
                            temp.pop();
                        }
                }
                continue;
            }
            if (line == " 1   2   3   4   5   6   7   8   9 ") { // ignore empty lines
                continue;
            }
            // if (line == " 1   2   3 ") { // ignore empty lines
            //     continue;
            // }

            // perform commands
            int a = line.find_first_of("m") + 5;
            int b = line.find_first_of("f") - 1;
            int numDigits = b - a;

            move = stoi(line.substr(a,numDigits));
            from = stoi(line.substr(11 + numDigits,1));
            to = stoi(line.substr(16 + numDigits,1));

            for (int i=0; i<move; i++) {
                if (!stacks.at(from - 1)->empty()) {
                    stacks.at(to - 1)->push(stacks.at(from - 1)->top());
                    stacks.at(from - 1)->pop();
                }
            }

        }

        cout << "Top Crates of Each Stack: ";
        for (auto e: stacks) {
            cout << e->top();
        }
        cout << "\n";

        myfile.close();
    }
    return 0;
}