from aws_cdk import Stack, aws_lambda, Duration
from constructs import Construct 

class OnfAwsLambdaContainerPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        function = aws_lambda.DockerImageFunction(self, "lambda_function",
                                    code= aws_lambda.DockerImageCode.from_image_asset("./assets"), timeout=Duration.seconds(30))



        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "OnfAwsLambdaContainerPythonQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
