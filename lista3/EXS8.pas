program exs8;

uses crt;

var n1,n2,n3,i,qtd,cont:longint;

begin;

 {Depois de se declarar as variaveis se le a quantidade de numeros que o usuario
 deseja e se le os 3 numeros.}

 clrscr;
 writeln ("Digite a quantidade de numeros voc� deseja ter na sequencia.");
 readln (qtd);
 writeln ("Digite o primeiro numero.");
 readln (n1);
 writeln ("Digite o segundo numero.");
 readln (n2);
 writeln ("Digite o terceiro numero.");
 readln (n3);

 clrscr;

 {Se coloca em um la�o de repeti��o para ir escrevendo os valores de acordo
 com regras ja estabelicidas e vai se multiplicando esses valores. Se coloca
 comandos break no meio do la�o por que se por acaso o contador ficar igual a
 quantidade de termos que o usuario deseja no meio do la�o ele n�o ira parar
 ate a checagem inicial.}

 while cont<>qtd do
      begin
      write (n1," ");
      n1:=n1*2;
      cont:=cont+1;

      if cont=qtd then
         break;

      write (n2," ");
      n2:=n2*3;
      cont:=cont+1;

      if cont=qtd then
         break;

      write (n3," ");
      n3:=n3*4;
      cont:=cont+1;
      end;

 writeln ("");
 writeln ("");
 write ("Para encerrar o programa pressione qualquer tecla.");
 readkey;

end.
