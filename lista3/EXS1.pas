program exs1;

uses crt;

const sal=1000;
      percentual=0.015;
      ano=2007;

var   novo: real;
      ano_atual, i: integer;

begin;

 //depois de se declarar as constantes e variaveis se da o resumo do programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa calculara o salario de uma pessoa contratada em 2005 com o salario de 1000$, ");
 writeln ("e recebendo aumento do dobro do percentual do ano anterior sendo que o primeiro e de 1.5%.");
 write ("para prosseguir tecle enter.");
 readkey;

 //se l� o ano atual para poder ser feita a contagem.

 clrscr;
 writeln ("digite o ano atual.");
 readln (ano_atual);

 //se atribui o valor do novo salario.

 novo:= sal*percentual+sal;

 //e na estrutura de repeti��o a cada ano aumentado se aumentar� a porcentagem e consequentemente o salario final.

 clrscr;

  for i:=ano to ano_atual do

  begin
  novo:= novo*(percentual*2)+novo;
  end;

  //E ent�o se apresenta o resultado ao usuario.

 writeln ("novo salario � de , ", novo:0:2 , " .");
 writeln (" ");
 write ("para encerrar precione qualquer tecla.");
 readkey;

end.
