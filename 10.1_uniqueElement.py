""" https://www.codingninjas.com/studio/problems/find-unique_625159?source=youtube&campaign=love_babbar_codestudio1&utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_codestudio1

the above is the link for question 

2M+1 where M elements are repeated twice, this twice is important because we XOR(exclusive or) (^) all elements of array with 0 and print the result. In a way question is very specific
because it has twice repeatitions which will cancel themselves. in the end it will be 0 0 0 7 0 0 and then xor of 0 and any no is the no itself so 7 ^ 0 is 0
So the code will be

# int findUnique(int *arr, int size)
# {
#     int i;
#     for(i=0;i<size;i++)
#     {
#         arr[i]^0;
#     }
# }
 but we need to store result 
int findUnique(int *arr, int size)
{
    int i;
    int result=0;
    for(i=0;i<size;i++)
    {
        result=arr[i]^result;
    }
    return result;
}  """
""" can you visualize the array elements getting shrinked to unique element """

# solution

def findUnique(arr, n) :
    #Your code goes here
    result=0
    for i in range(0,n):
        result=arr[i]^result
    return result

