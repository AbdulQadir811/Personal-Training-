#include <iostream>
#include <string>

using namespace std;
string palindrome_checker(string str)
{
    int len = str.length();
    string result = "";
    for(int i = 0 ; i< len/2 ; i++ )
    {
        if(str[i] != str[(len-1)-i])
        {
            result = str + " is not a palindrome string";
            return result;
        }
    }
    
    result =  str + " is a palindrome string";
}

int main()
{
    string mystr = "civic";
   cout<<  palindrome_checker(mystr) << endl;
    mystr = "baab";
    cout<<  palindrome_checker(mystr) << endl;
    mystr = "ab";
    cout<<  palindrome_checker(mystr) << endl;
    
    return 0;
}
