#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 20

int histogram[10]={0};

void get_histogram(int upper_bound);
void print_histogram();

int main(void)
{
  get_histogram(10);
  print_histogram();

  return 0;
}

void get_histogram(int upper_bound)
{
  srand(time(NULL));
  for(int i=0; i<N; i++)
    histogram[rand()%upper_bound]++;
}

void print_histogram()
{
  int max=histogram[0];
  printf("%d", 0);
  for(int i=1; i<10; i++)
  {
    printf(" %d",i);
    if(histogram[i]>max) max=histogram[i];
  }
  printf("\n");
  for(int k=0; k<max; k++)
  {
    if(histogram[0]>0) printf("*");
    else printf(" ");
    histogram[0]--;
    for(int i=1; i<10; i++)
    {
      if(histogram[i]>0)
        printf(" *");
      else printf("  ");
      histogram[i]--;
    }
    printf("\n");
  }

}
