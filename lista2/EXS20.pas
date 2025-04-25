program exs20;

uses crt;

var idade: integer;

begin;

 //depois de se declarar as variaveis se apresenta o programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa recebera sua idade e lhe mostrara sua categoria.");
 write ("para comecar tecle enter.");
 readkey;

 clrscr;
 writeln ("por favor digite sua idade.");
 readln (idade);

 //se le a idade para dar a classifica��o ao usuario.

 clrscr;

   {antes de se come�ar a cadeia de ifs se coloca uma condi��o para que se o
   usuario tiver menos de 5 anos ele nao pode ser um nadador.}

 if (idade < 5) then
    begin
    writeln ("Voce nao tem idade para ser um nadador.");
    write ("para encerrar o programa precione qualquer tecla.");
    readkey;
    exit;
    end;

 //ent�o se come�a a estrutura de case para classificar o usuario, e ja se apresenta o resultado.

 case idade of

    5..7: begin
          writeln ("Voce e um nadador infantil.");
          end;

    8..10: begin
           writeln ("Voce e um nadador juvenil.");
           end;

    11..15: begin
            writeln ("Voce e um nadador adolescente.");
            end;
    16..30: begin
            writeln ("Voce e um nadador adulto.");
            end;

    else    begin
            writeln ("Voce e um nadador senior.");
            end;

 end;

  writeln (" ");
  write ("para encerrar o programa precione qualquer tecla.");
  readkey;

end.