"""Apply host compatibility flags before PlatformIO creates build environments."""
import os

Import("env")

if env.get("PIOENV") == "test_native_xray" and os.name == "nt":
    env.Append(BUILD_UNFLAGS=[
        "-fxray-instrument",
        "-fxray-instruction-threshold=1",
    ])
