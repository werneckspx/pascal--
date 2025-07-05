program mega_teste;
var
  a, b, c: integer;
  x, y: real;
  s, t: string;
  flag: boolean;
  i, j: integer;
  // a: real;            // ERRO: declaração duplicada
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

  // Teste comandos vazios (deve dar erro)
  //;
  //;

  // Teste atribuição de tipos incompatíveis (erro)
  //a := "string";      // ERRO
  //s := 123;           // ERRO
  //flag := 10;         // ERRO

  // Teste operação aritmética inválida
  //a := s + 1;         // ERRO

  // Teste operação lógica inválida
  //flag := a and b;    // ERRO

  // Teste operação relacional inválida
  //if s < 5 then       // ERRO
  //  writeln("erro relacional");

  // Teste uso de variável não declarada
  //z := 10;            // ERRO

  // Teste break/continue fora de laço
  //break;              // ERRO
  //continue;           // ERRO

end.