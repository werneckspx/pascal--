program exs5;

uses crt;

var n1,n2: real;
    opcao: integer;

begin;

 //se declara as variaveis e se da o resumo do programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa recebera dois numeros e te dara op��es sobre o");
 writeln ("o que voce deseja fazer com eles.");
 write ("para comecar tecle enter.");
 readkey;

 clrscr;
 writeln ("por favor digite o primeiro numero.");
 readln (n1);

 clrscr;
 writeln ("agora digite o segundo numero.");
 readln (n2);

 //se recolhe os numeros que serao utilizados para se fazer os calculos

 clrscr;
 writeln ("para media entre os numero digitados digite 1.");
 writeln ("para diferenca do maior pelo menor digite 2");
 writeln ("para o produto entre os numeros digitados digite 3");
 writeln ("para divisao do primero pelo segundo, sendo o segundo diferente de 0 tecle 4.");
 readln (opcao);

   {se faz um pequeno menu para ler a op��o que o usuario deseja e se faz uma
   condi��o de case em cima dela para o programa executar de acordo com a
   vontade do usuario.}

 clrscr;

 case opcao of

     //na primeira se soma os dois numeros e os divide por 2.

     1: begin
        writeln ("a media entre os numeros e ", ((n1+n2)/2):0:2 , " .");
        end;

          {na segunda se subtrai o numero maior pelo menor se descobre isso com
          uma pequena cadeia de ifs}

     2: begin
        if (n1 > n2) then
           begin
           writeln ("a diferenca entre os numeros e de ", (n1-n2):0:2 , " .");
           end

           else if (n2 > n1) then
                   begin
                   writeln ("a diferenca entre os numero e de ", (n2-n1):0:2 , " .");
                   end

                   else  begin
                         writeln (" os numeros sao iguais.");
                         end;
        end;

     //na terceira se multiplica um numero pelo outro.

     3: begin
        writeln ("o produto dos numeros digitados e ", (n1*n2):0:2 , " .");
        end;

     //na quarta se divide um numero pelo outro.

     4: begin
        writeln ("a divisao dos numeros e ", (n1/n2):0:2 , " .");
        end;


 end;

 if (opcao > 1) and (opcao < 4) then
    begin
    writeln ("opcao invalida!");
    end;


 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.