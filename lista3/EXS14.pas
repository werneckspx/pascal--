program exs14;

uses crt;

var divida,valor,juros,lol:real;
    qtd,i:integer;

begin

 {Depois de se declarar as variaveis se l� o valor da divida.}

 clrscr;
 writeln ("Digite o valor da divida.");
 readln (lol);

 {Atribui-se}

 valor:=lol;
 qtd:=1;
 juros:=0;
 writeln ("Valor da divida:RS",lol:0:2," .");
 writeln ("Valor dos juros:R$",juros:0:2," .");
 writeln ("Quantidade de parcelas: ",qtd," .");
 writeln ("Valor da parcela:R$,",valor:0:2," ,");

 divida:=lol*1.10;
 valor:=divida/3;
 qtd:=qtd+2;
 juros:=lol*0.10;

 for i:=1 to 4 do
     begin
     writeln;
     writeln ("Valor da divida:RS",divida:0:2," .");
     writeln ("Valor dos juros:R$",juros:0:2," .");
     writeln ("Quantidade de parcelas: ",qtd," .");
     writeln ("Valor da parcela:R$,",valor:0:2," ,");

     divida:=lol*(1.10+(i*0.05));
     juros:=lol*(0.10+(i*0.05));
     qtd:=qtd+(3*1);
     valor:=(divida)/qtd;


     end;

 writeln;
 write ("Para encerrar o programa pressione qualquer valor.");
 readkey;

end.