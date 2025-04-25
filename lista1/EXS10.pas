program exs10;

uses crt;

var dia1,mes1,ano1,dia2,mes2,ano2: integer;

//se declara as variaveis todas do tipo inteiro porque n�o existe ano ou mes ou dia negativo, ou com virgula.

begin;

 //ent�o voc� resume o que o programa faz para o usuario.

 clrscr;
 writeln ("caro usuario este programa recebera duas datas que voce deseja e lhe mostrara a data cronologicamente maior.");
 write ("para comecar aperte enter");
 readkey;

 //se le as duas datas que o usuario colocar.

 clrscr;
 writeln ("primeiro digite o ano da primeira data.");
 readln (ano1);

 clrscr;
 writeln ("agora digite o mes da primeira data.");
 readln (mes1);

 clrscr;
 writeln ("agora digite o dia da primeira data.");
 readln (dia1);

 clrscr;
 writeln ("agora digite o ano da segunda data.");
 readln (ano2);

 clrscr;
 writeln ("agora digite o mes da segunda data.");
 readln (mes2);

 clrscr;
 writeln ("agora digite o dia da segunda data.");
 readln (dia2);

 //entao se inicia a cadeia de ifs onde voc�, ira come�ar pelos anos colocando como condi�ao um maior que o outro
 //ai caso a primeira condi��o de um ano ser maior que o outro n�o for atendida se parte para a segunda.
 //e se caso a segunda n�o for atendida que seria o caso de anos iguais se parte para os meses.
 //ai se cria uma cadeia para os meses igual a cadeia dos anos, e se caso eles forem iguais se cria uma pros dias tambem.
 //caso os dias forem iguais se manda uma mensagem pro usuario falando que as duas datas s�o iguais.

 if ano1 > ano2 then
                   begin
                   writeln ("A maior data e", ano1,"-",mes1,"-",dia1,".");
                   end

                   else
                       if ano1 < ano2 then begin
                                           writeln ("A maior data e", ano2,"-",mes2,"-",dia2,".");
                                           end

                                           else
                                               if mes1 > mes2 then begin
                                                                   writeln ("A maior data e", ano1,"-",mes1,"-",dia1,".");
                                                                   end

                                                                   else
                                                                       if mes2 > mes1 then begin
                                                                                           writeln ("A maior data e", ano2,"-",mes2,"-",dia2,".");
                                                                                           end

                                                                                           else
                                                                                               if  dia1 > dia2 then begin
                                                                                                                       writeln ("A maior data e", ano1,"-",mes1,"-",dia1,".");
                                                                                                                       end

                                                                                                                       else
                                                                                                                           if dia2  > dia1 then begin
                                                                                                                                                write ("A maior data e", ano2,"-",mes2,"-",dia2,".");
                                                                                                                                                end

                                                                                                                                                else begin
                                                                                                                                                     writeln ("As duas datas sao iguais.");
                                                                                                                                                     end;
 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");    readkey;

end.
