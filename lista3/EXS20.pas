program exs20;

uses crt;

const valor=30;

var sexo:char;
    cont_h,cont_f:integer;
    num,cod:longint;
    bruto,liq,desconto,media_h,media_f:real;

begin

 clrscr;
 cod:=1;

    repeat

       begin
       clrscr;
       writeln("Para encerrar o recebimento de dados digite codigo=99999.");
       writeln;
       writeln ("Digite o seu codigo.");
       readln (cod);
       writeln ("Digite seu sexo:M para masculino,F para feminino.");
       readln (sexo);
       writeln ("Digite o numero de horas aulas trabalhadas.");
       readln (num);

       bruto:=valor*num;

       if (sexo="M") then
       begin
       liq:=bruto*0.90;
       media_h:=media_h+liq;
       cont_h:=cont_h+1;
       end

       else
            if (sexo="F") then
            begin
            liq:=bruto*0.95;
            media_f:=media_f+liq;
            cont_f:=cont_f+1;
            end;


       writeln;
       writeln("Seu codigo �, ",cod," .");
       writeln("Seu sal�rio bruto �, R$",bruto:0:2," .");
       writeln("Seu sal�rio liquido �, R$",liq:0:2," .");
       readkey;
       end;

    until (cod=99999);

  if (cont_h=0) then
     cont_h:=1;

  media_h:=media_h/cont_h;

  if (cont_f=0) then
     cont_f:=1;

  media_f:=media_f/cont_f;

  clrscr;
  writeln ("A media do sal�rio liquido dos homens �, R$",media_h:0:2," .");
  writeln ("A media do sal�rio liquido das mulheres �, R$",media_f:0:2," .");
  writeln;
  write ("Para encerrar o programa pressione qualquer tecla.");
  readkey;

end.                                                                      2
