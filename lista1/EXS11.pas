program exs11;

uses crt;

var hora_i,hora_f,min_i,min_f,hora_d,min_d: integer;

//se declara as variaveis que serao utilizadas.

begin;

 //se apresenta o programa para o usuario

 clrscr;
 writeln ("caro usuario este programa lhe mostrara a duracao de um jogo baseado na hora de inicio e fim.");
 write ("para comecar tecle enter");
 readkey;

 //ent�o se come�a a adquirir os valores das variaveis.

 clrscr;
 writeln ("primeiramente digite a hora que o jogo comecou, numeros de 00-23.");
 readln (hora_i);

 clrscr;
 writeln ("agora digite os minutos do primeiro horario.");
 readln (min_i);

 clrscr;
 writeln ("agora digite a hora que o jogo terminou, numeros de 00-23.");
 readln (hora_f);

 clrscr;
 writeln ("agora digite os minutos do segundo horario.");
 readln (min_f);

 //agora se abre a cadeia de ifs. Para casos mais simples como a hora final e minuto final maior que os iniciais.
 //simplesmente � nescessario diminuir da hora final a hora inicial e o mesmo com os minutos.

 clrscr;

 if (hora_f > hora_i) and (min_f > min_i) then
    begin
    writeln ("o jogo durou ",hora_f - hora_i, " horas e ", min_f - min_i, "minutos .");
    end

    //agora quando os minutos finais tem um valor menor que os minutos iniciais j� � nescessario diminuir uma hora do total de horas
    //e subtrair os minutos finais com 60 que � o valor da hora diminuida com o valor dos minutos iniciais.

    else
        if (hora_f > hora_i) and (min_f < min_i) then
           begin
           writeln ("o jogo durou ",(hora_f - hora_i)-1 ," horas ", (min_f+60)-min_i, " minutos ."); readkey;
           end

           //agora para o caso da hora inicial ser maior que a final o tratamento � diferente.
           //porem para o caso dos minutos iniciais forem maior que os finais o tratamento � o mesmo
           //no caso da hora inicial ser maior que a final, se soma a hora final com 24 e depois se substrai pela hora inical


           else begin

               if min_i > min_f then
                  begin
                  min_f  := min_f+60;
                  hora_f := hora_f-1;
                  end;

               if hora_i > hora_f then
               begin
               hora_f := hora_f + 24;
               min_d  := min_f - min_i;
               hora_d := hora_f - hora_i;
               end;

               //entao a unica coisa restante � mostrar para o usuario o valor de dura��o do jogo.

               writeln ("o jogo durou ",hora_d," horas ",min_d, " minutos.");
                end;

 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla");    readkey;

end.
