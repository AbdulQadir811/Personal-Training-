#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
void Maxof()
{
    int x = 3;
    int arr[6] = {1,2,3,4,5,6};
     int n = sizeof(arr)/4;
    for(int i = 0 ;i< (n)-2;i++ )
    {
        int max = 0;
        for(int j= i;j<i+x;j++)
        {
            if(max<arr[j])
            {
                max = arr[j];
            }
        
        
        }
          cout << max <<endl;
    }
}

int main() {
 
  Maxof();
}