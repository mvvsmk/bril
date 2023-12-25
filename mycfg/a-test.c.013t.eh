
;; Function main (main, funcdef_no=0, decl_uid=3174, cgraph_uid=1, symbol_order=0)

int main ()
{
  int a;
  int D.3181;

  a = 4;
  if (a != 4) goto <D.3179>; else goto <D.3180>;
  <D.3179>:
  a = 2;
  <D.3180>:
  somewhere:
  printf ("%d", a);
  D.3181 = 0;
  goto <D.3182>;
  D.3181 = 0;
  goto <D.3182>;
  <D.3182>:
  return D.3181;
}


