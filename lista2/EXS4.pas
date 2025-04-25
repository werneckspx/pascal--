program exs4;

uses crt;

var n1,n2,n3: real;

begin;

 //depois de se declarar as variaveis, se l� os numeros do usuario.

 clrscr;
 writeln ("caro usuario este programa recebera 3 numeros e lhe dira qual o maior deles.");
 write ("para continuar precione qualquer tecla.");
 readkey;

 clrscr;
 writeln ("por favor digite o primeiro numero.");
 readln (n1);

 clrscr;
 writeln ("digite o segundo numero diferente do primeiro.");
 readln (n2);

 clrscr;
 writeln ("agora digite o terceiro numero diferente dos outros 2.");
 readln (n3);

 {se faz uma cadeia de ifs como condi��o um numero maior que os outros dois.
  E se apresenta ao usuario os resultados.}

 if (n1 < n2) and (n1 < n3) then
    begin
    writeln ("O maior numero e ,", n1:0:2 , " .");
    end

    else if (n2 < n1) and (n2 < n3) then
            begin
            writeln ("O maior numero e ", n2:0:2 , " .");
            end

            else if (n3 < n1) and (n3 < n2) then
                    begin
                    writeln ("O maior numero e ,", n3:0:2 , " .");
                    end

                    else begin
                         writeln ("Os numeros nao atenderam as condicoes exigidas.");
                         end;

 writeln (" ");
 write ("Para encerrar o programa precione qualquer tecla.");
 readkey;

end.