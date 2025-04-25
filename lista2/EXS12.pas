program exs12;

uses crt;

var sal: real;
    grat: integer;

begin;

 //depois de se declarar as variaveis se da o resumo do programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa lhe mostrara sua gratificacao, e um imposto de 7% sobre o salario sobre ele.");
 write ("tecle enter para iniciar.");
 readkey;

 //ent�o se le o salario dele para calcular a gratifica��o recebida.

 clrscr;
 writeln ("primeiramente digite o seu salario.");
 readln (sal);

 clrscr;

 //se faz uma cadeia de ifs para definir de quanto ser� a gratifica��o.

 if (sal > 900) then
    begin
    grat:= 35;
    end

    else if (sal <= 900) and (sal > 600) then
            begin
            grat:= 50;
            end

            else if (sal <= 600) and (sal > 350) then
                    begin
                    grat:= 75;
                    end

                    else if (sal <= 350) then
                            begin
                            grat:= 100;
                            end;

  //Ent�o so resta apresentar ao usuario os resultados.

  writeln ("seu novo salario � de ", (sal*0.93+grat):0:2 , " .");
  writeln (" ");
  write ("para encerrar o programa precione qualquer tecla.");
  readkey;

end.