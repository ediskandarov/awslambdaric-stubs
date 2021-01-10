"""Typing hints in this module are based on

https://github.com/aws/aws-lambda-python-runtime-interface-client/blob/main/awslambdaric/lambda_context.py
https://github.com/aws/aws-lambda-python-runtime-interface-client/blob/main/test/test_lambda_context.py

"""

from typing import Dict, Optional


class Client:
    app_package_name: Optional[str]
    app_title: Optional[str]
    app_version_code: Optional[str]
    app_version_name: Optional[str]
    installation_id: Optional[str]

class ClientContext:
    client: Client
    custom: Optional[Dict[str, str]]
    env: Optional[Dict[str, str]]

class CognitoIdentity:
    cognito_identity_id: Optional[str]
    cognito_identity_pool_id: Optional[str]

class LambdaContext:
    aws_request_id: str
    function_name: Optional[str]
    function_version: Optional[str]
    invoked_function_arn: Optional[str]
    log_group_name: Optional[str]
    log_stream_name: Optional[str]
    memory_limit_in_mb: Optional[str]

    client_context: ClientContext
    identity: CognitoIdentity

    def get_remaining_time_in_millis() -> int: ...
