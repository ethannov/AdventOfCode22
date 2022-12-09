// cd ..
// cd __directoryName
// ls

#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

struct file {
    string name;
    int size;
};

struct dir {
    string name;
    vector<file*> files;
    vector<dir*> dirs;
    int size;
};

class fileTree {
    public:
        fileTree();
    private:
        dir* root = nullptr;
};

fileTree::fileTree() {
    root = new dir;
}

int main() {
    
    fileTree christmasTree;
    return 0;
}