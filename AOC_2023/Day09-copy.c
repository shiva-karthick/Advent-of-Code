#include "header_files/common.h"
#include "header_files/debug.h"
#include <stdbool.h>

/* --- Day 9: Mirage Maintenance --- */

int main(int argc, char **argv)
{

  static char line[128];
  static long a[24][24]; /* long for 16-bit platforms */

  long array[24] = {0};
  size_t n, d, i, depth = 0, check_count = 0;
  double difference = 0;

  char *tok, *rest;
  long p1 = 0, p2 = 0, acc1 = 0, acc2 = 0; /* long for 16-bit platforms */
  int nz;

  if (argc > 1)
    freopen(argv[1], "r", stdin);

  while ((rest = fgets(line, sizeof(line), stdin)))
  {
    for (n = 0; (tok = strsep(&rest, " ")); n++)
    {
      assert(n < LEN(*a));
      a[0][n] = atol(tok);
      printf("%ld,", a[0][n]);
    }

    printf("\n number of values : %zu\n", n);

    /* generate rows until all 0, 'd' is depth */
    for (d = 1, nz = 1; nz && d < n; d++)
    {
      printf("depth : %zu\n", d);
      for (i = 0, nz = 0; i < n - d; i++)
      {
        printf("a[%zu][%zu] - a[%zu][%zu] : %ld\n", d - 1, i + 1, d - 1, i, a[d - 1][i + 1] - a[d - 1][i]);
        nz |= (a[d][i] = a[d - 1][i + 1] - a[d - 1][i]);
        printf("nz : %d\n", nz);
        printf("a[%zu][%zu] : %ld\n", d, i, a[d][i]);
      }
      printf("Exit inner loop\n");
    }

    /* extrapolate forward and backwards */
    for (i = 0, acc1 = acc2 = 0; i < d; i++)
    {
      acc1 += a[d - i - 1][n - d + i];
      acc2 = a[d - i - 1][0] - acc2;
    }

    p1 += acc1;
    p2 += acc2;
  }

  printf("09: %ld %ld\n", p1, p2);
  return 0;
}
