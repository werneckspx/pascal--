program exs21;

uses crt;

var codigo: integer;

begin;

 //depois de se declarar as variaveis se apresenta o programa ao usuario.

 clrscr;
 writeln ("este programa recebera o codigo de origem de um produto e lhe dira ");
 writeln ("de onde este produto veio.");
 write ("para prosseguir tecle enter.");
 readkey;

 //se le o codigo do produto para apresentar de onde o produto veio.

 clrscr;
 writeln ("por favor digite o codigo do produto.");
 readln (codigo);

 clrscr;

 {se cria uma estrutura de case para definir de onde veio o produto, e ja se
   apresenta ao usuario este resultado.}

 case codigo of

    1: begin
       writeln ("Veio da regiao sul.");
       end;

    2: begin
       writeln ("Veio da regiao norte.");
       end;

    3: begin
       writeln ("Veio da regiao leste.");
       end;

    4: begin
       writeln ("Veio da regiao oeste.");
       end;

    5..6: begin
          writeln ("Veio da regiao nordeste.");
          end;

    7..9: begin
          writeln ("Veio da regiao sudeste.");
          end;

    10..20: begin
            writeln ("Veio da regiao centro-oeste.");
            end;

    21..30: begin
            writeln ("Veio da regiao nordeste.");
            end;

 else  begin
       writeln ("Codigo invalido.");
       end;

 end;

 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.