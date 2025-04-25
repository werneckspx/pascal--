program exs23;

uses crt;

var codigo,qtd, valor : integer;
    nota, fim, preco, desc: real;

begin;

 //depois de se declarar as variaveis se apresenta o programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa recebera o codigo do produto comprado,");
 writeln ("a quantidade comprada do produto, e lhe mostrara o preco do produto,");
 writeln ("o preco total da nota, o valor de desconto e o preco com desconto.");
 write ("para comecar tecle enter.");
 readkey;

 {Ent�o se pede ao usuario o codigo do produto, se cria uma condi��o de if para caso ele digite uma op��o invalida,
   nesta condi��o se diz ao usuario que o codigo � invalido. E se da o comando de exit para o programa ir para
   a linha final de execu��o.}

 clrscr;
 writeln ("por favor digite o codigo do produto.");
 readln (codigo);

 if (codigo < 1) or (codigo > 40 ) then
       begin
       clrscr;
       writeln ("opcao invalida!");
       write ("para encerrar o programa precione qualquer tecla.");
       readkey;
       exit;
       end;

 //caso ele digite uma op��o valida se l� a quantidade que sera comprada do produto.

 clrscr;
 writeln ("agora digite a quantidade comprada do produto.");
 readln (qtd);

 //ent�o se come�a uma estrutura de case para definir o valor do produto comprado.

 case codigo of

    1..10: begin
           valor:=10;
           end;

    11..20: begin
            valor:=15;
            end;

    21..30: begin
            valor:=20;
            end;

    31..40: begin
            valor:=30;
            end;

 end;

 //depois de definir o valor do produto se calcula o valor da nota.

 nota:= valor*qtd;

 //e com o valor da nota se faz uma cadeia de ifs para definir o desconto que ser� dado ao usuario.

 if (nota > 500) then
    begin
    desc:= nota*0.15;
    end

    else if (nota <= 500) and (nota > 250) then
            begin
            desc:= nota*0.10;
            end

            else if (nota <= 250) then
                    begin
                    desc:= nota*0.05;
                    end;

 //ent�o so resta apresentar ao usuario os resultados.

 writeln ("o valor do produto e de ", valor , " .");
 writeln ("o preco total da nota e de ", nota:0:2 , " .");
 writeln ("o valor do desconto e de ", desc:0:2 , " .");
 writeln ("o preco final e ", (nota - desc):0:2 , " .");
 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.