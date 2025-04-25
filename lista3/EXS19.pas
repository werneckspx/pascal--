program exs19;

uses crt;

var n_total,m_total,n,m:integer;

begin

 clrscr;
 m:=1;
 n:=2;
 while (m <= n) do
       begin
       clrscr;
       writeln ("Para encerrar e verificar a soma total digite um valor de m maior ou igual a n.");
       writeln("Digite o valor de M,inteiro e positivo.");
       readln(m);
       writeln("Digite o valor de N, inteiro e positivo.");
       readln(n);
       n_total:=n_total+n;
       m_total:=m_total+m;
       end;

 clrscr;
 writeln ("O total da soma de M, ",m_total," .");
 writeln ("O total da soma de N, ",n_total," .");
 writeln;
 write("Para encerrar o programa precione qualquer tecla.");
 readkey;

end.
