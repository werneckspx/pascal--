program exs16;

uses crt;

var preco, desconto: real;

begin;

 //depois de se declarar as variaveis se apresenta o programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa recebera o preco de um produto e calculara,");
 writeln ("o desconto deste e o novo preco.");
 write ("para comecar tecle enter.");
 readkey;

 //se l� o pre�o do produto para definir o valor do desconto.

 clrscr;
 writeln ("primeiramente digite o preco do produto.");
 readln (preco);

 clrscr;

 //se define o valor do desconto com uma cadeia de ifs onde a condi��o atendida
 //definir� de quanto sera o desconto.

 if (preco > 100) then
    begin
    desconto:= preco*0.15;
    end

    else if (preco <= 100) and (preco > 30) then
            begin
            desconto:= preco*0.10;
            end

            else if (preco <= 30) then
                    begin
                    desconto:= preco*0;
                    end;

 //ent�o se apresenta os resultados ao usuario.

 writeln ("o valor de desconto e de ", desconto:0:2 , " .");
 writeln ("o novo valor do produto e ", preco-desconto:0:2 , " .");
 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.
