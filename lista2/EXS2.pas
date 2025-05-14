program EXS2;

var n1,n2,media :real;

begin;

 //depois de se declarar as variaveis se da o resumo do programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa recebera duas notas suas calculara a media aritimetica delas,");
 writeln ("entao lhe mostrara se voce foi aprovado ou reprovado.");
 write ("para comecar tecle enter.");
 readkey;

 //entao se le as variaveis para fazer a media de nota.

 clrscr;
 writeln ("por favor digite a primeira nota.");
 readln (n1);

 clrscr;
 writeln ("agora digite a segunda nota.");
 readln (n2);

 clrscr;

 media:= (n1+ n2)/2;

   {ent�o antes de se come�ar a cadeia de ifs para apresentar a mensagem ao usuario
   se mostra a media aritimetica dele}

 writeln ("Sua media aritimetica e ", media:0:2, " .");

 //ent�o se faz uma pequena cadeia de ifs para definir a mensagem apresentada ao usuario.

 if (media >= 7) and (media <= 10) then
    begin
    writeln ("Voce foi aprovado!!!");
    end;

    else if(media < 7) and (media >= 4) then
            begin
            writeln ("Voce tera que fazer o exame.");
            end;

            else if (media < 4) and (media >= 0) then
                    begin
                    writeln ("Voce foi reprovado.");
                    end;

 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.