#!/usr/bin/env python3
import os
import sys

import aws_cdk as cdk

# プロジェクトルートを sys.pathに追加
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
print(os.path.dirname(__file__))

from lib.cdk_python_for_study_stack import CdkPythonForStudyStack


app = cdk.App()
CdkPythonForStudyStack(app, "CdkPythonForStudyStack",
)

app.synth()
