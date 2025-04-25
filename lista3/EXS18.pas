program exs18;

uses crt;

var num:real;
    cont:integer;

begin

 clrscr;

 num:=1;
 while num>0 do
       begin
       writeln("Digite o novo numero.");
       cont:=cont+1;
       writeln("Para encerrar o programa digite 0 ou um valor negativo.");
       cont:=cont+1;
       readln(num);

       if (num<=0) then
          break;

       writeln ("O valor, ",num:0:2," .");
       cont:=cont+1;
       writeln ("Tem a raiz quadrada de,",sqrt(num):0:2," .");
       cont:=cont+1;
       writeln ("Seu valor ao quadrado � de, ",sqr(num):0:2," .");
       cont:=cont+1;
       writeln ("Seu valor ao cubo � de, ",exp(3*ln(num)):0:2," .");
       cont:=cont+1;

       if (cont>=20) then
          begin
          clrscr;
          cont:=0;
          writeln ("O valor, ",num:0:2," .");
          cont:=cont+1;
          writeln ("Tem a raiz quadrada de,",sqrt(num):0:2," .");
          cont:=cont+1;
          writeln ("Seu valor ao quadrado � de, ",sqr(num):0:2," .");
          cont:=cont+1;
          writeln ("Seu valor ao cubo � de, ",exp(3*ln(num)):0:2," .");
          cont:=cont+1;

          end;

       end;

end.
