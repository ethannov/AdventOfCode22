#include <iostream>
#include <fstream>
using namespace std;

int main () {
    ifstream myfile;
    myfile.open ("input.txt");

    // Find if a pair fully contains the other
    if (myfile.is_open()) {
        string line;
        string pair1;
        string pair2;
        int p1start;
        int p1end;
        int p2start;
        int p2end;
        int counter = 0;

        while ( getline (myfile, line) )
        {
            pair1 = line.substr(0, line.find(","));
            pair2 = line.substr(line.find(",")+1, -1);

            p1start = atoi( pair1.substr(0, pair1.find("-")).c_str() );
            p1end = atoi( pair1.substr(pair1.find("-")+1, -1).c_str() );
            p2start = atoi( pair2.substr(0, pair2.find("-")).c_str() );
            p2end = atoi( pair2.substr(pair2.find("-")+1, -1).c_str() );

            if ( (p1start <= p2start && p1end >= p2end) || (p2start <= p1start && p2end >= p1end)) {
                counter++;
                // cout << "*";
            }

            // cout << line << '\n';
            // cout << pair1 << "+" << pair2 << '\n';
            // cout << p1start << " " << p1end << '\n';
            // cout << p2start << " " << p2end << '\n';
        }
        cout << "Number of fully overlapped pairs: " << counter << "\n";
        myfile.close();
    }
    return 0;
}