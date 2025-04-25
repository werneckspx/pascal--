program exs14;

uses crt;

var sal,bon,aux,novo_sal: real;

begin;

 //depois de se declarar as variaveis se da um resumo do programa para o usuario

 clrscr;
 writeln ("caro usuario este programa lhe mostrara seu novo salario com bonificacao e auxilio escola.");
 write ("para prosseguir tecle enter.");
 readkey;

 // entao se le o salario dele para se fazer os calculos de bonifica��o e auxilio escola.

 clrscr;
 writeln ("por favor digite o seu salario.");
 readln (sal);

 // o calculo da bonifica��o � feita em uma cadeia de ifs onde a condi��o atendida sera somada ao salario inicial
 // juntamente com o auxilio escola.

 if (sal > 1200) then
    begin
    bon:= 0;
    end

    else if (sal <= 1200) and (sal >= 500) then
            begin
            bon:= sal*0.12;
            end

            else if (sal < 500) then
                 begin
                 bon:= sal*0.05;
                 end;


  //como o auxilio escola so tem duas condi��es se a primeira n�o for atendida automaticamente sera calculada a segunda

 if (sal > 600) then
    begin
    aux:= 100;
    end

    else
        begin
        aux:= 150;
        end;

 //ent�o a unica coisa restante � calcular o novo salario e o apresentar ao usuario.

 novo_sal:= sal+bon+aux;

 clrscr;
 writeln ("caro usuario seu novo salario e ", novo_sal:4:2 , " .");
 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.
