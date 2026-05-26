#include <stdio.h>
#include <stdlib.h>
#include <zxcvbn.h>

int main(void) {
#ifdef USE_DICT_FILE
  if (!ZxcvbnInit(ZXCVBN_DICT_FILE)) {
    return EXIT_FAILURE;
  }
#endif
  ZxcvbnMatch("password", NULL, NULL);

  return EXIT_SUCCESS;
}
