#include<stdio.h>
#include<stdbool.h>

int main(){
	int a = 4;
	if (a != 4)
		a = 2;
somewhere:
	printf("%d",a);
	return 0;
}
