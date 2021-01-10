<img src="http://mypy-lang.org/static/mypy_light.svg" alt="mypy logo" width="300px"/>

Stubs for AWS Lambda Python Runtime Interface Client(awslambdaric)
==================================================================

![Test](https://github.com/toidi/awslambdaric-stubs/workflows/Test/badge.svg)

This package contains [type stubs](https://www.python.org/dev/peps/pep-0561/) to
provide more precise static types and type inference for [AWS Lambda Python
Runtime
Interface(awslambdaric)](https://github.com/aws/aws-lambda-python-runtime-interface-client).

`awslambdaric` uses dynamic Python features that makes having precise types for
some code patterns problematic. The final goal is to be able to get precise
types for most common patterns. Currently, `LambdaContext` class is supported. A
simple example:

```python
from awslambdaric.lambda_context import LambdaContext

def lambda_handler(event: dict, context: LambdaContext):
    message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])
    return {
        'request_id': context.aws_request_id,
        'message' : message,
    }
```

## Installation

Install latest published version as:

```console
$ pip install -U awslambdaric-stubs
```

To install the development version of the package:

```console
$ git clone https://github.com/toidi/awslambdaric-stubs.git
$ cd awslambdaric-stubs
$ pip install -U .
```

## Development Setup

First, clone the repo and cd into it, like in _Installation_, then:

```console
$ pip install -r dev-requirements.txt
```
