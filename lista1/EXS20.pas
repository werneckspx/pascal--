program exs20;

uses crt;

var cod_p, cod_o : integer;
    peso,novo_peso : real;

begin;

 //depois de se declarar as variaveis se da o resumo do programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa lhe mostrara o preco de um produto baseado em seu codigo de pais de origem e");
 writeln ("o codigo do produto em si.");
 write ("para prosseguir tecle enter.");
 readkey;

 //o usuario digitar� 2 valores num�ricos inteiros, que ser�o os codigos usados nas estruturas case.
 //e ele digitar� tambem o peso do produto.

 clrscr;
 writeln ("primeiramente digite o codigo do produto comprado numero inteiro entre 1 e 10.");
 readln (cod_p);

 clrscr;
 writeln ("agora digite o codigo do pais de origem numero inteiro entre 1 e 3.");
 readln (cod_o);

 clrscr;
 writeln ("agora digite o peso do produto em quilos exemplo 1.200 ");
 readln (peso);


 clrscr;

 novo_peso:= peso*1000;

 {aqui se come�a as estruturas de cases um contendo o outro.
 o primeiro case tem como condi��o o codigo do produto sendo de 1..4, o segundo de 5..7, e o terceiro de 8..10.
 dentro dessas 3 condi��es se coloca outras 3 que � o codigo de cada pais, onde o imposto � diferente.
 e dentro da estrutura de cada pais ja se mostra ao usuario os valores do peso em gramas, o pre�o total do produto, o valor do imposto, e o pre�o do produto com imposto.
 e dessa mesma maneira se faz para as outras estruturas de case.}

 case cod_p of

 1..4 :  case cod_o of
              1:  begin
                  writeln ("o peso em grama e ", novo_peso:4:2 , " .");
                  writeln ("o preco total do produto e ", (novo_peso*10):4:2 , " .");
                  writeln ("o valor do imposto sobre o produto e 0.");
                  writeln ("o preco do produto com imposto e ,",  (novo_peso*10):4:2 ," .");
                  end;

              2:  begin
                  writeln ("o peso em grama e ", novo_peso:4:2 , " .");
                  writeln ("o preco total do produto e ", (novo_peso*10):4:2 , " .");
                  writeln ("o valor do imposto sobre o produto e ,",  ((novo_peso*10)*0.15):4:2 ,  " .");
                  writeln ("o preco do produto com imposto e ,",  ((novo_peso*10)*1.15):4:2 ," .");
                  end;

              3:  begin
                  writeln ("o peso em grama e ", novo_peso:4:2, " .");
                  writeln ("o preco total do produto e ", (novo_peso*10):4:2 , " .");
                  writeln ("o valor do imposto sobre o produto e .",  ((novo_peso*10)*0.25):4:2 ,  " .");
                  writeln ("o preco do produto com imposto e ,",  ((novo_peso*10)*1.25):4:2 ," .");
                  end;
          end;


 5..7 :  case cod_o of
              1:  begin
                  writeln ("o peso em grama e ", novo_peso:4:2 , " .");
                  writeln ("o preco total do produto e ", (novo_peso*25):4:2 , " .");
                  writeln ("o valor do imposto sobre o produto e 0.");
                  writeln ("o preco do produto com imposto e ,",  (novo_peso*25):4:2 ," .");
                  end;

              2:  begin
                  writeln ("o peso em grama e ", novo_peso:4:2 , " .");
                  writeln ("o preco total do produto e ", (novo_peso*25):4:2 , " .");
                  writeln ("o valor do imposto sobre o produto e ,",  ((novo_peso*25)*0.15):4:2 ,  " .");
                  writeln ("o preco do produto com imposto e ,",  ((novo_peso*25)*1.15):4:2 ," .");
                  end;

              3:  begin
                  writeln ("o peso em grama e ", novo_peso:4:2, " .");
                  writeln ("o preco total do produto e ", (novo_peso*25):4:2 , " .");
                  writeln ("o valor do imposto sobre o produto e .",  ((novo_peso*25)*0.25):4:2 ,  " .");
                  writeln ("o preco do produto com imposto e ,",  ((novo_peso*25)*1.25):4:2 ," .");
                  end;
         end;


 8..10:  case cod_o of
              1:  begin
                  writeln ("o peso em grama e ", novo_peso:4:2 , " .");
                  writeln ("o preco total do produto e ", (novo_peso*35):4:2 , " .");
                  writeln ("o valor do imposto sobre o produto e 0.");
                  writeln ("o preco do produto com imposto e ,",  (novo_peso*35):4:2 ," .");
                  end;

              2:  begin
                  writeln ("o peso em grama e ", novo_peso:4:2 , " .");
                  writeln ("o preco total do produto e ", (novo_peso*35):4:2 , " .");
                  writeln ("o valor do imposto sobre o produto e ,",  ((novo_peso*35)*0.15):4:2 ,  " .");
                  writeln ("o preco do produto com imposto e ,",  ((novo_peso*35)*1.15):4:2 ," .");
                  end;

              3:  begin
                  writeln ("o peso em grama e ", novo_peso:4:2, " .");
                  writeln ("o preco total do produto e ", (novo_peso*35):4:2 , " .");
                  writeln ("o valor do imposto sobre o produto e .",  ((novo_peso*35)*0.25):4:2 ,  " .");
                  writeln ("o preco do produto com imposto e ,",  ((novo_peso*35)*1.25):4:2 ," .");
                  end;

        end;
 end;

 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");   readkey;

end.
