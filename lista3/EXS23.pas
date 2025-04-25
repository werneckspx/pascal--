program exs23;

uses crt;

var salario,quilo,valor,faturamento,total:real;
    tipo,qtd:integer;

begin

 clrscr;
 writeln ("Digite o valor do salario minimo.");
 readln (salario);

 valor:=salario/8;
 quilo:=1;


  while quilo<>0 do
     begin
     clrscr;
     writeln ("Para encerrar o recebimento de dados digite 0 para quillowats.");
     writeln;
     writeln ("Digite a quantidade gasta de quillowats.");
     readln (quilo);
     writeln ("Digite o tipo de consumidor.");
     writeln ("1 para residencial; 2 para comercial; 3 para industrial.");
     readln (tipo);

     case tipo of
     1:total:=(valor*quilo)*1.05;
     2:total:=(valor*quilo)*1.10;
     3:total:=(valor*quilo)*1.15;
     end;

     faturamento:=faturamento+total;

     if (total>=500) and (total<=1000) then
        qtd:=qtd+1;

     writeln ("O valor a ser pago � de, R$",total:0:2," .");

     end;

  writeln ("O valor de cada quillowat � de, R$",valor:0:2," .");
  writeln ("O faturamento da empresa � de, R$",faturamento:0:2," .");
  writeln ("A quantidade de consumidores que gastam entre 500R$ e 1000R$ � de, ",qtd," .");
  writeln;
  write ("Para encerrar o programa pressione qualquer tecla.");
  readkey;

end.