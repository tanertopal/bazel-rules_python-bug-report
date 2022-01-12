load("@rules_python//python/pip_install:requirements.bzl", "compile_pip_requirements")
load("@rules_python//python:defs.bzl", "py_binary")
load("@test//:requirements.bzl", "requirement")

# Check that our compiled requirements are up-to-date
# Run
#   bazel run //:requirements.update
# to update requirements.txt
compile_pip_requirements(
    name = "requirements",
    requirements_in = "requirements.in.txt",
    requirements_txt = "requirements.lock.txt",
)

py_binary(
    name = "server",
    srcs = ["server.py"],
    deps = [
        requirement("tensorflow"),
    ],
)
