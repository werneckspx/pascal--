program exs24;

uses crt;

var codigo: integer;
    cat, refri : char;
    preco, imp, aumento, novo : real;
    clas : string;

begin;

 //depois de se declarar as variaveis se da o resumo do programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa recebera o codigo e preco de um produto e se ele nescessita de refrigeracao e lhe mostrara:");
 writeln ("o valor do aumento, o valor do imposto, o novo preco e a classificacao do produto.");
 write ("para comecar tecle enter.");
 readkey;

 //ent�o se le o pre�o, o codigo, e se o produto nescesssita de refrigera��o

 clrscr;
 writeln ("primeiramente digite o preco do produto.");
 readln (preco);

 clrscr;
 writeln ("agora digite o codigo do produto.");
 writeln ("1 para produtos de limpeza.");
 writeln ("2 para produtos de alimentacao.");
 writeln ("3 para produtos de vestimenta.");
 readln (codigo);

   //caso o usuario digite algum codigo invalido se manda esta mensagem a ele e se encerra o programa com o comando exit.

   if (codigo < 1) or (codigo > 3) then
      begin
      writeln ("Codigo invalido.");
      writeln ("para encerrar o programa precione qualquer tecla.");
      readkey;
      exit;
      end;

 clrscr;
 writeln ("Digite S caso o produto nescessite de refrigeracao.");
 writeln ("Digite N caso o produto nao nescessite de refrigeracao.");
 writeln ("Lembre-se de usar letras maiusculas.");
 readln (refri);

   //Caso ele digite uma express�o invalida se manda a mesma mensagem a ele e se encerra o programa.

   if (refri <> "S") and (refri <> "N") then
      begin
      writeln ("Exprecao invalida.");
      writeln ("para encerrar o programa precione qualquer tecla.");
      readkey;
      exit;
      end;

   {para definir o aumento do produto se faz uma cadeia de ifs, e dentro dela se cria uma estrutura case para
   englobar o tipo dos produtos}

 clrscr;

 if (preco > 25) then
    begin
       case codigo of

          1:  begin
              aumento:= preco*0.12;
              end;

          2:  begin
              aumento:= preco*0.15;
              end;

          3:  begin
              aumento:= preco*0.18;
              end;

       end;
    end

    else if (preco <= 25) then
            begin
               case codigo of

                     1:  begin
                         aumento:= preco*0.12;
                         end;

                     2:  begin
                         aumento:= preco*0.15;
                         end;

                     3:  begin
                         aumento:= preco*0.18;
                         end;

                end;
            end;


 {Para definir o imposto se coloca a condi��o pedida, e nela se coloca o imposto.
  Caso essa condi��o n�o for atendida se calcula o imposto com outro valor.}

 if (codigo = 2) or (refri = "S") then
    begin
    imp:= preco*0.05;
    end

    else begin
         imp:= preco*0.08;
         end;

 //se calcula o novo pre�o e a partir dele ja se define a classifica��o do produto com uma cadeia de ifs.

 novo:= preco+imp+aumento;

 if (novo >= 120) then
    begin
    clas:= "Caro";
    end

    else if (novo < 120) and ( novo > 50) then
            begin
            clas:= "Normal";
            end

            else if (novo <= 50) then
                    begin
                    clas:= "Barato";
                    end;

 //Ent�o a unica coisa restante � mostrar ao usuario os resultados.

 writeln ("O valor do aumento e de ", aumento:0:2 , " .");
 writeln ("O valor do imposto e de ", imp:0:2 , " .");
 writeln ("O novo preco e de ", novo:0:2 , " .");
 writeln ("A classificacao e ", clas , " .");
 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.