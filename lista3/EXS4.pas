program exs4;

uses crt;

var cod,cod_menor,cod_maior  ,i,  m1,maior,menor, aci, cont: integer;
    media_vei, media_aci: real;

begin;

 {Depois de se declarar as variaveis se atribui valores as variaveis que serao
 utilizados posteriormente.}

 clrscr;

 maior:=0;
 menor:=10000;
 media_vei:=0;
 media_aci:=0;

 {Se cria um la�o de repeti��o para receber os valores e ir se definindo os
 valores finais que ser�o apresentados ao usuario.}

 for i:=1 to 5 do
     begin
     clrscr;
     writeln ("Digite o codigo da cidade.");
     readln (cod);
     writeln ("Digite o numero de veiculos de passeio.");
     readln (m1);
     writeln ("Digite o numero de acidentes de transito.");
     readln (aci);

     media_vei:=media_vei+m1;

     if ( aci>maior) then
        begin
        maior:=aci;
        cod_maior:= cod;
        end;

     if ( aci < menor) then
        begin
        menor:=aci;
        cod_menor:= cod;
        end;

     if (m1 < 2000) then
        begin
        media_aci:= media_aci+aci;
        cont:=cont+1;
        end;

     end;

  {Se calcula as duas medias e se apresenta os resultados ao usuario.}

  media_vei:= media_vei/5;
  media_aci:= media_aci/cont;

  clrscr;
  writeln ("A cidade que mais tem acidentes e, ",cod_maior ," com ,",maior," acidentes.");
  writeln ("A cidade que mais tem acidentes e, ",cod_menor ," com ,",menor," acidentes.");
  writeln ("A media da quantidade de veiculos das 5 cidades e de, ",media_vei:0:2 ," veiculos.");
  writeln ("A media de acidentes das cidade que possuem menos que 2000 veiculos de passeio,");
  writeln ("� de, ", media_aci:0:2 ," acidentes.");
  writeln ("");
  write ("Para encerrar o programa pressione qualquer tecla.");
  readkey;

end.

