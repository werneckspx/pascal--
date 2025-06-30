{
program TesteOperacoes;
var
  a, b, c, d, e, f: integer;
  x, y, z, aux: real;
begin
  a := 10;
  b := 3;
  x := 2.5;
  y := 4.0;

  // Expressão com todas as operações entre inteiros
  c := a + b * 2 - 5 div 2 + 8 mod 3;
  writeln("c = ", c);
  
  // Expressão com todas as operações entre reais e inteiros
  z := x + y * 2.0 - a / b + 7.5;
  writeln("z = ", z);

  // Operações entre inteiro e real (resultado deve ser real)
  z := a + x;
  writeln("a + x = ", z);
  z := a - x;
  writeln("a - x = ", z);
  z := a * x;
  writeln("a * x = ", z);
  z := a / x;
  writeln("a / x = ", z);

  // Teste de while
  d := 0;
  while d < 5 do
  begin
    writeln("d = ", d);
    d := d + 1;
  end;

  // Teste de mod e div entre inteiros
  e := 17 div 3;
  f := 17 mod 3;
  writeln("17 div 3 = ", e);
  writeln("17 mod 3 = ", f);
end.
}


program TesteExpressaoCompleta;
var
  a, b, c, aux1: integer;
  x, y, aux: real;
  flag: boolean;
begin
  a := 10;
  b := 3;
  c := 2;
  x := 2.5;
  y := 4.0;

  aux := 9/2;
  aux1 := 9 div 2;

  if(4 >= (aux)) then
    writeln(aux);
  else if(4 >= (aux1)) then
    writeln(aux1);

  // Expressão única com todas as operações
  flag := not ( ((a + b * c - 5 div 2 + 8 mod 3) > (x + y * 2.0 - a / b + 7.5))
             and ((a < x) or (b >= c)) );

  write("flag = ", flag);
  a := 1;
  b:= 3;
  a := a+b*2;
  writeln("");
  writeln(a);

  writeln("Teste de Hexadecimais:");

  a := $A;      // 10 em decimal
  b := $1F;     // 31 em decimal
  c := $FF;     // 255 em decimal
  writeln(a);   // Deve imprimir 10
  writeln(b);   // Deve imprimir 31
  writeln(c);   // Deve imprimir 255

  writeln("Teste de Octais:");

  a := 10;
  b := $A;
  c := &12;
  writeln(a);   // 10
  writeln(b);   // 10
  writeln(c);   // 10

end.