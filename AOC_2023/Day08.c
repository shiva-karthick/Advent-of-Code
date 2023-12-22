#include "header_files/common.h"
#include "header_files/debug.h"
#include <stdbool.h> /* prevents lsp from flagging debug_raw as an error */

#define BUFFER 1024

static char dirs[512];
static char names[BUFFER][4];
static size_t map[BUFFER][2]; /* left and right */
static size_t nnames, zzz;

/* Given the char *name,  */
static size_t get_name_idx(const char *name)
{
  size_t i;

  for (i = 0; i < nnames; ++i)
    if (!strcmp(names[i], name))
    {
      return i;
    }

  assert(nnames < LEN(names));
  snprintf(names[nnames], LEN(*names), "%s", name);
  return nnames++;
}

/* returns no. steps to first terminal */
static int count_steps(size_t pos, int part)
{
  int step = 0;
  char *dir;

  for (dir = dirs;; dir++, step++)
  {
    if ((!part && pos == zzz) || (part && names[pos][2] == 'Z'))
      return step;
    if (*dir != 'R' && *dir != 'L') /* reset the dirs */
      dir = dirs;
    pos = map[pos][*dir == 'R'];
  }
}

int main(int argc, char **argv)
{
  char name[4], left[4], right[4]; /* Remember to include null terminator */
  size_t pos;
  int64_t p1, p2 = 0, steps, inc;

  if (argc > 1)
    freopen(argv[1], "r", stdin);

  /* Get a string of directions from a stream. */
  fgets(dirs, sizeof(dirs), stdin);

  while (fscanf(stdin, " %3s = (%3s, %3s)", name, left, right) == 3)
  {

    printf("name : left : right = %s, %s, %s \n", name, left, right);

    pos = get_name_idx(name);

    debug_raw("pos : ", pos);

    map[pos][0] = get_name_idx(left);
    map[pos][1] = get_name_idx(right);

    debug_raw("map[pos][0] = ", map[pos][0], "map[pos][1] = ", map[pos][1],
              "\n---\n");
  }

  zzz = get_name_idx("ZZZ");
  debug_raw("ZZZ = ", zzz);
  debug_raw("AAA = ", get_name_idx("AAA"));

  p1 = count_steps(get_name_idx("AAA"), 0);

  debug_raw("part 1 answer : ", p1);

  /*
   * Part 2. Using Lowest Common Multiple assuming that: Ah I got it!
   *  - all routes are cyclic
   *  - exactly 1 terminal is visited each cycle
   *  - period = first terminal, ie: terminals at 0(mod period)
   */
  for (pos = 0; pos < nnames; pos++)
  {
    if (names[pos][2] == 'A')
    {
      steps = count_steps(pos, 1);
      if (!p2)
        p2 = steps; /* p2 is old steps */
      else
        for (inc = p2; p2 % steps; p2 += inc)
          ;
    }
  }
  debug_raw("p2 : ", p2);

  /* print the names array */
  /* printf("\n names \n"); */
  /* for (size_t i = 0; i < LEN(names); ++i) { */
  /*   for (size_t j = 0; j < LEN(*names); ++j) */
  /*     printf("names[%zu][%zu] : %c \n", i, j, names[i][j]); */
  /*   printf("\n"); */
  /* } */

  /* print the map array */
  /* printf("\n Map \n"); */
  /* for (size_t i = 0; i < LEN(map); ++i) { */
  /*   for (size_t j = 0; j < LEN(*map); ++j) */
  /*     printf("map[%zu][%zu] : %zu \n", i, j, map[i][j]); */
  /*   printf("\n"); */
  /* } */

  return 0;
}
