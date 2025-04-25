program exs21;

uses crt;

var num,soma,media,maior,menor,media_par , percentagem_impar:real;
    qtd,qtd_par:longint;
    cont_par:integer;

begin

 clrscr;
 writeln ("Para encerrar o recebimento de numeros digite o n�mero 30000.");
 writeln ("Digite um numero.");
 readln(num);
 soma:=soma+num;
 qtd:=1;
 media:=num;
 maior:=num;
 menor:=num;
 cont_par:=1;
 percentagem_impar:=1;

 if ((trunc(num) mod 2)=0)then
 media_par:=media_par+num;

 if ((trunc(num) mod 2)=1)then
 percentagem_impar:=percentagem_impar+1;


 while num<>30000 do
       begin
       clrscr;
       writeln ("Para encerrar o recebimento de numeros digite o n�mero 30000.");
       writeln ("Digite outro numero.");
       readln(num);

       soma:=soma+num;
       qtd:=qtd+1;
       media:=media+num;

       if (num > maior) then
          maior:=num;

       if (num < menor) then
       menor:=num;

       if ((trunc(num) mod 2)=0)then
       begin
       media_par:=media_par+num;
       cont_par:=cont_par+1;
       end;

       if ((trunc(num) mod 2)=1)then
       begin
       percentagem_impar:=percentagem_impar+1;
       end;

       end;


 media:=media/qtd;
 media_par:=media_par/cont_par;
 percentagem_impar:=qtd/percentagem_impar*100;

 writeln ("Soma dos numeros: ",soma:0:2," .");
 writeln ("Quantidade de numeros digitados: ",qtd," .");
 writeln ("Media dos numeros digitados: ",media:0:2," .");
 writeln ("Maior numero digitado: ",maior:0:2," .");
 writeln ("Menor numero digitado: ",menor:0:2," .");
 writeln ("Media dos numeros pares: ",media_par:0:2," .");
 writeln ("Percentagem dos numeros impares: ",percentagem_impar:0:2,"% .");
 writeln;
 write ("Para encerrar o programa pressione qualquer tecla.");
 readkey;


end.



