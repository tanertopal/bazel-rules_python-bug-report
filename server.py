
import tensorflow as tf
import tensorflow_io as tfio

if __name__ == '__main__':
    # Succeeded when we install tensorflow_io by using pip.
    # Failed when we use bazel, bacause 
    # https://github.com/bazelbuild/rules_python/blob/main/python/pip_install/extract_wheels/lib/purelib.py#L49
    # skip to extract purelib to target directory.
    print(tfio.__version__)
