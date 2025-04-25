program exs25;

uses crt;

var preco,imposto,seguro,fim,total_imposto:real;
    cod,valor_transporte:integer;
    transporte,perigo:char;

begin

 clrscr;

 preco:=1;

 while preco>0 do
    begin
    clrscr;
    writeln ("Para encerrar o recebimento de dados digite um valor menor ou igual a 0.");
    writeln;
    writeln ("Digite o pre�o do produto.");
    readln (preco);

    if (preco <=0) then
       break;

    writeln ("Digite o codigo do produto.");
    writeln ("1 para origem dos Estados Unidos.");
    writeln ("2 para origem do M�xico.");
    writeln ("3 para origem de outro lugar.");
    readln (cod);
    writeln ("Digite T para o meio de transporte terrestre.");
    writeln ("Digite F para o meio de transporte fluvial.");
    writeln ("Digite A para o meio de transporte a�reo.");
    readln (transporte);
    writeln ("Digite S se a carga for perigosa.");
    writeln ("Digite N se a carga n�o for perigosa.");
    readln (perigo);

    if preco<=100 then
    imposto:=preco*0.05

    else imposto:=preco*0.10;

    case perigo of

    "S":begin

          case cod of

            1:valor_transporte:=50;
            2:valor_transporte:=21;
            3:valor_transporte:=24;

          end;

        end;

    "N":begin

          case cod of

            1:valor_transporte:=12;
            2:valor_transporte:=21;
            3:valor_transporte:=60;

          end;

        end;

    end;

      if (cod=2) or (transporte="A") then
         seguro:=preco/2

         else seguro:=0;

    fim:=preco+imposto+valor_transporte+seguro;
    total_imposto:=total_imposto+imposto;

    clrscr;
    writeln ("O valor do imposto �, R$",imposto:0:2," .");
    writeln ("O valor do transporte �, R$",valor_transporte," .");
    writeln ("O valor do seguro �, R$",seguro:0:2," .");
    writeln ("O pre�o final �, R$",fim:0:2," .");
    readkey;

  end;

  writeln;
  writeln ("O pre�o total dos impostos �, R$",total_imposto:0:2," .");
  writeln;
  write ("para encerrar o programa pressione qualquer tecla.");
  readkey;

end.