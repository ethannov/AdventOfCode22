#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
using namespace std;

struct file {
    string name;
    int size;
};

class dir {
    public:
    string name;
    vector<file*> files;
    vector<dir*> dirs;
    int size = 0;
    dir* parent = nullptr;

    dir();
    dir(string x) {name = x;}
    bool contains(string x) {
        for (auto e : dirs) {
            if (e->name == x) {
                return true;
            }
        }
        return false;
    };
};

class fileTree {
    public:
        fileTree(string rootName);
        void add_dir(dir x);
        dir* get_root() {return root;}
        vector<dir*> postOrder();
        void get_size(dir x, int size);
        void set_size(dir x, int size);
    private:
        dir* root = nullptr;
};

fileTree::fileTree(string rootName) {
    root = new dir(rootName);
}

vector<dir*> fileTree::postOrder() {
  vector<dir*> dirs;
  stack<pair<dir*, int>> st;
  int i = 0;
  dir* x = root;
  while (x != nullptr || st.size() > 0) {
    if (root != NULL) {
        
    }
  }
  return dirs;
}

//https://www.geeksforgeeks.org/iterative-postorder-traversal-of-n-ary-tree/
vector<dir*> postorder(dir* root) 
{
    int currentRootIndex = 0;
    vector<dir*> postorderTraversal;
    stack<pair<dir*, int>> st;
    while (root != NULL || st.size() > 0)
    {
        if (root != NULL)
        {
             
            // Push the root and it's index
            // into the st
            st.push(pair(root, currentRootIndex));
            currentRootIndex = 0;
 
            // If root don't have any children's that
            // means we are already at the left most
            // node, so we will mark root as NULL
            if (root->dirs.size() >= 1)
            {
                root = root->dirs[0];
            }
            else
            {
                root = NULL;
            }
            continue;
        }
 
        // We will pop the top of the st and
        // push_back it to our answer
        pair<dir*, int> temp = st.top();
        st.pop();
        postorderTraversal.push_back(temp.first);
 
        // Repeatedly we will the pop all the
        // elements from the st till popped
        // element is last children of top of
        // the st
        while (st.size() > 0 && temp.second ==
                st.top().first->dirs.size() - 1)
        {
            temp = st.top();
            st.pop();
             
            postorderTraversal.push_back(temp.first);
        }
 
        // If st is not empty, then simply assign
        // the root to the next children of top
        // of st's node
        if (st.size() > 0)
        {
            root = st.top().first->dirs.at(temp.second + 1);
            currentRootIndex = temp.second + 1;
        }
    }
    return postorderTraversal;
}

int main() {
    ifstream myfile;
    myfile.open ("input.txt");
    //myfile.open ("test.txt");

    vector<string> commands;
    if (myfile.is_open()) {
        string line;
        while ( getline (myfile, line) )
        {
            commands.push_back(line);
        }
        myfile.close();
    }

    // create tree
    dir* currDir;
    fileTree tree("/");
    bool is_ls = false;
    for (auto line : commands) {
        // if cd
            // if cd .., point to parent of current dir
            // if cd name
                // if name exists in tree, point to that dir
                // if name doesn't exist, create dir and point to it
        if (line == "$ cd /") {
                    currDir = tree.get_root();
                }
                else if (line.substr(0, 4) == "$ cd") {
                    if (line == "$ cd ..") {
                        currDir = currDir->parent;
                    }
                    else {
                        int i = line.find_last_of(' ');
                        string name = line.substr(i+1, line.length()-i);
                        
                        if (!currDir->contains(name)) {
                            dir* temp = new dir(name);
                            temp->parent = currDir;
                            currDir->dirs.push_back(temp);
                            currDir = temp;
                        }
                        else {
                            for (auto e : currDir->dirs) {
                                if (e->name == name) {
                                    currDir = e;
                                }
                            }
                        }
                    }
                }
    // if ls, continue
    // if dir and doesn't exist in current dir, add dir to current dir
    // if file and doesn't exit in currnt dir, add file to current dir
        if (line.substr(0, 4) == "$ ls") {
            is_ls = true;
            continue;
        } 
        else if (line.substr(0, 4) == "$ cd") {
            is_ls = false;
        }

        if (is_ls) {
            if (line.substr(0, 3) != "dir") {
                file* newFile = new file;
                int i = line.find_first_of(' ');
                newFile->size = stoi(line.substr(0, i));
                newFile->name = line.substr(i+1, line.length() - i);

                currDir->files.push_back(newFile);
            }
        }
    }


    // set sizes of dirs in tree
    vector<dir*> postorder_dirs = postorder(tree.get_root());
    for (auto e : postorder_dirs) {
        for (auto file : e->files) {
            e->size += file->size;
        }
        for (auto dir : e->dirs) {
            e->size += dir->size;
        }
    }

    // find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes
    int sum = 0;
    for (auto e : postorder_dirs) {
        if (e->size <= 100000) {
            sum += e->size;
        }
    }

    cout << "Answer: " << sum << "\n";

    // The total disk space available to the filesystem is 70000000. 
    // To run the update, you need unused space of at least 30000000. 
    // You need to find a directory you can delete that will free up enough space to run the update.
    // Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. 
    // What is the total size of that directory?
    int disk = 70000000;
    int update = 30000000;
    int spaceUsed = tree.get_root()->size;
    int spaceUnused = disk - spaceUsed;
    int spaceNeeded = update - spaceUnused;

    dir* deleteCandidate = tree.get_root();
    for (auto e : postorder_dirs) {
        if (e->size >= spaceNeeded) {
            if (e->size < deleteCandidate->size) {
                deleteCandidate = e;
            }
        }
    }

    cout << "Answer: " << deleteCandidate->size << "\n";
    return 0;
}
