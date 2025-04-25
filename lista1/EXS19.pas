program exs19 ;

uses crt;

var n1,n2: real;

begin;

 //depois de se declarar as variaveis se da o resumo do programa ao usuario

 clrscr;
 writeln ("caro usuario este programa lhe mostrara sua classificacao de acordo com seu peso e altura.");
 write ("para continuar tecle enter.");
 readkey;

 //ent�o se le a altura e peso do usuario para mostra-lhe a sua classifica��o

 clrscr;
 writeln ("por favor digite sua altura.");
 readln (n1);

 clrscr;
 writeln ("agora digite seu peso.");
 readln (n2);

 //ent�o se faz 3 cadeias de ifs 1 para cada condi��o de altura e dentro das cadeias de alturas se coloca as condi��es
 //de pesos para achar a classifica��o do usuario

 if (n1 < 1.20) then
    begin
         if (n2 > 90) then
            begin
            writeln ("sua classificacao e "G" .");
            end

            else  if (n2 <= 90) and (n2 >= 60) then
                     begin
                     writeln ("sua classificacao e "D" .");
                     end

                     else if (n2 < 60) then
                             begin
                             writeln ("sua classificacao e "A" .");
                             end
    end;

  if (n1 > 1.20) and (n1 < 1.70) then
     begin
          if (n2 > 90) then
             begin
             writeln ("sua classificacao e "H" .");
             end

             else  if (n2 <= 90) and (n2 >= 60) then
                      begin
                      writeln ("sua classificacao e "E" .");
                      end

                      else if (n2 < 60) then
                              begin
                              writeln ("sua classificacao e "B" .");
                              end
     end;

   if (n1 > 1.70) then
     begin
          if (n2 > 90) then
             begin
             writeln ("sua classificacao e "J" .");
             end

             else  if (n2 <= 90) and (n2 >= 60) then
                      begin
                      writeln ("sua classificacao e "F" .");
                      end

                      else if (n2 < 60) then
                              begin
                              writeln ("sua classificacao e "C" .");
                              end

    end;

  //depois so resta mostrar ao usuario sua classifica��o.

 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.
