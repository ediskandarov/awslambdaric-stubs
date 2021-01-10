from distutils.core import setup

install_instructions = """\
# Experimental awslambdaric type stubs

This package contains type stubs to provide more precise
static types and type inference for awslambdaric. awslambdaric uses
dynamic Python features that are hard to understand by static type checkers,
this is why the plugin is needed in addition to type stubs.

## Installation

```console
$ pip install awslambdaric-stubs
```

"""


setup(
    name="awslambdaric-stubs",
    description="Stubs for AWS Lambda Python Runtime Interface Client(awslambdaric)",
    long_description=install_instructions,
    long_description_content_type='text/markdown',
    version="0.1.0",
    author='Eduard Iskandarov',
    author_email='eduard.iskandarov@yandex.ru',
    license='MIT License',
    url="https://github.com/toidi/awslambdaric-stubs",
    package_data={"awslambdaric-stubs": ["__init__.pyi", "lambda_context.pyi"]},
    packages=["awslambdaric-stubs"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3'
    ],
)
