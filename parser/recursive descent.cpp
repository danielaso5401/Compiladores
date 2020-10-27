#include <iostream>
#include <stdlib.h>
#include <fstream>
using namespace std;


int point = 0;
void E(); // E -> T | T + E
void F(); // F -> T 
void G(); // G -> T + E
void T(); // T -> int | int * T | (E)
void U(); // U -> int
void V(); // V -> int * T
void W(); // W -> (E)*
string expr;
string text;



int main(){
	
  	ifstream archivo;
	archivo.open("entrada.txt", ios::in);
	while(!archivo.eof())
	{
		getline(archivo,expr);
	}
	archivo.close();
  
  	cout<<expr<<endl;
  
  for(int i=0; i<expr.length(); i++){
  	if('t'==expr[i]){
  		text.append("i");
	  }
	else if('+'==expr[i]){
		text.append("+");
	}
	else if('*'==expr[i]){
		text.append("*");
	}
	else if('('==expr[i]){
		text.append("(");
	}
	else if(')'==expr[i] ){
		text.append(")");
	}
  }
  expr=text;
  int tam = expr.length();
  expr += "$";
  E();
  if (tam == point)
    cout << "Aceptado" << endl;
  else
    cout << "Rechazado" << endl;
}

void E() 
{
  cout << "E-> T | T + E" << endl;
  F();
  G();
}

void F ()
{
	cout << "F-> T" << endl;
	T();
}

void G() 
{
  if (expr[point] == '+') 
  {
    point++;
    cout << "G-> T + E" << endl;
    T();
    E();
  }
}

void T() 
{
  cout << "T-> int | int * T | (E)" << endl;
  U();
  V();
  W();
}

void U()
{
	
	if (isalpha(expr[point])) 
	{
	    point++;
	    cout << "U-> int" << endl;
  	}
}
void V() 
{
  if (expr[point] == '*') 
  {
    point++;
    cout << "V-> int * T" << endl;
    U();
    T();
  }

}

void W() 
{
  if (expr[point] == '(') 
  {
    point++;
    cout << "W-> (E)" << endl;
    E();
    if (expr[point] != ')') 
	{
      cout << "Rechazado" << endl;
      exit(0);
    }
    point++;
   }

}

