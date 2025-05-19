program teste;
var
  a, a_1: integer;
  b: real;
  c: string;
begin
  a := 10;
  b := 20.5;
  
  c := {a
  m
  e
  m
  }
   "texto";

  ;

  a := (1 + 2) * (-3) - 4 / 2 mod 2 div 1;

  // Teste if-else com else if encadeado
  if a = 10 then
    writeln("a = 10");
  else if b > 10 then
    writeln("b eh maior que 10");
  else
    writeln("nenhuma condição satisfeita");

  // Teste for
  for a := 1 to 5 do
    writeln(a);

  // Teste while
  while a < 10 do
  begin
    a := a + 1;
    if a = 7 then
      break;
  end;

  // Teste break e continue
  for b := 1 to 10 do
  begin
    if b = 5 then
      continue;
    writeln(b);
  end;

  // Teste chamadas de procedimento simples
  clrscr;
  readln(a);
  writeln(c);

  // Teste expressões com operadores lógicos e relacionais
  if (a > 5) and (b < 30) or not (a = 0) then
    writeln("expressao logica verdadeira");

  // Teste erros sintáticos (comentados para evitar erro de parse)
  // a 10; // erro: falta operador :=
  // if a = then writeln("erro"); // erro: expressão incompleta
  // for a := 1 to do writeln(a); // erro: falta valor final no for
  // while do writeln(a); // erro: falta expressão no while
  // writeln("teste" // erro: falta parêntese fechando
end.
