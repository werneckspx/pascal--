program exs15;

uses crt;

var preco,maior,menor,total_imp,imposto,fim,adicional: real;
    i,qtd_barato,qtd_normal,qtd_caro,custo_est:integer;
    refri,cat: char;

    //aqui se declara as variaveis.


begin

 clrscr;

 maior:=0;
 menor:=30000;

 for i:=1 to 12 do
     begin
     //e aqui se le os dados do produto que o usuario digitar�.

     clrscr;
     writeln ("Digite o pre�o do produto.");
     readln (preco);
     writeln ("Digite S se o produto necessitar de refrigera��o.");
     writeln ("Digite N se o produto n�o necessitar de refrigera��o.");
     readln (refri);
     writeln ("Digite a categoria do produto.");
     writeln ("A para alimenta��o.");
     writeln ("L para limpeza.");
     writeln ("V para vestuario.");
     readln (cat);

     {Abaixo nas varias cadeias de ifs sera feita a defini��o de quanto sera o
     custo de estocagem.}

     if (preco <20) then
        begin

        if (cat="A") then
           begin
           custo_est:=2;
           end

           else if (cat="L") then
                   begin
                   custo_est:=3;
                   end

                   else if (cat="V") then
                           begin
                           custo_est:=4;
                           end


        end;

     if (preco >= 20) and (preco <=50) then
        begin
           if (refri="S") then
              begin
              custo_est:=6;
              end

              else if refri="N" then
                      begin
                      custo_est:=0;
                      end
        end;


     if (preco >50) then
        begin
           if (refri="S") then
              begin
              if (cat="A") then
                 begin
                 custo_est:=5;
                 end

                 else if (cat= "L") then
                         begin
                         custo_est:=2;
                         end

                         else if (cat="V") then
                                 begin
                                 custo_est:=4;
                                 end
              end

              else if  (refri="N") then
                       begin
                         if (cat="A") or (cat="V") then
                            begin
                            custo_est:=0;
                            end

                            else if (cat="L") then
                                    begin
                                    custo_est:=1;
                                    end
                       end


        end;

        //se define o imposto.

        if (cat="A") or (refri="S") then
           begin
           imposto:=preco*0.04;
           end

           else begin
                imposto:=preco*0.02;
                end;


       fim:=preco+imposto+custo_est;

       //aqui se apresenta os resultados do produto singular.

       writeln ("O custo de estocagem � de, R$",custo_est," .");
       writeln ("O imposto � de, R$",imposto:0:2," .");
       writeln ("O pre�o final � de, R$",fim:0:2," .");

       {Se define a classifica��o do produto e se faz a contagem para no
       final se apresentar quantos de cada classifica��o tem produtos.}

       if (fim<20) then
          begin
          writeln ("A classifica��o do produto � barato.");
          qtd_barato:=qtd_barato+1;
          end

          else if (fim>=20) and (fim<=100) then
                  begin
                  writeln ("A classifica��o do produto � medio.");
                  qtd_normal:=qtd_normal+1;
                  end

                  else if (fim>100) then
                          begin
                          writeln ("A classfica��o do produto � caro.");
                          qtd_caro:=qtd_caro+1;
                          end;

       {Se calcula o adicional total e o imposto total, e logo em seguida
       se define qual o maior pre�o e qual o menor pre�o.}

       adicional:=adicional+imposto+custo_est;
       total_imp:=total_imp+imposto;

       if (maior < preco) then
          begin
          maior:=preco;
          end;

       if (menor < preco) then
          begin
          menor:=preco;
          end;



     end;

  //se apresenta os resultados finais ao usuario.

  writeln ("O maior pre�o � de, R$",maior:0:2," .");
  writeln ("O menor pre�o � de, R$",menor:0:2," .");
  writeln ("A media dos valores adicionais � de, R$",adicional:0:2," .");
  writeln ("O total dos impostos � de, R$",total_imp:0:2," .");
  writeln ("A quantidade de produtos com classifica��o barato � de, ",qtd_barato," .");
  writeln ("A quantidade de produtos com classifica��o medio � de, ",qtd_normal," .");
  writeln ("A quantidade de produtos com classifica��o caro � de, ",qtd_caro," .");
  writeln;
  write ("Para encerrar o programa pressione qualquer tecla.");
  readkey;

end.