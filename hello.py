#include<stdio.h>
int gcd(int j, int k){
	if(j % k == 0){
		return k;
	}
	return gcd(k, j % k);
}
int main(){
	int j = 1988, k = 1617;
	printf("GCD = %d\n", gcd(j, k));
	return 0;
}