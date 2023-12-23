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

  /* Loop until we have read all the lines in the file */
  while ((rest = fgets(line, sizeof(line), stdin)))
  {

    /* Parse and collect the values in the array */
    for (n = 0; (tok = strsep(&rest, " ")); n++)
    {
      assert(n < LEN(*a)); /* make sure the length of the parsed values is less
                              than the length of the array*/
      array[n] = atol(tok);
    }
    /*  */

    /* print out the length of the array, e.g. n = 6 */
    printf("n : %zu\n", n);

    /* print the initial contents of the array */
    /* for (size_t i = 0; i < LEN(array); i++) */
    /*   printf("%ld,", array[i]); */
    /* printf("\n---\n"); */

    /* run the while loop until the array has all zeros, then we break */
    while (1)
    {
      for (size_t i = 0; i < (n - (depth + 1)); i++)
      {
        printf("i : %zu\n", i);
        difference = array[i] - array[i + 1];
        printf("difference : %f\n", difference);
        array[i] = (long)abs(difference); /* cast to long type */
      }

      /* print out the the array, e.g. n = 6 */
      for (size_t ii = 0; ii < n; ii += 1)
        printf("%ld,", array[ii]);

      printf("\nDepth %zu\n", depth + 1);
      printf("\n---\n");

      /* check if the array is all zeroes, if then break */
      for (long i = 0; i < (n - (depth + 1)); i++)
      {
        if (array[i] == 0)
          check_count += 1;
      }
      if (check_count == (n - (depth + 1)))
      {
        for (size_t i = 0; i < n; i++)
        {
          acc1 += array[i];
        }
        break;
      }
      /*  */

      check_count = 0; // reset the variable
      /* Use 0-indexing when calculating the depth */
      depth += 1;
    }

    printf("current acc1 is : %zu\n", acc1);
    p1 += acc1; /* add the acc1 to the p1 */
    acc1 = 0;   /* reset for the next tree */
    depth = 0;  /* reset for the next tree */
    check_count = 0;
  }

  printf("p1 : %ld \n", p1);

  return 0;
}
