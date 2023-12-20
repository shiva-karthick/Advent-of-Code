#include "common.h"

struct mapent {
  int64_t src, dst, len;
};

struct range {
  int64_t off, len;
};

static int64_t seeds[24]; // array

/*  Each element in the array is of type mapent */
static struct mapent maps[8][50];

static size_t nseeds, ntypes;

/* This code defines a function named mk_range that creates and returns a new
 * struct range object with the specified offset and length.  */
static struct range mk_range(int64_t off, int64_t len) {
  struct range r; /* Initialise the new struct range r */
  r.off = off;
  r.len = len;
  return r;
}

static void parse(void) {

  static char line[256];
  char *rest, *tok;
  size_t nents = 0;
  int nt;

  rest = fgets(line, sizeof(line), stdin);
  strsep(&rest, " "); /* skip 'seeds:' */

  while ((tok = strsep(&rest, " "))) {
    assert(nseeds < LEN(seeds));
    seeds[nseeds++] = strtoll(tok, NULL, 10);
  }

  // print out the contents of seeds
  for (int ii = 0; ii < 24; ++ii)
    printf("Seed : %i is %" PRIi64 "\n", ii, seeds[ii]);

  while ((rest = fgets(line, sizeof(line), stdin)))
    if (!isalnum(rest[0])) // The line if (!isalnum(rest[0])) within the
                           // provided code block checks the first character
                           // (rest[0]) of the string read by fgets and takes no
                           // action if it's not alphanumeric.
      ;
    else if (isalpha(rest[0])) { /* seed-to-soil map, add new map*/
      assert(ntypes < LEN(maps));
      ntypes++;
      nents = 0;
    } else {
      assert(nents < LEN(*maps));
      nt = sscanf(rest, "%" PRIi64 " %" PRIi64 " %" PRIi64,
                  &maps[ntypes - 1][nents].dst, &maps[ntypes - 1][nents].src,
                  &maps[ntypes - 1][nents].len);
      assert(nt ==
             3); // make sure the "list" of instructions are in set of three's'
      nents++;   // add the next instruction in the SAME map
    }
}

static struct range map_range(int t, struct range r) {
  struct mapent *e;
  size_t i;
  int64_t next; /* lowest mapped range above r */

  if ((size_t)t >= ntypes)
    return r;

  next = r.off + r.len;         /* 79 + 1 = 80 */

  for (i = 0; i < LEN(maps[i]) && (e = &maps[t][i])->len; i++)
    if (r.off < e->src)
      next = MIN(next, e->src);
    else if (r.off < e->src + e->len)
      return mk_range(r.off + e->dst - e->src,
                      MIN(r.len, e->src + e->len - r.off));

  /* no match */
  return mk_range(r.off, next - r.off);
}

static int64_t recur(int t, struct range r) {
  struct range mapped; /* Initialise a varaible of type struct range */
  int64_t best = INT64_MAX;

  /* Base Case */
  if ((size_t)t >= ntypes)
    return r.off;

  while (r.len) {
    mapped = map_range(t, r);
    best = MIN(best, recur(t + 1, mapped));
    r.off += mapped.len;
    r.len -= mapped.len;
  }

  return best;
}

int main(int argc, char **argv) {
  int64_t p1 = INT64_MAX, p2 = INT64_MAX;
  size_t i;

  // Reassigns stdin to the file specified
  freopen("/home/shankar/Shiva/Advent-of-Code/AOC_2023/data/day5a.txt", "r",
          stdin);

  parse();

  for (i = 0; i < nseeds; i++)
    p1 = MIN(p1, recur(0, mk_range(seeds[i], 1)));
  for (i = 0; i < nseeds - 1; i += 2)
    p2 = MIN(p2, recur(0, mk_range(seeds[i], seeds[i + 1])));

  printf("Day 05: %" PRIi64 " %" PRIi64 "\n", p1, p2);
  return 0;
}
