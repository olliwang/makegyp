#include <stdio.h>

#include "zlib.h"


int main(int argc, char **argv) {
  printf("zlibVersion(): %s\n", zlibVersion());
  return 0;
}
