program exs23;

uses crt;

var horas, grat : integer;
    peri,cat: char;
    sal_min, sal_liq, val_hora, sal_bruto, auxilio, imp : real;

begin;

 {depois de se declarar as variaveis, se apresenta o programa ao usuario.}

 clrscr;
 writeln ("caro usuario te calculara e te mostrara, o valor da hora em funcao do periodo trabalhado, o valor do salario bruto,");
 writeln ("o valor do imposto, sua gratificacao, o auxilio alimentacao, o salario liquido e sua classificacao.");
 write ("para prosseguir tecle enter.");
 readkey;

 clrscr;
 writeln ("por favor digite o valor do salario minimo.");
 readln (sal_min);

 clrscr;
 writeln ("agora digite a quantidade de horas trabalhadas.");
 readln (horas);

 clrscr;
 writeln ("agora digite o periodo que voce trabalha sendo M=matutino, V=vespertino, N=noturno. Lembre-se de colocar letra maiuscula.");
 readln (peri);

 clrscr;
 writeln ("agora digite sua funcao O=operario, G=gerente. Lembre-se de colocar letra maiuscula.");
 readln (cat);

 {ent�o se le as variaveis do salario minimo, da quantidade de horas, do periodo em que o usuario trabalha e de sua
  fun��o, para que se possa realizar os calculos.}

 clrscr;

 //a primeira cadeia de ifs � para definir o valor de cada hora trabalhada.

 if (peri="M") then
    begin
    val_hora:= sal_min*0.10;
    end

    else if (peri="V") then
            begin
            val_hora:= sal_min*0.15;
            end

            else if (peri="N") then
                    begin
                    val_hora:= sal_min*0.12;
                    end;

 sal_bruto:= val_hora*horas;

 //ent�o se abre uma estrutura de case com uma cadeia de ifs interna para se calcular o valor do imposto.

 case cat of

     "O": begin if (sal_bruto >= 300) then
                 begin
                 imp:= sal_bruto*0.05;
                 end

                 else if (sal_bruto < 300) then
                         begin
                         imp:= sal_bruto*0.03;
                         end;
        end;

     "G": begin if (sal_bruto >= 400) then
                 begin
                 imp:= sal_bruto*0.06;
                 end

                 else if (sal_bruto < 400) then
                         begin
                         imp:= sal_bruto*0.04;
                         end;
        end;
 end;

 //ent�o se abre outra cadeia de ifs para se definir de quanto ser� a gratifica��o do usuario.

 if (peri="N") and (horas > 80) then
     begin
     grat:= 50;
     end

     else  begin
           grat:= 30;
           end;

 //ent�o outra cadeia de ifs � aberta para definir de quanto ser� o auxilio alimenta��o do usuario.

 if (cat = "O") or (val_hora <= 25) then
    begin
    auxilio:= sal_bruto/3;
    end

    else   begin
           auxilio:= sal_bruto/2;
           end;

 //se calcula o valor do salario liquido para apresentar ao usuario.

 sal_liq:= sal_bruto - imp + grat + auxilio;

 //ent�o ja na ultima cadeia de ifs se apresenta ao usuario todos os resultados juntamente com sua classifica��o.

 if (sal_liq > 600) then
    begin
    writeln ("o valor de cada hora trabalhada e de ", val_hora:4:2 , " .");
    writeln ("o valor do salario bruto e de ", sal_bruto:4:2 , " .");
    writeln ("o valor de imposto pago e de ", imp:4:2 , " .");
    writeln ("a gratificacao recebida e de ", grat , " .");
    writeln ("o valor do auxilio alimentacao e de ", auxilio:4:2 , " .");
    writeln ("o salario liquido e de ", sal_liq:4:2 , " .");
    writeln ("e sua classificacao e BEM REMUNERADO.");
    end

    else if (sal_liq <= 600) and (sal_liq >= 350) then
            begin
            writeln ("o valor de cada hora trabalhada e de ", val_hora:4:2 , " .");
            writeln ("o valor do salario bruto e de ", sal_bruto:4:2 , " .");
            writeln ("o valor de imposto pago e de ", imp:4:2 , " .");
            writeln ("a gratificacao recebida e de ", grat , " .");
            writeln ("o valor do auxilio alimentacao e de ", auxilio:4:2 , " .");
            writeln ("o salario liquido e de ", sal_liq:4:2 , " .");
            writeln ("e sua classificacao e NORMAL.");
            end

            else if (sal_liq < 350) then
                    begin
                    writeln ("o valor de cada hora trabalhada e de ", val_hora:4:2 , " .");
                    writeln ("o valor do salario bruto e de ", sal_bruto:4:2 , " .");
                    writeln ("o valor de imposto pago e de ", imp:4:2 , " .");
                    writeln ("a gratificacao recebida e de ", grat , " .");
                    writeln ("o valor do auxilio alimentacao e de ", auxilio:4:2 , " .");
                    writeln ("o salario liquido e de ", sal_liq:4:2 , " .");
                    writeln ("e sua classificacao e MAL REMUNERADO.");
                    end;

 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.