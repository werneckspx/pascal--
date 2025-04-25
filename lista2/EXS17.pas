program exs17;

uses crt;

const senha= 4531;

var tentativa : integer;

begin;

 //depois de se declarar as variaveis se apresenta o programa ao usuario.

 clrscr;
 writeln ("caro usuario este programa recebera sua tentativa de adentrar ao sistema,");
 writeln ("e te dira se sua senha e valida ou nao.");
 write ("para comecar tecle enter.");
 readkey;

 //se l� a senha que o usuario digitou para a checagem de validade.

 clrscr;
 writeln ("por favor digite a senha.");
 readln (tentativa);

 clrscr;

 //Ent�o se faz uma cadeia de ifs para checar a validade de senha.

 if (tentativa = senha) then
    begin
    writeln ("Voce tem permicao de acesso.");
    end

    else begin
         writeln ("Voce nao tem permicao de acesso.");
         end;

 //se apresenta os resultados ao usuario.

 writeln (" ");
 write ("para encerrar o programa precione qualquer tecla.");
 readkey;

end.