program exs7;

uses crt;

var n1: real;

begin;

 //depois de se declarar as variaveis se apresenta o resumo do programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa calculara seu aumento e caso voce nao for o receber te mostrara uma mensagem.");
 write ("para come�ar precione enter.");
 readkey;

 //se coleta a variavel do salario para se fazer a condicional.

 clrscr;
 writeln ("por favor informe o seu salario.");
 readln (n1);

   {ent�o se faz uma condi��o para que se o salario for maior que 500 entao se recebe 30% de aumento caso contrario
   se mostra a mensagem ao usuario que ele nao tem direito a aumento}

 if (n1 < 500) then
    begin
    writeln ("seu novo salario e de ", (n1*1.30):0:2 , " .");
    end

    else if (n1 >= 500 ) then
            begin
            writeln ("caro usuario voce tem direito a aumento.");
            end;

 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.