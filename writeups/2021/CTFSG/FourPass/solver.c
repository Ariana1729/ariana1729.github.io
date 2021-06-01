#include<stdio.h>
#include<stdlib.h>
#include<math.h>

//#define MAX 10000
//#define sMAX 100
#define MAX 100000000
#define sMAX 10000

int main(){
    printf("Generating squarefree smooth numbers\n");

    unsigned int i,j,k;
    unsigned int *sieve = malloc(MAX*sizeof(unsigned int));
    
    unsigned int *sqs_ls[9];
    unsigned int sqs_cnt[9]={0};

    for(i=2;i<MAX;++i)sieve[i]=0;
    for(i=2;i<MAX;++i){
        if(sieve[i] == -1)continue;
        if(sieve[i] == 0){
            for(j=2;i*j<MAX;++j){
                if(j%i==0)sieve[j*i]=-1;
                else{
                    if(sieve[j*i]!=-1)sieve[j*i]++;
                }
            }
            sieve[i] = 1;
        }
    }

    for(i=2;i<10;++i){printf("[DEBUG] %d %d\n",i,sieve[i]);}

    for(i=2;i<MAX;++i){
        if(sieve[i]!=-1)sqs_cnt[sieve[i]-1]++;
    }

    for(i=0;i<9;++i){
        printf("Number of square free numbers with %d factors: %d\n",i+1,sqs_cnt[i]);
        sqs_ls[i] = malloc(sqs_cnt[i]*sizeof(unsigned int));
        for(j=2,k=0;j<MAX;++j){
            if(sieve[j]==i+1){
                sqs_ls[i][k] = j;
                ++k;
            }
        }
        printf("[DEBUG] ");
        for(k=0;k<10;++k){printf("%d ",sqs_ls[i][k]);}
        printf("\n");
    }

    // all the prime computations done now
    
    unsigned long int A,B,m;
    unsigned long int sol;
    while(1){
        printf("A = ");
        scanf("%u",&A);
        printf("B = ");
        scanf("%u",&B);
        sol = A*B;
        m = (A<B)?A:B;
        for(i=0;i<9;++i){
            for(j=k=0;j<sqs_cnt[i];++j){
                if(sqs_ls[i][j] > m)break;
                if(i%2==0)sol-=(A/sqs_ls[i][j]) * (B/sqs_ls[i][j]);
                else sol+=(A/sqs_ls[i][j]) * (B/sqs_ls[i][j]);
            }
        }
        printf("f(%u,%u)=%lu\n",A,B,sol);
    }

    return 0;
}
