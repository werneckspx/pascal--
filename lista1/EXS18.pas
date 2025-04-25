program exs17;

uses crt;

var x,y,z: real;

begin;

 //depois de se declarar as variaveis se da o resumo do programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa recebera tres medidas e te dira se essas medidas sao de um triangulo,");
 writeln ("equilatero, isosceles ou escaleno. ou se essas tres medidas nao formem um triangulo tambem.");
 writeln (" ");
 write ("para prosseguir precione enter.");
 readkey;

 //entao se le as 3 medidas do usuario para descobrir qual tipo de triangulo �.

 clrscr;
 writeln ("por favor digite a primeira medida .");
 readln (x);

 clrscr;
 writeln ("agora digite a segunda medida .");
 readln (y);

 clrscr;
 writeln ("agora digite a terceira medida .");
 readln (z);

 // entao se come�a a cadeia de ifs. Note que para a cadeia central ser executada uma condi��o tem que ser cumprida
 // pois se essa condi��o primaria nao for cumprida a figura em quest�o n�o � um triangulo.
 // porem quando ela ja foi cumprida basta colocar condi��es para cada tipo de triangulo baseado em seu formato.
 // dessa forma voc� mostra ao usuario se a figura em quest�o � algum dos tipos de tri�ngulo, ou n�o � um triangulo.

 clrscr;

 if (x < y+z) and (y < x+z) and (z < x+y) then
    begin

         if (x=y) and (x=z) then
            begin
            writeln ("este triangulo e equilatero.");
            end

            else if (x=y) or (x=z) or (y=z) then
                    begin
                    writeln ("este  triangulo e isosceles.");
                    end

                    else if (x<>y) and (x<>z) and (y<>z) then
                            begin
                            writeln ("este triangulo e escaleno.");
                            end
   end

                            else
                                begin
                                writeln ("estas medidas nao formam um triangulo.");
                                end;


 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.
