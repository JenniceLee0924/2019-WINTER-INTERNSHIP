//
//  main.cpp
//  drive_test
//
//  Created by Jennice Lee on 10/17/19.
//  Copyright © 2019 Jennice Lee. All rights reserved.
//

#include <iostream>
#include "multi.h"
#include "sum.h"

using namespace std;
int main() {
    int age = 70;
    int age2 = 16;
    bool isNotIntox = true;
    if((age)>=1 && (age<16)){
        cout << "Can't Drive"<< endl;
    }
    else if(!isNotIntox){
        cout << "Can't Drive" << endl;
    }
    else if((age>= 80 && age>100)||(age - age2>5)){
        cout << "Can't Drive" << endl;
    }
    else
        cout << "Can Drive" << endl;

    cout << multi(1, 1) << endl;
    cout << sum(1,1) << endl;

    return 0;
}
