program exs22;

uses crt;

var sexo,experiencia:char;
    idade,feminino,masculino,qtd_mulher21,menor_mulher,qtd_experiencia:integer;
    media_homem,percentagem_homem:real;

begin

 clrscr;

 idade:=1;
 menor_mulher:=30000;

 while (idade<>0) do
   begin
     clrscr;
     writeln ("Para encerrar o recebimento de dados digite 0 para idade.");
     writeln;
     writeln ("Digite a sua idade.");
     readln(idade);

       if (idade=0) then
          break;

     writeln("Digite o seu sexo:F para feminino,M para masculino.");
     readln(sexo);
     writeln ("Se voc� tem esperiencia no servi�o digite S caso contrario digite N.");
     readln(experiencia);

     if (sexo="F") then
        begin
        feminino:=feminino+1;

          if (idade < 21) and (experiencia="S") then
             qtd_mulher21:=qtd_mulher21+1;

          if (idade < menor_mulher) then
             menor_mulher:=idade;
        end

        else if (sexo="M") then
                begin
                masculino:=masculino+1;

                if (experiencia="S") then
                   media_homem:=media_homem+idade;
                   qtd_experiencia:=qtd_experiencia+1;

                if (idade>45) then
                   percentagem_homem:=percentagem_homem+1;


                end;


   end;

   if masculino=0 then
      masculino:=1;

 percentagem_homem:=percentagem_homem/masculino*100;


   if qtd_experiencia=0 then
      qtd_experiencia:=1;

 media_homem:=media_homem/qtd_experiencia;



 clrscr;
 writeln ("A quantidade de canditadas �: ",feminino," .");
 writeln ("A quantidade de candidatos �: ",masculino," .");
 writeln ("A quantidade de candidatas com menos de 21 anos e experiencia �: ",qtd_mulher21," .");
 writeln ("A candidata mais nova tem ",menor_mulher," anos de idade.");
 writeln ("A media da idade dos homens que tem esperiencia no servi�o, ",media_homem:0:2," .");
 writeln ("A percentagem de homens com mais de 45 anos, ",percentagem_homem:0:2,"% .");
 writeln;
 write ("Para encerrar o programa pressione qualquer tecla.");
 readkey;

end.
