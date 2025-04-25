program exs9;

uses crt;

var saldo, percentual : real;

begin;

 //depois de se declarar as variaveis se da o resumo do programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa recebera seu saldo medio e calculara o valor do credito oferecido.");
 write ("para comecar tecle enter.");
 readkey;

 //entao se le o saldo que utilizaremos para calcular de quanto sera o percentual de credito dado ao usuario.

 clrscr;
 writeln ("por favor digite o seu saldo medio.");
 readln (saldo);

 clrscr;

 //se monta uma cadeia de ifs para definir de quanto sera o valor do percentual.

 if (saldo > 400) then
    begin
    percentual:= saldo*0.30;
    end

    else if (saldo <= 400) and (saldo > 300) then
            begin
            percentual:= saldo*0.25;
            end

            else if (saldo <= 300) and (saldo > 200) then
                    begin
                    percentual := saldo*0.20;
                    end

                    else if (saldo <= 200) then
                            begin
                            percentual:= saldo*0.10;
                            end;

 //se apresenta os resultados ao usuario.

 writeln ("seu saldo medio e ", saldo:0:2 , " .");
 writeln ("o percentual e de ", percentual:0:2 , " .");
 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.