program exs12;

uses crt;

var num: integer;
    peca,i,cont_f,cont_m,fodao,total_peca:integer;
    folha,media_homem,media_mulher,sal,lol:real;
    sexo:char;

begin

 {Depois de se declarar as variaveis se l� o valor do salario minimo.}

 clrscr;
 writeln ("Digite o valor do salario minimo.");
 readln (sal);

 fodao:=0;

 {Ent�o se coloca tudo em um la�o para definir o valor total da folha de
 pagamento,a media de pe�as dos homens e das mulheres, o total de pe�as
 fabricadas no mes, e o codigo do operario com maior salario.}

 for i:=1 to 15 do
    begin
    clrscr;
    writeln ("Digite o numero do operario n� ",i," .");
    readln (num);
    writeln ("Digite quantas pe�as ele fabricou no mes.");
    readln (peca);
    writeln ("Digite o sexo do funcionario M para masculino F para feminino.");
    readln (sexo);

    if (peca<=20) then
       begin
       lol:=sal;
       end

       else if (peca>20) and (peca<=31) then
               begin
               lol:=sal+((sal*0.03)*(peca-20));
               end

               else if (peca>31) then
                       begin
                       lol:=sal+((sal*0.05)*(peca-31));
                       end;

    writeln ("O salario do operario N� ",num," � R$",lol:0:2," .");
    readkey;

    folha:=folha+lol;
    total_peca:=total_peca+peca;

    if (sexo="M") then
        begin
        cont_m:=cont_m+1;
        media_homem:=media_homem+peca;
        end

        else if (sexo="F") then
                begin
                cont_f:=cont_f+1;
                media_mulher:=media_mulher+peca;
                end;


    if (num>fodao) then
       fodao:=num;

 end;

 media_homem:=media_homem/cont_m;
 media_mulher:=media_mulher/cont_f;

 clrscr;

 {So resta apresentar ao usuario os resultados.}

 writeln;
 writeln ("O total da folha de pagamento � de,R$", folha:0:2," .");
 writeln ("O numero total de pe�as fabricada no m�s � de, ",total_peca," .");
 writeln ("A media de pe�as fabricada pelos homens � de, ",media_homem:0:2," .");
 writeln ("A media de pe�as fabricada pelas mulheres � de, ",media_mulher:0:2," .");
 writeln ("O numero do operario com maior sal�rio �, ",fodao," .");
 writeln;
 write ("Para encerrar o programa pressione qualquer tecla.");
 readkey;

end.
