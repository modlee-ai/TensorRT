#
# SPDX-FileCopyrightText: Copyright (c) 1993-2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys
from setuptools import setup, find_packages


def no_publish():
    blacklist = ["register"]
    for cmd in blacklist:
        if cmd in sys.argv:
            raise RuntimeError('Command "{}" blacklisted'.format(cmd))


REQUIRED_PACKAGES = [
    "numpy",
    "onnx",
]


def main():
    no_publish()
    setup(
        name="modlee-onnx_graphsurgeon",
        # version=onnx_graphsurgeon.__version__,
        version="0.3.27",
        description="ONNX GraphSurgeon",
        long_description=open("README.md", "r", encoding="utf-8").read(),
        long_description_content_type="text/markdown",
        license="Apache 2.0",
        url="https://github.com/modlee-ai/TensorRT/tree/release/8.6/tools/onnx-graphsurgeon",
        author="NVIDIA",
        author_email="svc_tensorrt@nvidia.com",
        classifiers=[
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        install_requires=REQUIRED_PACKAGES,
        packages=find_packages(),
        zip_safe=True,
    )


if __name__ == "__main__":
    main()
