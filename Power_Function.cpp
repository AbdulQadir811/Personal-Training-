/******************************************************************************

                              ⦁	Given are three numbers x, y and z such that x = yz. Write a function to compute x.
*******************************************************************************/

#include <iostream>

using namespace std;
int MyFunction( int y,int z)
{
   int result = 1 ;
   for(int i =1 ; i < z+1 ; i++)
   {
       result *= y;
   }
   return result;
}

int main()
{
  cout<< ( MyFunction(2,1));
    return 0;
}
