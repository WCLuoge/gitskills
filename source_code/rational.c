#include <stdio.h>

struct rational {
  int numerator, denominator;
};

int m_gcd(int a, int b);
struct rational make_rational(int numerator, int denominator);
struct rational add_rational(struct rational a, struct rational b);
struct rational sub_rational(struct rational a, struct rational b);
struct rational mul_rational(struct rational a, struct rational b);
struct rational div_rational(struct rational a, struct rational b);
void print_rational(struct rational a);

int main(void)
{
  struct rational a = make_rational(1,8);
  struct rational b = make_rational(0,8);
  print_rational(add_rational(a,b));
  print_rational(sub_rational(a,b));
  print_rational(mul_rational(a,b));
  print_rational(div_rational(a,b));
  return 0;
}

int m_gcd(int a, int b)
{
  if(b==0) return a;
  else return m_gcd(b, a%b);
}
struct rational make_rational(int numerator, int denominator)
{
  struct rational r;
  if(denominator==0)
  {
    r.numerator=1;
    r.denominator=-1;
  }
  else if(numerator==0)
  {
    r.numerator=0;
    r.denominator=1;
  }
  else
  {
    int gcd=m_gcd(numerator,denominator);
    gcd= gcd*denominator>0?gcd:-gcd;
    numerator /=gcd;
    denominator /=gcd;
    r.numerator=numerator;
    r.denominator=denominator;
  }
  return r;
}
struct rational add_rational(struct rational a, struct rational b)
{
  struct rational r;
  int numerator, denominator;
  numerator = a.numerator*b.denominator+b.numerator*a.denominator;
  denominator=a.denominator*b.denominator;
  r=make_rational(numerator,denominator);
  return r;
}
struct rational sub_rational(struct rational a, struct rational b)
{
  struct rational r;
  int numerator, denominator;
  numerator = a.numerator*b.denominator-b.numerator*a.denominator;
  denominator=a.denominator*b.denominator;
  r=make_rational(numerator,denominator);
  return r;
}
struct rational mul_rational(struct rational a, struct rational b)
{
  struct rational r;
  int numerator, denominator;
  numerator = a.numerator*b.numerator;
  denominator=a.denominator*b.denominator;
  r=make_rational(numerator,denominator);
  return r;
}
struct rational div_rational(struct rational a, struct rational b)
{
  struct rational r;
  int numerator, denominator;
  numerator = a.numerator*b.denominator;
  denominator=a.denominator*b.numerator;
  r=make_rational(numerator,denominator);
  return r;
}
void print_rational(struct rational a)
{
  if(a.denominator==1) printf("%d\n",a.numerator);
  else if(a.denominator==-1)printf("%s\n","NAN");
  else printf("%d/%d\n",a.numerator,a.denominator);
}
