program exs19;

uses crt;

var altura : real;
    sexo : char;

begin;

 //depois de se declarar as variaveis se apresenta o programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa recebera sua altura e sexo para lhe dizer seu peso   ideal.");
 write ("para prosseguir tecle enter.");
 readkey;

 //ent�o se recebe a altura do usuario para definir seu peso ideal.

 clrscr;
 writeln ("por favor digite sua altura como 1.60 .");
 readln (altura);

 //ent�o se recebe o sexo do usuario para se criar a estrutura case.

 clrscr;
 writeln ("Digite seu sexo.");
 writeln ("M para homem.");
 writeln ("F para mulher.");
 writeln ("lembre-se de colocar letra maiuscula.");
 readln (sexo);

 clrscr;

 //no case se faz os calculos e se apresenta ao usuario o seu peso ideal.

 case sexo of

    "M": begin
         writeln ("Seu peso ideal e ", ((72.7*altura)-58):0:2 , " kg .");
         end;

    "F": begin
         writeln ("Seu peso ideal e ", ((62.1*altura)-44.7):0:2 , " kg .");
         end;

 end;

 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.