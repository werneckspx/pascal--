program exs3;

uses crt;

var numero,i,j: integer;
    fat,n:real;

begin;

 {Depois de se declarar as variaveis se da o resumo do programa ao usuario.}

 clrscr;
 writeln ("Caro usuario este programa recebera um numero e lhe mostrara quantos numeros,");
 writeln ("uma tabela com a fatorial deste valor.");
 write ("para continuar pressione enter.");
 readkey;

 {Ent�o se le o numero para definir ate que numero a fatorial sera calculada.}

 clrscr;
 writeln ("Digite o numero inteiro.");
 readln (numero);

 clrscr;

  {Ent�o se cria dois la�os para definir a fatorial e a soma desta fatorial.}

   for i:=1 to numero do
       begin


           for j:=1 to i do
                begin
                fat:=1;
                fat:= fat/i;
                end;
       n:= n+fat;
       writeln (fat:0:2);
       delay (400);
       end;

 {A unica coisa restante � apresentar os resultados ao usuario.}

  clrscr;
  writeln ("A fatorial do numero,",numero," �, ", n:0:10 , " .");
  writeln ("Para encerrar o programa pressione qualquer tecla.");
  readkey;

end.
