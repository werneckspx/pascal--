program exs22;

uses crt;

var sal, sal_liq, imp: real;
    tempo, grat: integer;
    clas: char;

begin;

 //depois de se declarar as variaveis se da o resumo do programa ao usuario

 clrscr;
 writeln ("caro usuario este programa calculara e te mostrara o valor do imposto que voce paga, sua gratificacao,");
 writeln ("seu salario liquido e sua classificacao, com base em seu salario.");
 writeln (" ");
 write ("para prosseguir tecle enter.");
 readkey;

 clrscr;
 writeln ("por favor digite o seu salario.");
 readln (sal);

 clrscr;
 writeln ("por favor digite o seu tempo de servico com numeros inteiros, ou seja se voce tem 2 anos e 10 meses de servico");
 writeln ("entao digite 2.");
 readln (tempo);

 //entao se le o sal�rio e o tempo de servi�o do usuario.

 clrscr;

 //a primeira cadeia de ifs � para determinar o valor de imposto pago pelo usuario de acordo com seu salario.

  if (sal >= 700) then
     begin
     imp:= sal*0.12;
     end

     else if (sal < 700) and (sal > 450) then
             begin
             imp:= sal*0.08;
             end

             else if (sal <= 450) and (sal >= 200) then
                     begin
                     imp:= sal* 0.03;
                     end

                     else if (sal < 200) then
                             begin
                             imp:= sal*0.00;
                             end;


  //a segunda cadeia de ifs � para determinar o valor da gratifica��o do usuario de acordo com seu sal�rio,
  //e tempo de servi�o.

  if  (sal > 500) then
      begin
      if (tempo > 3) then
         begin
         grat:= 30;
         end

         else if (tempo <= 3) then
                 begin
                 grat:= 20;
                 end
      end


      else if (sal <= 500) then
              begin
              if (tempo >= 6) then
                 begin
                 grat:= 33;
                 end

                 else if (tempo > 3) and (tempo < 6) then
                 begin
                 grat:= 35;
                 end

                 else if (tempo <= 3) then
                         begin
                         grat:= 23;
                         end

              end;


  //se calcula o valor do sal�rio liquido da seguinte forma:
  //salario - imposto - a gratifica��o que foram obtidos acima.

  sal_liq:= sal-imp+grat;

  //ent�o se come�a uma cadeia de ifs para determinar a classifica��o do usuario de acordo com seu sal�rio liquido.

  if (sal_liq >= 600) then
     begin
     clas:= "C";
     end

     else if (sal_liq > 350) and (sal_liq < 600) then
             begin
             clas:= "B";
             end

             else if (sal_liq <= 350) then
                     begin
                     clas:= "A";
                     end;

 //a �nica coisa restante a se fazer � mostrar ao usuario os resultados.

 writeln ("caro usuario o imposto pago por voce e de ", imp:4:2, " .");
 writeln ("a gratificacao e de ", grat, " .");
 writeln ("o salario liquido e de ", sal_liq:4:2, " .");
 writeln ("e sua classificacao e ", clas , " .");

 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.