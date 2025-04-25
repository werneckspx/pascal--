program exs6;

uses crt;

var cod: array [1..10] of integer;
    turno: array [1..10] of char;
    categoria: array [1..10] of char;
    horas: array [1..10] of integer;
    valor: array [1..10] of real;
    total: array [1..10] of real;
    inicial: array[1..10] of real;
    alimentacao: array [1..10] of real;
    i:integer;

    {Se declara um vetor para cada op��o que sera lida e para cada valor que
    se apresentar� ao usuario.}

begin;



 clrscr;
 for i:=1 to 10 do
     begin

       {Se coloca na estrutura de for para ler os 4 dados dos 10 funcionarios
       tratando para caso do usuario digitar op��es invalidas nas op��es de
       turno e de categoria.}

       begin
       clrscr;
       writeln ("Digite o codigo do funcionario numero: ", i ," .");
       readln (cod[i]);
       end;
       writeln("");

       turno[i]:="j";
       while (turno[i] <> "M") and (turno[i] <> "V") and (turno[i] <> "N") do
       begin
       writeln ("Digite o turno do funcionario numero: ",i," .");
       writeln ("M para matutino, V para vespertino, e N para noturno.");
       readln (turno[i]);
       end;
       writeln("");

       categoria[i]:="p";
       while (categoria[i] <> "O") and (categoria[i] <> "G") do
       begin
       writeln ("Digite a categoria do funcionario numero: ",i," .");
       writeln ("O para operario e G para gerente.");
       readln (categoria[i]);
       end;
       writeln("");

       begin
       writeln ("Digite a quantidade de horas trabalhadas do funcionario numero: ",i," .");
       readln (horas[i]);
       end;

       {Se come�a uma estrutura de case para definir o valor da hora trabalhada.}

        case categoria[i] of

           "G":begin
                  case turno[i] of
                    "M": valor[i]:=450*0.18;
                    "V","N": valor[i]:=450*0.15;
                  end;

               end;

          "O":begin
                 case turno[i] of
                    "M": valor[i]:=450*0.13;
                    "V","N": valor[i]:=450*0.10;
                  end;
              end;

        end;

     //se calcula o salario inicial.

     inicial[i]:=valor[i]*horas[i];

     //se cria uma cadeia de ifs para definir o valor do auxilio alimenta��o.

     if (total[i] < 300) then
        alimentacao[i]:=total[i]*0.20

        else if (total[i] >= 300) and (total[i] <= 600) then
                alimentacao[i]:= total[i]*0.15

                else if (total[i] > 600) then
                        alimentacao[i]:= total[i]*0.5;

    //ent�o se calcula o valor total.

   total[i]:= inicial[i]+alimentacao[i];


   end;

 clrscr;

 {Para finalizar se cria uma estrutura de for para apresentar os resultados
 ao usuario.}

 for i:=1 to 10 do
     begin
     writeln ("Funcionario, ", cod[i], " .");
     writeln ("Trabalhou, ",horas[i], " .");
     writeln ("Hora trabalhada vale, R$",valor[i]:0:2, " .");
     writeln ("Salario inicial, R$",inicial[i]:0:2, " .");
     writeln ("Auxilio alimenta��o, R$",alimentacao[i]:0:2, " .");
     writeln ("Salario final, R$",total[i]:0:2, " .");
     writeln ("");
     delay(500)
     end;

 writeln ("");
 write ("para encerrar o programa pressione qualquer tecla.");
 readkey;

end.