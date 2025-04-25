program exs15;

uses crt;

var sal, hora_t, hora_e, dep: integer;
    sal_bru, sal_liq, val_ht, val_he, imp, grat : real;

begin;

 //depois de se declarar as variaveis se apresenta o programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa calculara seu salario de acordo com o valor do salario minimo,");
 writeln ("da quantidade de horas trabalhadas e extras, e dos dependentes.");
 write ("para prosseguir tecle enter.");
 readkey;

 //ent�o se le os valores de salario minimo, da quantidade de horas trabalhadas e horas extras, e a quantidade de dependentes.

 clrscr;
 writeln ("por favor digite o valor do salario minimo.");
 readln (sal);

 clrscr;
 writeln ("agora digite a quantidade de horas trabalhadas.");
 readln (hora_t);

 clrscr;
 writeln ("agora digite a quantidade de dependentes.");
 readln (dep);

 clrscr;
 writeln ("agora digite a quantidade de horas extras.");
 readln (hora_e);

 //o valor da hora trabalhada sera o valor do salario minimo divido por 5.
 //e da hora extra o valor da hora trabalhada vezes 1.5

 val_ht:= sal/5;
 val_he:= val_ht*1.5;

 // o salario bruto � calculado pela quantidade de horas trabalhadas * o seu valor, pela quantidade de horas extras * o seu valor
 // e pela quantidade de dependentes * 32.

 sal_bru:=   (val_ht * hora_t)+(dep * 32)+(val_he * hora_e);


 //para descobrir o imposto � nescessario uma cadeia de ifs
 //se o salario for maior que 500 entao o imposto sera de 20%, se estiver entre 500 e 200 sera de 10%, caso menor que 200 n�o ha imposto.

 if (sal_bru > 500) then
    begin
    imp:= sal_bru * 0.20;
    end

    else if (sal_bru <= 500) and (sal_bru >= 200) then
            begin
            imp:= sal_bru * 0.10;
            end

            else if (sal_bru < 200) then
                    begin
                    imp:= 0;
                    end;


 //o salario liquido � calculado pela subtra��o do imposto sobre o salario bruto.

 sal_liq:=  sal_bru - imp;

 //aqui ja se calcula a bonifica��o e apresenta ao usuario o salario recebido dele.
 //caso o salario seja maior que 350 a bonifica��o � de 50 e basta ser somada ao salario liquido.
 //caso seja menor ou igual a 350 a bonifica��o � de 100 e da mesma maneira so � nescessario somar ao salario liquido.

 if (sal_liq > 350) then
    begin
    writeln ("caro usuario seu novo salario sera de ", sal_liq+50:2:2, " .");
    end

    else if (sal_liq <= 350) then
            begin
            writeln ("caro usuario seu novo salario sera de ", sal_liq+100:2:2, " .");
            end;

 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.
