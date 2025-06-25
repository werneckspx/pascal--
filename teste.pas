program teste;
var
  a, a_1: integer;
  b: real;
  c: string;
  d: boolean;
begin
{
  a := (1 + 2);

  e: real;

  // Teste if-else com else if encadeado
  if a = 10 then
    writeln("a = 10");
  else if b > 10 then
    writeln("b eh maior que 10");
  else
    writeln("nenhuma condição satisfeita");
  
  if a < b then
    if c > d then
      x := 1;
    else
      x := 2;
  else
    x := 3;
  
  //Teste while
  while i < 10 do
    i := i + 1;

  //Teste while com break 
  while a < 10 do
  begin
    a := a + 1;
    if a = 7 then
      break;
  end;

  //Teste while com continue 
  while a < 10 do
  begin
    a := a + 1;
    if a = 7 then
      continue;
  end;

  //Teste while com if e continue
  while a < 10 do
  begin
    if a = 7 then
      continue;
    if c > d then
      x := 1;
    else
      x := 2;
  end;

  //Teste while com if e break
  while a < 10 do
  begin
    if a = 7 then
      break;
    if c > d then
      x := 1;
    else
      x := 2;
  end;

  // Teste break e continue
  for b := 1 to 10 do
  begin
    if b = 5 then
      continue;
    writeln(b);
  end;

  // Teste expressões com operadores lógicos e relacionais
  if (a > 5) and (b < 30) or not (a = 0) then
    writeln("expressao logica verdadeira");

  // Teste erros sintáticos (comentados para evitar erro de parse)
  // a 10; // erro: falta operador :=
  // if a = then writeln("erro"); // erro: expressão incompleta
  // for a := 1 to do writeln(a); // erro: falta valor final no for
  // while do writeln(a); // erro: falta expressão no while
  // writeln("teste" // erro: falta parêntese fechando}

//Teste for
  for a := 1 to 5 do
    writeln(a);

  for i := 0 to 4 do 
    sum := sum + i;

//Teste for encadeado
  for i := 0 to 2 do
    for j := 0 to 1 do
      total := total + (i * j);
end.




