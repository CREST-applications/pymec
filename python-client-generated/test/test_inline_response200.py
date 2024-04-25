# coding: utf-8

"""
    MEC-RM API

    This is the MEC Recource Manager API specification.  Current Version: v0.5.0.2 (Major: 0.5, Minor: 0, Patch: 2)  As a general-purpose stateless middleware, we have designed this system with a high level of flexibility. There is no predefined API invocation flow in this system. Application developers have the freedom to creatively develop different invocation flows based on their specific needs. In fact, this application-centric flexible development is what we advocate and one of the main driving forces behind our transition from RPC-based APIs to stateless APIs.  The document covers not-fixed fields which may not compatable between versions. (espesilly version change greater than minor version)  For implement of non-published APIs, you can reference the source code by your own responsibility.  ## Documents: * [API Document](https://mecdoc.dolylab.cc/)  # noqa: E501

    OpenAPI spec version: v0.5.0.2
    Contact: nb22509@shibaura-it.ac.jp
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_client.rest import ApiException


class TestInlineResponse200(unittest.TestCase):
    """InlineResponse200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInlineResponse200(self):
        """Test InlineResponse200"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.inline_response200.InlineResponse200()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
