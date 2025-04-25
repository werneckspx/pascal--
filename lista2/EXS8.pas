program exs8;

uses crt;

var sal:real;

begin;

 //depois de se coletar as variaveis se apresenta o programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa calculara seu novo salario de acordo com seu salario atual.");
 write ("para comecar tecle enter");
 readkey;

 //entao se le o salario dele para poder calcular de quanto sera o aumento.

 clrscr;
 writeln ("por favor informe seu salario.");
 readln (sal);

 {ent�o se caso o salario do usuario for menor ou igual a 300 se da um aumento de 35% a ele caso contrario
  ele recebe somente 15% de aumento.}

 if (sal <= 300) then
    begin
    writeln ("seu novo salario e de ", (sal*1.35):0:2 , " .");
    end

    else if (sal > 300) then
            begin
            writeln ("seu novo salario e de ", (sal*1.15):0:2 , " .");
            end;


 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.