# coding: utf-8

"""
    MEC-RM API

    This is the MEC Recource Manager API specification.  Current Version: v0.5.0.2 (Major: 0.5, Minor: 0, Patch: 2)  As a general-purpose stateless middleware, we have designed this system with a high level of flexibility. There is no predefined API invocation flow in this system. Application developers have the freedom to creatively develop different invocation flows based on their specific needs. In fact, this application-centric flexible development is what we advocate and one of the main driving forces behind our transition from RPC-based APIs to stateless APIs.  The document covers not-fixed fields which may not compatable between versions. (espesilly version change greater than minor version)  For implement of non-published APIs, you can reference the source code by your own responsibility.  ## Documents: * [API Document](https://mecdoc.dolylab.cc/)  # noqa: E501

    OpenAPI spec version: v0.5.0.2
    Contact: nb22509@shibaura-it.ac.jp
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseWorkerContract(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'int',
        'status': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'code': 'code',
        'status': 'status',
        'job_id': 'job_id'
    }

    def __init__(self, code=None, status=None, job_id=None):  # noqa: E501
        """ResponseWorkerContract - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._status = None
        self._job_id = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if status is not None:
            self.status = status
        if job_id is not None:
            self.job_id = job_id

    @property
    def code(self):
        """Gets the code of this ResponseWorkerContract.  # noqa: E501


        :return: The code of this ResponseWorkerContract.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ResponseWorkerContract.


        :param code: The code of this ResponseWorkerContract.  # noqa: E501
        :type: int
        """

        self._code = code

    @property
    def status(self):
        """Gets the status of this ResponseWorkerContract.  # noqa: E501


        :return: The status of this ResponseWorkerContract.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseWorkerContract.


        :param status: The status of this ResponseWorkerContract.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def job_id(self):
        """Gets the job_id of this ResponseWorkerContract.  # noqa: E501

        Job ID. This ID should be an 64-bit signed integer. since JSON is not able to handle 64-bit unsigned integer, use string instead. This object can be null if no job is available.  # noqa: E501

        :return: The job_id of this ResponseWorkerContract.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ResponseWorkerContract.

        Job ID. This ID should be an 64-bit signed integer. since JSON is not able to handle 64-bit unsigned integer, use string instead. This object can be null if no job is available.  # noqa: E501

        :param job_id: The job_id of this ResponseWorkerContract.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ResponseWorkerContract, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResponseWorkerContract):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
