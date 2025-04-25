program exs6;

uses crt;

var n1,n2 :real;
    op: integer;

begin;

 //depois de se declarar as variaveis se apresenta ao usuario o programa.

 clrscr;
 writeln ("caro usuario este programa recebera dois numero e te dara opcoes para voce decidir o que fazer com eles.");
 write ("para continuar tecle enter.");
 readkey;

 //se coleta os numeros que ser�o utilizados nos calculos e a op��o do calculo que o usuario deseja.

 clrscr;
 writeln ("por favor digite o primeiro numero.");
 readln (n1);

 clrscr;
 writeln ("agora digite o segundo numero.");
 readln (n2);

 clrscr;
 writeln ("para que o primeiro numero seja elevado ao segundo digite 1.");
 writeln ("para que seja mostrada a raiz quadrada de cada um dos numeros digite 2.");
 writeln ("para que seja mostrada a raiz cubica de cada um dos numeros digite 3.");
 readln (op);

 clrscr;

 //ent�o se come�a uma cadeia de ifs para definir o que ser� feito e ja se apresenta o resultado ao usuario.

 case op of

   1: begin
      writeln ("o resultado de um numero elevado ao outro e ", exp(n2*ln(n1)):0:2, " .");
      end;

   2: begin
      writeln ("a raiz quadrada do primeiro numero e ", sqrt (n1):0:2 , " .");
      writeln ("a raiz quadrada do segundo numero e ", sqrt (n2):0:2, " .");
      end;

   3: begin
      writeln ("a raiz cubica do primeiro numero e ", exp (1/3*ln (n1)):0:2 , " .");
      writeln ("a raiz cubica do segundo numero e ", exp (1/3*ln (n2)):0:2 , " .");
      end;

 end;

    { para o caso do usuario digitar uma op��o invalida para a cadeia de ifs se cria uma condi��o para dizer que
      a op��o � invalida.}

 if (op < 1) or (op > 3) then
    begin
    writeln ("opcao invalida!");
    end;

 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.