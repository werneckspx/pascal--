program mega_teste;
var
  a, b, c: integer;
  x, y: real;
  s, t: string;
  flag: boolean;
  i, j: integer;
begin
  // Teste de atribuição simples
  a := 1;
  b := 2;
  c := a + b * 3 - 4 div 2 mod 2;
  x := 2.5;
  y := x * 2.0 + 1.5 / 3.0;
  s := "abc";
  t := s + "def";
  flag := true;

  // Teste de operadores relacionais e lógicos
  if (a = b) or (x <> y) and not flag then
    writeln("relacional e logico ok");

  // Teste de bloco begin/end e comandos vazios
  begin
    ;
    a := a + 1;
    ;
    b := b - 1;
  end;

  // Teste if-else encadeado
  if a > 0 then
    writeln("a > 0");
  else if a = 0 then
    writeln("a = 0");
  else
    writeln("a < 0");

  // Teste while com break e continue
  i := 0;
  while i < 5 do
  begin
    if i = 2 then
      continue;
    if i = 4 then
      break;
    writeln(i);
    i := i + 1;
  end;

  // Teste for simples
  for j := 1 to 3 do
    writeln(j);

  // Teste for aninhado
  for i := 0 to 1 do
    for j := 0 to 1 do
      writeln(i);

  // Teste read e readln
  read(a);
  readln(b);

  // Teste write e writeln com expressões
  write(a);
  writeln("fim do teste");

  // Teste operadores unários
  a := -b + c;

  // Teste string vazia e boolean
  s := "";
  flag := false;

  // Teste comandos vazios
  ;
  ;

  a:= 1;
  b := 2;
  y := 3.99;
  x := 16.21314;

  a := b + y;
  writeln(a);
  y := x+b;
  writeln(y);
  y := x + a;
  writeln(y);
  if(a < y+b) then
    x := y;
  writeln(x);

  a := $A;      // 10 em decimal
  b := $1F;     // 31 em decimal
  c := $FF;     // 255 em decimal
  writeln(a);   // Deve imprimir 10
  writeln(b);   // Deve imprimir 31
  writeln(c);   // Deve imprimir 255

  a := 10;
  b := $A;
  c := &12;
  writeln(a);   // 10
  writeln(b);   // 10
  writeln(c);   // 10
end.