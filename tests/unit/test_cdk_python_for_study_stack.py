import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_python_for_study.cdk_python_for_study_stack import CdkPythonForStudyStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_python_for_study/cdk_python_for_study_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkPythonForStudyStack(app, "cdk-python-for-study")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
