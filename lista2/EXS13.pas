program exs13;

uses crt;

var preco, novo : real;
    clas: string;

begin;

 //depois de se declarar as variaveis se da o resumo do programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa recebera o preco de um produto e lhe mostrara o novo pre�o e classificacao.");
 write ("para prosseguir tecle enter.");
 readkey;

 clrscr;
 writeln ("primeiramente digite o preco do produto.");
 readln (preco);

 //entao se le o preco do produto para se calcular o novo pre�o.

 clrscr;

 //o novo pre�o � calculado por uma cadeia de ifs onde sera definido o aumento que o produto ira receber.

 if (preco > 100) then
    begin
    novo:= preco* 1.15;
    end

    else if (preco <= 100) and (preco > 50) then
            begin
            novo:= preco* 1.10;
            end

            else if (preco <= 50) then
                    begin
                    novo:= preco * 1.05;
                    end;

 //a classifica��o � feita sobre o novo pre�o em uma cadeia de ifs onde cada condi��o dara a classifica��o.

 if (novo > 200) then
    begin
    clas:="Muito caro";
    end

    else if (novo <= 200) and (novo > 120) then
            begin
            clas:= "Caro";
            end

            else if (novo <= 120) and (novo > 80) then
                    begin
                    clas:= "Normal";
                    end

                    else if (novo <= 80) then
                            begin
                            clas:= "Barato";
                            end;

 //Ent�o se apresenta ao usuario o novo pre�o e a classifica��o do produto.

 writeln ("O novo preco do produto e de ", novo:0:2 , " .");
 writeln ("A classificacao e de ", clas , " .");
 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.