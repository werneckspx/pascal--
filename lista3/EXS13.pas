program exs13;

uses crt;

var qtd,i,tempo,cont_m,cont_f,cont_24,periodo:integer;
    percentagem_m,percentagem_f,percentagem_24:real;
    sexo:char;

begin

 {Depois de se declarar as variaveis se l� o valor do periodo, e da quantidade
 de crian�as nascidas durante este periodo.}

 clrscr;
 writeln ("Digite o intervalo do periodo em meses.");
 readln (periodo);
 writeln ("Digite a quantidade de crian�as nascidas no periodo.");
 readln(qtd);

 clrscr;

  {Se cria um la�o para definir a percentagem de quantas crian�as de ambos
  os sexos morreram antes do periodo e a percentagem de quantas crian�as
  morreram antes de completar 24 meses.}

  for i:=1 to qtd do
      begin
         clrscr;
         writeln ("Digite o sexo da crian�a N�, ",i," :M para masculino F para feminino.");
         readln (sexo);
         writeln ("Digite o tempo de vida da crian�a em meses.");
         readln (tempo);

         if (sexo="F") and (tempo <=periodo) then
            begin
            cont_f:=cont_f+1;
            end

            else if (sexo="M") and (tempo<=periodo) then
                    begin
                    cont_m:=cont_m+1;
                    end;

         if (tempo <24) then
            begin
            cont_24:=cont_24+1;
            end;

      end;

      //aqui se faz os calculos.

 percentagem_m:=cont_m/qtd*100;
 percentagem_f:=cont_f/qtd*100;
 percentagem_24:=cont_24/qtd*100;

 //e apresenta os resultados ao usuario.

 writeln ("A percentagem de crian�as do sexo masculino mortas no periodo �, ", percentagem_m:0:2,"% .");
 writeln ("A percentagem de crian�as do sexo feminino mortas no periodo �, ", percentagem_f:0:2,"% .");
 writeln ("A percentagem de crian�as que morreram com menos de 24 meses �, ", percentagem_24:0:2,"% .");
 writeln;
 write ("Para encerrar o programa pressione qualquer tecla.");
 readkey;

end.
