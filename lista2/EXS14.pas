program exs14;

uses crt;

var sal, novo : real;

begin;

 //depois de se declarar as variaveis se apresenta o programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa recebera seu salario e calculara seu novo salario com aumento.");
 write ("para comecar tecle enter.");
 readkey;

 //depois se le o salario do usuario para calcular o novo.

 clrscr;
 writeln ("primeiramente digite o seu salario.");
 readln (sal);

 clrscr;

 //se calcula o novo salario do usuario com uma sequencia de ifs onde as condi��es definem de quanto ser� o aumento.

 if (sal > 1000) then
    begin
    novo:= sal*1.05;
    end

    else if (sal <= 1000) and  (sal > 800) then
            begin
            novo:= sal*1.10;
            end

            else if (sal<= 800) and (sal > 700) then
                    begin
                    novo:= sal*1.20;
                    end

                    else if (sal <= 700) and (sal > 500) then
                            begin
                            novo:= sal*1.30;
                            end

                            else if (sal <= 500) and (sal > 300) then
                                    begin
                                    novo:= sal*1.40;
                                    end

                                    else if (sal <= 300) then
                                            begin
                                            novo:= sal*1.50;
                                            end;

 //Ent�o so resta apresentar ao usuario os resultados.

 writeln ("Seu novo salario e de ", novo:0:2 , " .");
 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.