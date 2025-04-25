program exs25;

uses crt;

var faltas, h  : real;
    extras, premio : integer;

begin;

 //Depois de se declarar as variaveis se da o resumo do programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa recebera a quantidade de horas extras e horas falta e,");
 writeln ("calculara o valor do premio.");
 write ("para comecar tecle enter.");
 readkey;

 //o usuario declarar� as horas extras e as horas faltas dele.

 clrscr;
 writeln ("Primeiramente digite a quantidade de horas extras feitas.");
 readln (extras);

 clrscr;
 writeln ("Agora digite a quantidade de horas faltas.");
 readln (faltas);

 //ent�o se faz o calculo de horas extras menos 66% da quantidade de cada hora falta.

 h:= extras- (2/3*(faltas));

 //se mutiplica esse valor por 60 para descobrir a quantidade de minutos.

 h:= h*60;

 //Ent�o se faz uma cadeia de ifs para definir qual ser� o premio do usuario.

 if (h >= 2500) then
    begin
    premio:= 500;
    end

    else if (h < 2400) and (h >= 1800) then
            begin
            premio:= 400;
            end

            else if (h < 1800) and (h >= 1200) then
                    begin
                    premio:= 300;
                    end

                    else if (h < 1200) and (h >= 600) then
                            begin
                            premio:= 200;
                            end

                            else if (h < 600) then
                                    begin
                                    premio:= 100;
                                    end;


  //ent�o so resta apresentar ao usuario o valor do premio.

  writeln ("O premio recebido e de ", premio , " .");
  writeln (" ");
  write ("Para encerrar o programa precione qualquer tecla.");
  readkey;

end.