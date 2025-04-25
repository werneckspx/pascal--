program exs16;

uses crt;

var base, altura: real;

begin

 clrscr;
 repeat
 clrscr;
 begin
 writeln ("Digite a base do triangulo.");
 readln (base);
 end;
 until (base>0);


 repeat
 clrscr;
 begin
 writeln ("Digite a altura do triangulo.");
 readln(altura);
 end;
 until (altura>0);

 clrscr;
 writeln ("A area do triangulo � de, ",(base*altura/2):0:2," cm .");
 writeln;
 write ("Para encerrar o programa pressione qualquer tecla.");
 readkey;

end.
