program TesteCompleto;
var
  i, idade, octInt, hexInt: integer;
  nota, media: real;
  nome, hexStr, octStr: string;
  flag: boolean;
begin
  writeln("Digite seu nome:");
  readln(nome);

  writeln("Digite sua idade:");
  readln(idade);

  writeln("Digite sua nota (real):");
  readln(nota);


  writeln("Olá, ", nome);
  writeln("Idade: ", idade);
  writeln("Nota: ", nota:0:2);


  flag := true;

  if flag then
    writeln("Flag está ativada.");

  writeln("Contador de 1 a 5:");
  for i := 1 to 5 do
    write("i = ", i);
end.
