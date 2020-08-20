#include<stdio.h>
//O(n) = n
int test_1(int n) {
	int sum = 0;
        for(int i=1; i<=n; i++) {
	    sum = sum + i;
	}
    return sum;
}

//O(n) = n^2
int test_2(int n) {
    int sum = 0;
        for(int i=1 ; i <= n; i++) {
	    for(int j=1; j<=n; j++) {
	        sum = sum + i * j;
	    }
	}
    return sum;
}

//addition
int test_3(int n) {
    int result;
    int sum_1 = 0;
    for(int i=1; i<=n; i++) {
        sum_1 = sum_1 + i;
    }

    int sum_2 = 0;
        for(int i=1 ; i <= n; i++) {
	    for(int j=1; j<=n; j++) {
	        sum_2 = sum_2 + i * j;
	    }
	}
    result = sum_1 + sum_2;
    return result;
}

//multiplication
int test_4(int n) {
    int ret = 0;
        for(int i=1 ; i <= n; i++) {
	    ret = ret + test_1(n);
	}
    return ret;
}

void main() {
    int res_1, res_2, res_3, res_4;
    res_1 = test_1(10);
    res_2 = test_2(10);
    res_3 = test_3(10);
    res_4 = test_4(10);
    printf("%d\n%d\n%d\n%d\n",res_1,res_2, res_3, res_4);
}

