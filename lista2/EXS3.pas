program exs3;

uses crt;

var n1,n2: real;

begin;

 //depois de se declarar as variaveis se da o resumo do programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa recebera dois numeros e lhe dira qual o menor.");
 write ("para comecar tecle enter.");
 readkey;

 //entao se le as notas que ele vai digitar.

 clrscr;
 writeln ("por favor digite o primeiro numero.");
 readln (n1);

 clrscr;
 writeln ("agora digite o segundo numero.");
 readln (n2);

 clrscr;

 //ent�o na cadeia de ifs se apresenta qual o numero � o maior.

 if (n1 > n2) then
    begin
    writeln ("o numero menor e ", n2:0:2 , " .");
    end

    else if (n2 > n1) then
            begin
            writeln ("o numero menor e ", n1:0:2 , " .");
            end

            else if (n1 = n2) then
                    begin
                    writeln ("os dois numeros sao iguais.");
                    end;

 writeln (" ");
 writeln ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.
