program exs15;

uses crt;

var invest: real;
    tipo: integer;

begin;

 //depois de se declarar as variaveis se da o resumo do programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa recebera o valor do seu investimento e de acordo onde voce investiu,");
 writeln ("sera calculado o novo coeficiente.");
 write ("para comecar precione enter.");
 readkey;

 // Ent�o se le o valor do investimento.

 clrscr;
 writeln ("por favor digite o valor do investimento.");
 readln (invest);

 // Se le a op��o que o usuario quer que definir� de quanto sera o investimento a ser calculado.

 clrscr;
 writeln ("Se o seu investimento for em poupanca tecle 1.");
 writeln ("Se o seu investimento for em fundos de renda fixa tecle 2.");
 readln (tipo);

 clrscr;

 //Ent�o se faz uma estrutura de case para caso o numero seja um tenha um aumento de 3% no investimento.
 //Se for 2 tera um aumento de 4%, e nisso ja se apresenta os resultados ao usuario.

 case tipo of

    1: begin
       writeln ("O novo valor do seu investimento e de ", (invest * 1.03):0:2 , " .");
       end;

    2: begin
       writeln ("O novo valor do seu investimento e de ", (invest * 1.04):0:2 , " .");
       end;

 end;

 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.
