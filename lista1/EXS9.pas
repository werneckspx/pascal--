program exs9;

uses crt,dos;

var ano, mes, dia, dia_semana: word;
    hora, minuto, segundo, cen_seg : word;

begin;

 //primeiro se apresenta ao usuario o que o programa ira fazer.

 clrscr;
 writeln ("caro usuario este programa lhe mostrara a data e hora atuais.");
 write ("para comecar tecle enter.");
 readkey;

 //para se adiquirir a hora e data atuais e nescessario usar dois comandos que estao em outra biblioteca
 //se usa a biblioteca "dos" e para adquirir os valores se usa o comando getdate para adiquirir a data.
 //e o comando get time para adquirir o horario, entao a unica coisa restante e ler esses valores,
 //com uma variavel do tipo word e depois seguir as instrucoes abaixo.

 getdate (ano, mes, dia, dia_semana);
 gettime (hora, minuto, segundo, cen_seg);

 clrscr;

 //ja que o m�s deve ser escrito em forma extensa entao para cada numero de 1 a 12 se escreve em uma condi��o
 //e a unica coisa restante � mostrar para o usuario os resultados.

 case mes of

      1:   writeln ("a data de hoje e ", dia, " de janeiro de ", ano, " .");
      2:   writeln ("a data de hoje e ", dia, " de fevereiro de ", ano, " .");
      3:   writeln ("a data de hoje e ", dia, " de marco de ", ano, " .");
      4:   writeln ("a data de hoje e ", dia, " de abril de ", ano, " .");
      5:   writeln ("a data de hoje e ", dia, " de maio de ", ano, " .");
      6:   writeln ("a data de hoje e ", dia, " de junho de ", ano, " .");
      7:   writeln ("a data de hoje e ", dia, " de julho de ", ano, " .");
      8:   writeln ("a data de hoje e ", dia, " de agosto de ", ano, " .");
      9:   writeln ("a data de hoje e ", dia, " de setembro de ", ano, " .");
      10:  writeln ("a data de hoje e ", dia, " de outubro de ", ano, " .");
      11:  writeln ("a data de hoje e ", dia, " de novembro de ", ano, " .");
      12:  writeln ("a data de hoje e ", dia, " de dezembro de ", ano, " .");

 end;

 //depois de terminar a estrutura de case se salta uma linha para certificar que o usuario n�o fique confuso
 //e se mostra as horas para ele junto com a data composta.

 writeln (" ");
 writeln ("e a hora e ", hora ,":",minuto);
 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");  readkey;

end.
