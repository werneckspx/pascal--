program exs24;

uses crt;

var menu:integer;
    salario,imposto,novo:real;


begin

 clrscr;

 menu:=0;
 repeat
   begin
       repeat
           begin
           clrscr;
           writeln ("Digite 1 para ver seu imposto.");
           writeln ("Digite 2 para ver seu novo sal�rio.");
           writeln ("Digite 3 para ver sua classifica��o.");
           writeln ("Digite 4 para finalizar.");
           readln (menu);

            case menu of
              1:begin
                clrscr;
                writeln ("Digite seu salario.");
                readln (salario);
                writeln;

                    if (salario <500) then
                       begin
                       imposto:=salario*0.05;
                       writeln ("O imposto a ser pago � de, R$",imposto:0:2," .");
                       readkey;
                       end

                   else if (salario >=500) and (salario<=850) then
                           begin
                           imposto:=salario*0.10;
                           writeln ("O imposto a ser pago � de, R$",imposto:0:2," .");
                           readkey;
                           end

                  else if (salario>850) then
                          begin
                          imposto:=salario*0.15;
                          writeln ("O imposto a ser pago � de, R$",imposto:0:2," .");
                          readkey;
                          end;
                end;

              2:begin
                clrscr;
                writeln ("Digite seu salario.");
                readln (salario);
                writeln;

                 if (salario>1500) then
                    begin
                    novo:=salario+25;
                    writeln ("Seu novo salario � de, R$",novo:0:2," .");
                    readkey;
                    end

                 else if (salario<=1500) and (salario >=750) then
                         begin
                         novo:=salario+50;
                         writeln ("Seu novo salario � de, R$",novo:0:2," .");
                         readkey;
                         end

                 else if (salario <750) and (salario >=450) then
                         begin
                         novo:=salario+75;
                         writeln ("Seu novo salario � de, R$",novo:0:2," .");
                         readkey;
                         end

                else begin
                     novo:=salario+100;
                     writeln ("Seu novo salario � de, R$",novo:0:2," .");
                     readkey;
                     end;

                end;

              3:begin
                clrscr;
                writeln ("Digite seu salario.");
                readln (salario);
                writeln;

                  if (salario <=700) then
                     begin
                     writeln ("Sua classifica��o �: mal remunerado.");
                     readkey;
                     end

                  else begin
                       writeln ("Sua classifica��o �: bem remunerado.");
                       readkey;
                       end;

                end;
            end;
           end;
       until (menu>=1) or (menu<=4)
   end;

 until (menu=4);

end.