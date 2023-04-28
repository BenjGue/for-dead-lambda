import aws_cdk as core
import aws_cdk.assertions as assertions

from onf_aws_lambda_container_python.onf_aws_lambda_container_python_stack import OnfAwsLambdaContainerPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in onf_aws_lambda_container_python/onf_aws_lambda_container_python_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = OnfAwsLambdaContainerPythonStack(app, "onf-aws-lambda-container-python")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
