#include<stdio.h>

void swap(int *p1,int *p2)

{

int t=*p1;

*p1=*p2;

*p2=t;

}

void permutation(int a[],int index,int size, int m)

{

if(index==m)

{

for(int i=0;i<m;i++)

printf("%d ",a[i]);

printf("\n");

}

else

{

for(int j=index;j<size;j++)

{

swap(&a[j],&a[index]);

permutation(a,index+1,size,m);//此处用到递归思想

swap(&a[j],&a[index]);

}

}

}

int main()

{

int n,m;

scanf("%d %d",&n,&m);

int a[n];

for(int i=0;i<n;i++)

a[i]=i+1;

permutation(a,0,n,m);

return 0;

}
