program exs10;

uses crt;

var mi: array [1..5] of real;
    altura,altura_total,quilos,percentagem:real;
    i,qtd,quilos80,idade: integer;

    {Se declara as variaveis.}

begin;

 clrscr;

  {Ent�o come�a a se ler as informa��es de cada jogador do primeiro time
  ja se tratando de fazer a contagem de quantos jogadores tem menos de 18
  anos e de quantos jogadores tem mais que 80 quilos. E a cada repeti��o do
  la�o se soma a idade, para definir a media da idade do time posteriormente
  e o mesmo se faz com a altura.
  E isso foi feito em 5 la�os de repeti��o da mesma maneira.}

  writeln ("Digite as informa��es dos jogadores do primeiro time.");

  for i:=1 to 11 do
     begin
       clrscr;
       writeln ("Digite a idade do jogador N�:",i, " .");
       readln (idade);
       mi[1]:=mi[1]+idade;

       writeln ("Digite a altura do jogador N�:",i, " .");
       readln (altura);
       altura_total:=altura_total+altura;

       writeln ("Digite peso do jogador N�:",i, " .");
       readln (quilos);

       if (idade<18) then
          begin
          qtd:=qtd+1;
          end;

       if (quilos > 80) then
          begin
          quilos80:=quilos80+1;
          end;

     end;

 clrscr;

  writeln ("Digite as informa��es dos jogadores do segundo time.");

  for i:=1 to 11 do
     begin
       clrscr;
       writeln ("Digite a idade do jogador N�:",i, " .");
       readln (idade);
       mi[2]:=mi[2]+idade;

       writeln ("Digite a altura do jogador N�:",i, " .");
       readln (altura);
       altura_total:=altura_total+altura;

       writeln ("Digite peso do jogador N�:",i, " .");
       readln (quilos);

       if (idade<18) then
          begin
          qtd:=qtd+1;
          end;

       if (quilos > 80) then
          begin
          quilos80:=quilos80+1;
          end;

     end;

 clrscr;

  writeln ("Digite as informa��es dos jogadores do terceiro time.");

  for i:=1 to 11 do
     begin
       clrscr;
       writeln ("Digite a idade do jogador N�:",i, " .");
       readln (idade);
       mi[3]:=mi[3]+idade;

       writeln ("Digite a altura do jogador N�:",i, " .");
       readln (altura);
       altura_total:=altura_total+altura;

       writeln ("Digite peso do jogador N�:",i, " .");
       readln (quilos);

       if (idade<18) then
          begin
          qtd:=qtd+1;
          end;

       if (quilos > 80) then
          begin
          quilos80:=quilos80+1;
          end;

     end;

 clrscr;

  writeln ("Digite as informa��es dos jogadores do quarto time.");

  for i:=1 to 11 do
     begin
       clrscr;
       writeln ("Digite a idade do jogador N�:",i, " .");
       readln (idade);
       mi[4]:=mi[4]+idade;

       writeln ("Digite a altura do jogador N�:",i, " .");
       readln (altura);
       altura_total:=altura_total+altura;

       writeln ("Digite peso do jogador N�:",i, " .");
       readln (quilos);

       if (idade<18) then
          begin
          qtd:=qtd+1;
          end;

       if (quilos > 80) then
          begin
          quilos80:=quilos80+1;
          end;

     end;

 clrscr;

  writeln ("Digite as informa��es dos jogadores do quinto time.");

  for i:=1 to 11 do
     begin
       clrscr;
       writeln ("Digite a idade do jogador N�:",i, " .");
       readln (idade);
       mi[5]:=mi[5]+idade;

       writeln ("Digite a altura do jogador N�:",i, " .");
       readln (altura);
       altura_total:=altura_total+altura;

       writeln ("Digite peso do jogador N�:",i, " .");
       readln (quilos);

       if (idade<18) then
          begin
          qtd:=qtd+1;
          end;

       if (quilos > 80) then
          begin
          quilos80:=quilos80+1;
          end;

     end;

 {Ent�o so resta apresentar ao usuario os resultados.}

 writeln ("A quantidade de jogadores com idade inferior a 18 anos �, ",qtd," .");
 writeln ("A media da altura de todos os jogadores do campeonato �, ",altura_total/55:0:2 ," .");
 writeln ("A percentagem de jogadores com mais de 80kg �, ",quilos80/55*quilos80:0:2,"% .");
 writeln;

   for i:=1 to 5 do
       begin
       mi[i]:=mi[i]/11;
       writeln ("A media da idade dos jogadores do time ",i," �, ",mi[i]/11:0:2, " .");
       end;

 writeln;
 write ("para encerrar o programa pressione qualquer tecla.");
 readkey;

end.