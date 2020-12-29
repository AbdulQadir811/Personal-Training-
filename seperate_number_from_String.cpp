#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int StringConverter(string mystr)
{
    int lenghtstr = mystr.length();
    int exponent  = 0;
    int result = 0;
    
    for(int i = lenghtstr-1; i >-1 ; i --)
    {
        if((int)(mystr[i]) > 48 && (int)(mystr[i]) < 58)
        {   
            result  += (((int)(mystr[i]))-48) * pow(10,exponent);
            exponent+=1;
        }
        
    }
    return result;
}

int main()
{
  cout<<(StringConverter("-12f34"));
  return 0;
}
