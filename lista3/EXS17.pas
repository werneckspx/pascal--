program exs17;

uses crt;

var qtd:integer;
    sal_carlos,sal_joao:real;

begin

  clrscr;

   {Depois de se declarar as variaveis se l� o salario de carlos.}

        writeln ("Digite o salario de carlos.");
        readln (sal_carlos);
        sal_joao:=sal_carlos/3;
        qtd:=0;

  {Ent�o se coloca em um loop como condi��o que so ira parar quando o salario
  de jo�o for maior que o salario de carlos.}

  while (sal_joao < sal_carlos) do
        begin
        sal_carlos:=sal_carlos*1.02;
        sal_joao:=sal_joao*1.05;
        qtd:=qtd+1;
        end;

        {E se apresenta este resultado ao usuario.}

 clrscr;
 writeln ("Demorar�, ",qtd," meses para o valor de jo�o ser igual ou ultrapassar o de carlos.");
 writeln;
 write ("para encerrar o programa pressione qualquer tecla.");
 readkey;

end.