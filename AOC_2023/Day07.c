/* --- Day 7: Camel Cards --- */
/* I am a master of c language */

/* Time to learn sorting algorithms
BUB - Bubble Sort,
SEL - Selection Sort,
INS - Insertion Sort,
MER - Merge Sort (recursive implementation),
QUI - Quick Sort (recursive implementation),
R-Q - Random Quick Sort (recursive implementation).*/

#include "common.h"

struct hand {
  char cards[6];
  int bet, type;
};

static struct hand hands[1024]; /* array of structs */
static size_t nhands = 0;
static int cur_part = 0; /* global to get it to cmp_hand */

static int cmp_int_desc(const void *a, const void *b) {
  return *(int *)b - *(int *)a;
}

/* Function to compare 2 hands */
static int cmp_hand(const void *a, const void *b) {
  const struct hand *ha = (struct hand *)a, *hb = (struct hand *)b;
  const char *order;
  size_t i, j;

  /* No need to perform second ordering rule */
  if (ha->type != hb->type)
    return ha->type - hb->type;

  /* Assign the order based on the value of cur_part */
  order = cur_part == 0 ? "23456789TJQKA" : "J23456789TQKA";

  /* Perform the second ordering rule */
  for (i = 0; i < LEN(ha->cards); i++) {
    if (ha->cards[i] == hb->cards[i])
      continue;
    /* Both cards are not the same */
    for (j = 0; order[j]; j++)
      if (order[j] == ha->cards[i])
        return -1;
      else if (order[j] == hb->cards[i])
        return 1;
  }

  return 0;
}

static int get_type(char *cards) {
  static int counts[256];
  int nj = 0;
  size_t i;

  memset(counts, 0, sizeof(counts));

  for (i = 0; cards[i]; i++) {
    printf("int value of cards[%zu] : %d \n", i, (int)cards[i]);
    counts[(int)cards[i]]++;
  }

  if (cur_part) {
    nj = counts['J']; /* get the number of J's */
    counts['J'] = 0;  /* clear the number of J's present in the counts array */
  }

  /* print counts */
  /* for (uint foo = 0; foo < 256; ++foo) */
  /*   printf("counts[%u] : %d \n", foo, counts[foo]); */

  /* sort only the few counts we care about */
  for (i = 0; i < 13; i++)
    counts[i] = counts[(int)"23456789TJQKA"[i]];

  printf("\n --- \n");
  for (uint foo = 0; foo < 13; ++foo)
    printf("counts[%u] : %d \n", foo, counts[foo]);

  qsort(counts, 13, sizeof(*counts), cmp_int_desc);

  printf("\n --- \n");
  for (uint foo = 0; foo < 13; ++foo)
    printf("counts[%u] : %d \n", foo, counts[foo]);

  /* classify into their respective types */
  if (counts[0] + nj == 5)
    return 6; /* AAAAA */
  if (counts[0] + nj == 4)
    return 5; /* AA8AA */
  if (counts[0] + nj == 3 && counts[1] == 2)
    return 4; /* 23332 */
  if (counts[0] == 3 && counts[1] + nj == 2)
    return 4; /*  */
  if (counts[0] + nj == 3)
    return 3;
  if (counts[0] + nj == 2 && counts[1] == 2)
    return 2;
  if (counts[0] == 2 && counts[1] + nj == 2)
    return 2;
  if (counts[0] + nj == 2)
    return 1;

  return 0;
}

/* long for 16-bit platforms to be as widely compatible as possible */
static long solve(void) {
  long score = 0;
  size_t i;

  /* precompute, avoids repeatedly doing it in cmp_hand */
  for (i = 0; i < nhands; ++i) {
    hands[i].type = get_type(hands[i].cards);
    printf("hands[%zu].type : %d \n", i, hands[i].type);
    /* if (i == 0) */
    /*   break; */
  }

  qsort(hands, nhands, sizeof(*hands), cmp_hand);

  for (i = 0; i < nhands; i++)
    score += hands[i].bet * (long)(i + 1);

  return score;
}

int main(int argc, char *argv[]) {
  long p1, p2; /* long for 16-bit platforms */
  int nt;

  if (argc > 1)
    freopen(argv[1], "r", stdin);
  printf("%s \n", argv[1]);

  while (1) {
    assert(nhands < LEN(hands)); /* checks if there's space in the hands array
                                    to avoid out-of-bounds errors. */
    nt = fscanf(stdin, " %5s %d", hands[nhands].cards, &hands[nhands].bet);
    if (nt != 2 || nt == EOF)
      break;
    nhands++;
  }
  printf("nhands : %ld \n", nhands);

  /* cur_part = 0; */
  /* p1 = solve(); */
  /* printf("part 1 : %ld \n", p1); */

  cur_part = 1;
  p2 = solve();
  printf("part 2 : %ld \n", p2);

  return 0;
}
