program exs7;

uses crt;

var n1,n2,n3: real;
    I: integer;

begin;

 //aqui se da o resumo do programa pro usuario e o que ele faz

 clrscr;
 writeln ("caro usuario este programa recebera tres numeros a sua escolha");
 writeln ("e de acordo com sua vontade eles serao apresentados em ordem,");
 writeln ("crescente, decrescente ou de modo que o maior fica no meio dos dois.");
 writeln (" ");
 write ("para iniciar tecle enter.");
 readkey;

 // aqui � feita a intera��o com o usuario onde ele digitar� os numeros a serem lidos

 clrscr;
 writeln ("primeiro digite o primeiro numero ");
 readln (n1);

 clrscr;
 writeln ("agora digite o segundo numero ");
 readln (n2);

 clrscr;
 writeln ("agora digite o terceiro numero ");
 readln (n3);

 clrscr;
 writeln ("agora digite o que voce quer que seja feito");
 writeln (" ");
 writeln ("digite 1 para os numeros serem apresentados em ordem crescente");
 writeln ("digite 2 para os numeros serem apresentados em ordem decrescente");
 writeln ("digite 3 para que o numero maior seja apresentado no meio dos outros dois");
 readln (i);

 //agora come�a a primeira cadeia de ifs onde o usuario digita 1 para obter seus numeros em ordem crescente
 //cada cadeia � constituida com 1 condi��o prim�ria, que � o recebimento do que o usuario deseja fazer com os
 //seus numeros digitados.
 //entao quando o programa acha a cadeia que o usuario deseja, ele abre a primeira condi��o da cadeia que pede a condi��o de um numero ser maior que o outro
 //e dentro dela foi colocado outra condi��o para determinar a ordem exata dos numeros a serem apresentados.



 if i=1
   then  begin

       if (n1<n2) and (n1<n3)
         then

              if (n2<n3)
                 then begin
                      writeln ("a ordem crescente dos numeros e, ", n1:0:2, " ,", n2:0:2, " ,", n3:0:2, " .");
                      end

                 else begin
                      writeln ("a ordem crescente dos numeros e, ", n1:0:2, " ,", n3:0:2, " ,", n2:0:2, " .");
                      end;


       if (n2<n1) and (n2<n3)
         then

              if (n1<n3)
                 then begin
                      writeln ("a ordem crescente dos numeros e, ", n2:0:2, " ,", n1:0:2, " ,", n3:0:2, " .");
                      end

                 else begin
                      writeln ("a ordem crescente dos numeros e, ", n2:0:2, " ,", n3:0:2, " ,", n1:0:2, " .");
                      end;


       if (n3<n2) and (n3<n1)
         then

              if (n1<n2)
                 then begin
                      writeln ("a ordem crescente dos numeros e, ", n3:0:2, " ,", n1:0:2, " ,", n2:0:2, " .");
                      end

                 else begin
                      writeln ("a ordem crescente dos numeros e, ", n3:0:2, " ,", n2:0:2, " ,", n1:0:2, " .");
                      end;
         end;

  if i=2
   then  begin

    if (n1>n2) and (n1>n3)
       then

            if (n2>n3)
             then begin
                  writeln ("a ordem decrescente dos numeros e, ", n1:0:2, " ,", n2:0:2, " ,", n3:0:2, " .");
                  end

                  else begin
                      writeln ("a ordem decrescente dos numeros e, ", n1:0:2, " ,", n3:0:2, " ,", n2:0:2, " .");
                      end;


    if (n2>n1) and (n2>n3)
      then

          if (n1>n3)
            then begin
                 writeln ("a ordem decrescente dos numeros e, ", n2:0:2, " ,", n1:0:2, " ,", n3:0:2, " .");
                 end

                 else begin
                      writeln ("a ordem decrescente dos numeros e, ", n2:0:2, " ,", n3:0:2, " ,", n1:0:2, " .");
                      end;


    if (n3>n2) and (n3>n1)
      then

          if (n1>n2)
            then begin
                 writeln ("a ordem decrescente dos numeros e, ", n3:0:2, " ,", n1:0:2, " ,", n2:0:2, " .");
                 end

                 else begin
                      writeln ("a ordem decrescente dos numeros e, ", n3:0:2, " ,", n2:0:2, " ,", n1:0:2, " .");
                      end;
         end;

 //somente para a op��o 3 do usuario que as coisas mudam um pouco aqui voc� so precisa saber qual o numero maior entao
 //basta fazer 3 condi��es, na qual o programa achar a condi��o verdadeira, so resta dar o tratamento para o usuario.

 if i=3
   then  begin

         if (n1>n2) and (n1>n3)
           then begin
                writeln ("a ordem desejada dos numeros e, ", n2:0:2, " ,", n1:0:2, " ,", n3:0:2, " .");
                end;

         if (n2>n1) and (n2>n3)
           then begin
                writeln ("a ordem desejada dos numeros e, ", n1:0:2, " ,", n2:0:2, " ,", n3:0:2, " .");
                end;

         if (n3>n2) and (n3>n1)
           then begin
                writeln ("a ordem desejada dos numeros e, ", n1:0:2, " ,", n3:0:2, " ,", n2:0:2, " .");
                end;

         end;


  writeln (" ");
  write ("para encerrar o programa aperte qualquer tecla.");
  readkey;

end.
