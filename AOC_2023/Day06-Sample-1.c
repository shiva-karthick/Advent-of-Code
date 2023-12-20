#include "common.h"
#include <stdbool.h>

static void parse_line(int64_t nums[4], int64_t *bignum) {
  static char line[64];
  char *s; /* a pointer named s to store an address of character value */

  /* fgets(line, sizeof(line), stdin); */
  /* A more safer way than the above, above statement, checks if fgets returns a
   * non-NULL pointer, indicating a successful read, while also considering the
   * case where the read reached the end of the file. This is relevant if you
   * expect input and reaching the end prematurely is an error. */
  assert(fgets(line, sizeof(line), stdin) != NULL || feof(stdin));

  sscanf(line, "%*s %" SCNi64 " %" SCNi64 " %" SCNi64 " %" SCNi64, &nums[0],
         &nums[1], &nums[2], &nums[3]);

  /* Print out the contents of nums */
  for (int i = 0; i < 4; ++i)
    printf("nums[%d] = %ld\n", i, nums[i]);

  for (*bignum = 0, s = line; *s; s++)
    if (isdigit(*s)) {
      printf("*s is %c\n", *s);
      *bignum = *bignum * 10 + (*s - '0');
    }
}

static int64_t solve(int64_t *times, int64_t *recs, size_t n) {
  size_t i;
  int64_t acc = 1, best, nbetter, tp, d;

  for (i = 0; i < n && times[i]; i++) {
    best = nbetter = 0;

    for (tp = 1; tp < times[i]; tp++) {
      d = tp * (times[i] - tp);
      if (d > recs[i])
        nbetter++;
      else if (d < best)
        break;
      best = d;
    }

    acc *= nbetter;
  }

  return acc;
}

int main(int argc, char **argv) {

  /* 0 means running for the sample data, and 1 for actual data */
  uint8_t flag = 1;
  uint8_t array_bounds = 0;

  if (!flag)
    array_bounds = 3;
  else {
    array_bounds = 4;
  }

  int64_t times[array_bounds], recs[array_bounds], bigtime, bigrec, p1 = 0,
                                                                    p2 = 0;

  /*
   * Return Value: stream on success, a null pointer on failure.
   * */
  assert(freopen("/home/shankar/Shiva/Advent-of-Code/AOC_2023/data/day6b.txt",
                 "r", stdin) != NULL);

  parse_line(times, &bigtime);
  printf("bignum is : %" SCNi64 "\n", bigtime);
  parse_line(recs, &bigrec);
  printf("bignum is : %" SCNi64 "\n", bigtime);

  /* print out the times and recs */
  for (int k = 0; k < LEN(times); ++k)
    printf("times[%d] %" PRIi64 " \n", k, times[k]);
  for (int k = 0; k < LEN(recs); ++k)
    printf("recs[%d] %" PRIi64 " \n", k, recs[k]);

  if (!flag) {
    p1 = solve(times, recs, 4);
    printf("Part 1 answer is %" PRIi64 "\n", p1);
  } else {
    p2 = solve(&bigtime, &bigrec, 1);
    printf("Part 2 answer is: %" PRIi64 "\n", p2);
  }

  return 0;
}
