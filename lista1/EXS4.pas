program exs4;

uses crt;

var n1,n2,n3: real;

begin;

 clrscr;
 writeln ("caro usuario este programa recebera tres numeros e os apresentara em ordem crescente");
 write ("para iniciarmos tecle enter.");
 readkey;

 clrscr;
 writeln ("por favor digite o primeiro numero ");
 readln (n1);

 clrscr;
 writeln ("agora digite o segundo numero diferente do primeiro ");
 readln (n2);

 clrscr;
 writeln ("agora digite o terceiro numero diferente do primeiro e do segundo ");
 readln (n3);

 //primeiro se le os 3 numeros que o usuario deseja.
 //ent�o o que deve ser feito � calcular todas as combina��es possiveis entre n1,n2,n3 serem diferentes e,
 //escreve-las, e depois disso s� e preciso mostrar os resultados.

 if (n1>n2) and (n1>n3) and (n2>n3)
   then  begin writeln("a ordem crescente desses numeros e ",n1:4:2,", ",n2:4:2,", ",n3:4:2 ,".");
         end

        else if (n1>n2) and (n1>n3) and (n3>n2)
               then  begin
                     writeln ("a ordem crescente desses numeros e ", n1:4:2,", ",n3:4:2 ,", ", n2:4:2, ".");
                     end

                     else if (n2>n1) and (n2>n3) and (n1>n3)
                            then  begin
                                  writeln ("a ordem crescente desses numeros e ", n2:4:2,", ",n1:4:2 ,", ", n3:4:2, ".");
                                  end

                                  else if (n2>n1) and (n2>n3) and (n3>n1)
                                         then  begin
                                               writeln ("a ordem crescente desses numeros e ", n2:4:2,", ",n3:4:2 ,", ", n1:4:2, ".");
                                               end

                                               else if (n3>n1) and (n3>n2) and (n1>n2)
                                                      then  begin
                                                            writeln ("a ordem crescente desses numeros e ", n3:4:2,", ",n1:4:2 ,", ", n2:4:2, ".");
                                                            end

                                                            else if (n3>n1) and (n3>n2) and (n2>n1)
                                                                   then  begin
                                                                         writeln ("a ordem crescente desses numeros e ", n3:4:2,", ",n2:4:2 ,", ", n1:4:2, ".");
                                                                         end;


 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla");
 readkey;

end.
