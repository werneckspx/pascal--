program EXS2;

uses crt;

var n1, i , j, fat: integer;
    e: real;

begin;

 clrscr;
 writeln ("caro usuario este programa recebera um numero inteiro a sua escolha e adicionara a 1 uma fracao ate chegar,");
 writeln ("no numero escolhido.");
 write ("para prosseguir tecle enter.");
 readkey;

 clrscr;
 writeln ("por favor digite um numero inteiro e positivo.");
 readln (n1);

 e:=1;

 for i:=1 to n1 do

    begin
    fat:=1;

     for j:=1 to i do
         begin
         fat:= fat*j;
         end;

       e:= e+1/fat;
     end;

 writeln ("E igual a ", e:0:6 , " .");
 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.
