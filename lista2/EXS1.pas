program exs1;

uses crt;

var n1,n2,n3,n4,media:= real;

begin;

 //depois de se declarar as variaveis se apresenta o programa ao usuario.

 clrscr;
 writeln ("Caro usuario este programa recebera quatro notas suas e lhe mostrara sua media aritimetica.");
 write ("para prosseguir tecle enter.");
 readkey;

 //se le os 4 valores para calcular a media.

 clrscr;
 writeln("por favor digite a primeira nota.");
 readln (n1);

 clrscr;
 writeln ("por favor digite a segunda nota.");
 readln (n2);

 clrscr;
 writeln ("por favor digite a terceira nota.");
 readln (n3);

 clrscr;
 writeln ("por favor digite a quarta nota.");
 readln (n4);


 media:= (n1+n2+n3+n4)/3;

 //se calcula a media e manda o resultado ao usuario.

 clrscr;
 writeln ("Sua media aritimetica e ", media:0:2, " .");

 //e se finaliza com uma cadeia de ifs para exibir a mensagem de aprova��o ou reprova��o.

 if (media < 7) then
    begin
    writeln ("Caro usuario voce foi reprovado.");
    end

    else if (media >= 7) then
            begin
            writeln ("Caro usuario voce foi aprovado.");
            end;

 writeln ("  ");
 write ("para encerrar precione qualquer tecla.");
 readkey;

end.