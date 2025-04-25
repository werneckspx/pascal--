program exs8;

uses crt;

var n1,n2,n3,n4: real;

begin;

 //primeiramente se da o resumo do que o programa far� para o usuario.
 //e depois j� se manda ele digitar as variaveis que ser�o utilizadas.

 clrscr;
 writeln ("caro usuario este programa recebera dois numeros e te dara opcoes sobre o que   fazer com eles.");
 write ("para continuar precione enter.");
 readkey;

 clrscr;
 writeln ("por favor digite o primeiro numero");
 readln (n1);

 clrscr;
 writeln ("por favor digite o segundo numero");
 readln (n2);

 //se da as op��es para o usuario escolher o que deseja ser feito a principio.

 clrscr;
 writeln ("tecle 1 para somar os dois numeros.");
 writeln ("tecle 2 para calcular a raiz quadrada de um numero.");
 readln (n3);

 //agora come�a uma pequena cadeia de ifs para determinar o que fazer caso o usuario digite 2.
 //se l� o valor que ele quer e apresenta-se o resultado a ele.

 clrscr;
 if n3=2 then begin
              writeln ("precione 1 para a raiz quadrada do primeiro numero.");
              writeln ("precione 2 para a raiz quadrada do segundo numero.");   readln (n4);
              end;

 //aqui � a outra parte da cadeia de if caso ele digite 1 para a variavel n4 se calcula a raiz quadrada de n1.
 //poderia ser utilizado somente um else, porem se fosse feito desse jeito qualquer valor que o usuario digitasse cairia no else.
 //por isso se abre outra condi��o para caso do usuario digitar um valor que n�o seja 2 o programa se encerra e assim ele tem que recome�ar.

 if n4=1 then begin
              writeln ("a raiz quadrada do primeiro numero e ", sqrt(n1):4:2, " .");
              end

              else if n4=2 then begin
                                writeln ("a raiz quadrada do segundo numero e ", sqrt(n2):4:2, " .");
                                end;



 //aqui est� a condi��o para o n3 ser 1.
 //so basta apresentar pro usuario a soma dos dois numeros.

 if  n3=1 then begin
               writeln ("o resultados da soma dos numeros e ",(n1+n2):4:2," .");
               end;


 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla");
 readkey;

end.




