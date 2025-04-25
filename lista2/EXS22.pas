program exs22;

uses crt;

var idade , clas : integer;
    peso: real;

begin;

 //depois de se declarar as variaveis se apresenta o programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa recebera sua idade e peso e te dara sua classificacao.");
 write ("para prosseguir tecle enter.");
 readkey;

 clrscr;
 writeln ("por favor digite a sua idade.");
 readln (idade);

 clrscr;
 writeln ("agora digite o seu peso.");
 readln (peso);


   {se l� a idade do usuario e seu peso para definir sua classifica��o.
    Se cria uma estrutura de case englobando as idades e dentro da estrutura
    de case se faz cadeias de ifs com condi��es para o peso do usuario para,
    definir sua classifica��o final.}


 if (idade < 0) then
    begin
    writeln ("idade invalida.");
    writeln ("para encerrar o programa precione qualquer tecla.");
    readkey;
    exit;
    end;

 case idade of

   0..19: begin
            if (peso <= 60) then
               begin
               clas:=9;
               end

               else if (peso > 60) and (peso <= 90) then
                       begin
                       clas:=8;
                       end

                       else if (peso > 90) then
                               begin
                               clas:= 7;
                               end;
          end;


  20..50: begin
            if (peso <= 60) then
               begin
               clas:=6;
               end

               else if (peso > 60) and (peso <= 90) then
                       begin
                       clas:=5;
                       end

                       else if (peso > 90) then
                               begin
                               clas:= 4;
                               end;

          end;

    else  begin
              if (peso <= 60) then
                 begin
                 clas:=3;
                 end

                 else if (peso > 60) and (peso <= 90) then
                         begin
                         clas:=2;
                         end

                         else if (peso > 90) then
                                 begin
                                 clas:= 1;
                                 end;
          end;

 end;

 //ent�o se apresenta ao usuario sua classifica��o.

 writeln ("sua classificacao e ", clas , " .");
 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.
