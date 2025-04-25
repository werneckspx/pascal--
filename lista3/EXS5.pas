program exs5;

uses crt;

var num, i,j, aux, aux2, sinal,sinal2,cont ,lol:integer;
    x, solucao,fat,teste: real;

begin;

 {Depois de se declarar as variaveis se l� o valor de x.}

 clrscr;
 writeln ("Digite o valor de X.");
 readln (x);

 {Se retira a parte inteira de x para poder utiliza-la como fim do la�o de
  repeti��o. E se atribui valores as variaveis para que possa entrar nos la�os
  e que de certo a exponencia��o inicial.}

 clrscr;
 lol:= trunc(x);
 aux:=1;
 aux2:=0;
 sinal:=1;

 if lol<0 then
 lol:=lol*(-1);

 {Se cria um la�o que vai ate a variavel x, ent�o se cria uma condi��o para
 definir se a fatorial sera positiva ou negativa e atribui o valor do contador}

 for i:=1 to lol do
     begin
     aux:=aux+1;
     teste:=0;
         if (aux mod 2 =0) then
            sinal2:=-1
            else
            sinal2:=+1;

            cont:=1;

            {Ja no segundo la�o se coloca um contador para definir a quanto
             x sera elevado e se tem as duas condi��es de if para definir de
             quanto a eleva��o de x ser� dividido.}

           for j:=1 to i do
               begin

               cont:=cont+1;

               if (aux2 = 4)  then
                  begin
                  sinal:=-1;
                  end;

               if (aux2 = 1) then
                  begin
                  sinal:=1;
                  end;

              end;

     {Aqui se faz os calculos e vai se atribuindo a divis�o e exponencia��o.}

     aux2:=aux2+sinal;
     fat:= exp(cont * ln(x));
     fat:= sinal2*(fat/aux2);
     teste:=teste+fat;
     solucao:=solucao+fat;
     writeln (teste:0:2);
     delay (400);

     end;

   {E por fim se apresenta ao usuario o resultado final.}
 clrscr;
 writeln ("O resultado da fatorial �, ", solucao:0:10 ," .");
 writeln ("");
 write ("Para encerrar o programa pressione qualquer tecla.");
 readkey;

end.
