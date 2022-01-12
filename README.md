# Bazel rules_python bug report

**Related issue:** https://github.com/bazelbuild/rules_python/issues/603

## Update requirements lockfile

```bash
$ ./bazelisk run //:requirements.update

# Updates requirements.lock.txt which will end with this:
...
...
...
zipp==3.7.0 \
    --hash=sha256:9f50f446828eb9d45b267433fd3e9da8d801f614129124863f9c51ebceafb87d \
    --hash=sha256:b47250dd24f92b7dd6a0a8fc5244da14608f3ca90a5efcd37a3b1642fac9a375
    # via importlib-metadata

# WARNING: The following packages were not pinned, but pip requires them to be
# pinned when the requirements file includes hashes. Consider using the --allow-unsafe flag.
# setuptools
```

## Build

```bash
# This will fail
$ ./bazelisk build :server

...
Collecting wrapt==1.13.3
  Using cached wrapt-1.13.3-cp38-cp38-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (84 kB)
Collecting zipp==3.7.0
  Using cached zipp-3.7.0-py3-none-any.whl (5.3 kB)
Collecting setuptools>=40.3.0
 (ERROR: In --require-hashes mode, all requirements must have their versions pinned with ==. These do not:
    setuptools>=40.3.0 from https://files.pythonhosted.org/packages/eb/53/0dd4c7960579da8be13fa9b2c2591643d37f323e3d79f8bc8b1b6c8e6217/setuptools-60.5.0-py3-none-any.whl#sha256=68eb94073fc486091447fcb0501efd6560a0e5a1839ba249e5ff3c4c93f05f90 (from google-auth==2.3.3->-r /home/tanto/development/tensorflow-io-bazel-test/requirements.lock.txt (line 41))
Traceback (most recent call last):
  File "/home/tanto/.pyenv/versions/3.8.12/lib/python3.8/runpy.py", line 194, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/tanto/.pyenv/versions/3.8.12/lib/python3.8/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/home/tanto/.cache/bazel/_bazel_tanto/af96a3edade469226adcfd4a038e828a/external/rules_python/python/pip_install/extract_wheels/__main__.py", line 5, in <module>
    main()
  File "/home/tanto/.cache/bazel/_bazel_tanto/af96a3edade469226adcfd4a038e828a/external/rules_python/python/pip_install/extract_wheels/__init__.py", line 69, in main
    subprocess.run(pip_args, check=True)
  File "/home/tanto/.pyenv/versions/3.8.12/lib/python3.8/subprocess.py", line 516, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/tanto/.pyenv/versions/3.8.12/bin/python3', '-m', 'pip', '--isolated', 'wheel', '-r', '/home/tanto/development/tensorflow-io-bazel-test/requirements.lock.txt']' returned non-zero exit status 1.
)
INFO: Elapsed time: 17.707s
INFO: 0 processes.
FAILED: Build did NOT complete successfully (0 packages loaded)
    currently loading:
```

## Problem / Issue

The resulting `requirements.lock.txt` file contains in the last line the following comment:

```
# WARNING: The following packages were not pinned, but pip requires them to be
# pinned when the requirements file includes hashes. Consider using the --allow-unsafe flag.
# setuptools
```

which seems to break bazel build.
