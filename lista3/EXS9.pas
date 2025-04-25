program exs9;

uses crt;

var vet: array [1..12] of real;
    aprovados,exame,reprovados,i:integer;
    geral:real;

begin;

 clrscr;
  {Depois de se declarar as variaveis se l� os valores das notas dos alunos.}

  for i:=1 to 6 do
     begin
     writeln ("Digite a primeira nota do aluno N�: ",i," .");
     readln (vet[i]);
     end;


  for i:=7 to 12 do
      begin
      writeln ("Digite a segunda nota do aluno N�: ",i-6," .");
      readln (vet[i]);
      end;

  {Ent�o se define a media de cada um deles.}

  vet[1]:=(vet[1]+vet[7])/2;
  vet[2]:=(vet[2]+vet[8])/2;
  vet[3]:=(vet[3]+vet[9])/2;
  vet[4]:=(vet[4]+vet[10])/2;
  vet[5]:=(vet[5]+vet[11])/2;
  vet[6]:=(vet[6]+vet[12])/2;

  {Se faz a contagem de quantos foram reprovados, estao de exame , e quantos
  foram aprovados. E nesse la�o ja se aproveita para fazer a soma de todas as
  notas}

  for i:=1 to 6 do
      begin
      if vet[i]<3 then
         reprovados:=reprovados+1

         else if (vet[i]>=3) and (vet[i]<=7) then
                 exame:=exame+1

                 else if (vet[i]>7)then
                         aprovados:=aprovados+1;



      geral:=geral+vet[i];
      end;

 //com todas as notas se calcula a media de todos os alunos.

 geral:=geral/6;

 {Ent�o se apresenta ao usuario os resultados.}

 for i:=1 to 6 do
      begin
      writeln ("A media do aluno N�: ",i," �,", vet[i]:0:2," .");
      end;

 writeln ("A quantidade de alunos reprovados � de, ",reprovados," .");
 writeln ("A quantidade de alunos aprovados � de, ",aprovados," .");
 writeln ("A quantidade de alunos de exame � de, ",exame," .");
 writeln ("A media da classe � de, ",geral:0:2, " .");
 writeln ("");
 write ("Para encerrar o programa precione qualquer tecla.");
 readkey;

end.
