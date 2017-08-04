#include<stdio.h>
#include<string.h>

int main()
{
	//1 is lie
	//A and B don't lie on Sunday
	int A[7]={1,0,1,0,1,0,0};
	int B[7]={0,1,0,1,0,1,0};
	int index;
	int tmp;

	for (index=0; index<7; index++)
	{
		tmp = (index >= 2)?(index-2):(index+5);
#if 0
		//the liar is A
		if (A[index]  == 1 && A[tmp] == 0 && B[index] == 0 && B[tmp] == 1)
		{
			printf("Today is %d\n", index+1);
		}
		//the liar is B
		if (A[index]  == 0 && A[tmp] == 1 && B[index] == 1 && B[tmp] == 0)
		{
			printf("Today is %d\n", index+1);
		}
#endif
		if ((A[index] ^ A[tmp]) && (B[index] ^ B[tmp]) && (A[index] ^ B[index]))
		{
			printf("Today is %d\n", index+1);
		}		
	}
	return 0;
}
