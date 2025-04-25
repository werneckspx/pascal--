program exs10;

uses crt;

var preco, imp, dis : real;

begin;

 //depois de se declarar as variaveis se apresenta ao usuario o resumo do programa.

 clrscr;
 writeln ("caro usuario este programa recebera o valor de custo de um carro e te retornara os valores do,");
 writeln ("imposto, da porcentagem do distribuidor e o valor final.");
 write ("para prosseguir tecle enter.");
 readkey;

 //entao se coleta o preco do carro para definir o valor do imposto e lucro do distribuidor.

 clrscr;
 writeln ("primeiramente digite o valor de preco de custo do carro.");
 readln (preco);

 clrscr;

 {se faz uma cadeia de ifs para atribuir o valor do imposto e do lucro do distribuidor a variaveis declaradas acima.}

 if (preco <= 12000) then
    begin
    imp:= preco*0;
    dis:= preco*0.05;
    end

    else if (preco > 12000) and (preco <= 25000) then
            begin
            imp:= preco*0.15;
            dis:= preco*0.10;
            end

            else if (preco > 25000) then
                    begin
                    imp:= preco*0.20;
                    dis:= preco*0.15;
                    end;


   //ent�o so resta mostrar ao usuario os resultados.

  writeln ("caro usuario o valor do imposto e de ", imp:0:2 , " .");
  writeln ("o valor do lucro do distribuidor e de ", dis:0:2 , " .");
  writeln ("o preco final do carro e de ", (preco+imp+dis):0:2 , " .");
  writeln (" ");
  write ("para encerrar o programa precione qualquer tecla");
  readkey;

end.
