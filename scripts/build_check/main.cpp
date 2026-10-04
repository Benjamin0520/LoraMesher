// Entry point for `pio run` on native. Actual tests run via `pio test`.
#include <cstdio>

#ifndef PIO_UNIT_TESTING
int main() {
    std::puts("LoRaMesher native build check. Run pio test -e native to execute tests.");
    return 0;
}
#endif
