program exs11;

uses crt;

var sal, aumento: real;

begin;

 //depois de se declarar as variaveis se apresenta o programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa recebera seu salario e calculara seu novo salario.");
 write ("para prosseguir tecle enter.");
 readkey;

 clrscr;
 writeln ("por favor informe o seu salario.");
 readln (sal);

 //ent�o se l� o valor do salario e a partir dele se come�a uma cadeia de ifs para definir quanto sera o aumento.

 clrscr;

 if (sal > 900) then
    begin
    aumento:= sal*0;
    end

    else if (sal <= 900) and (sal > 600) then
            begin
            aumento:= sal*0.05;
            end

            else if (sal <= 600) and (sal > 300) then
                    begin
                    aumento:= sal*0.10;
                    end

                    else if (sal <= 300) then
                            begin
                            aumento:= sal*0.15;
                            end;


  //ent�o so resta apresentar ao usuario os resultados.

  writeln ("seu aumento foi de ", (aumento):0:2 , " .");
  writeln ("seu novo salario e de ", (sal+aumento):0:2 , " .");
  writeln (" ");
  write ("para encerrar o programa precione qualquer tecla");
  readkey;

end.