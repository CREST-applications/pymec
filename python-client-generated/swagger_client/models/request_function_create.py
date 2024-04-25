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

class RequestFunctionCreate(object):
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
        'code_id': 'str',
        'runtime': 'str'
    }

    attribute_map = {
        'code_id': 'code_id',
        'runtime': 'runtime'
    }

    def __init__(self, code_id=None, runtime=None):  # noqa: E501
        """RequestFunctionCreate - a model defined in Swagger"""  # noqa: E501
        self._code_id = None
        self._runtime = None
        self.discriminator = None
        self.code_id = code_id
        self.runtime = runtime

    @property
    def code_id(self):
        """Gets the code_id of this RequestFunctionCreate.  # noqa: E501

        Codex ID.  Hic campus debet esse validus ID adhibet ad obiectum BLOB datum (alias, dID). (Verificatio validitatis nondum implementata est)  Non suadetur: Si haec functio anonyma nullam postulationem scripti requirit, uti potes 0 ut valor huius campi. In hoc systemate, 0 erit validus BLOB objectus ID qui normaliter per GET /data/0/blob potest descendi. (Nondum implementatum)  Hic ID debet esse integer signatus 64-bitum adhibet ad praesens obiectum BLOB datum, quia JSON non potest integer non signatum 64-bitum tractare, stringam utere.  # noqa: E501

        :return: The code_id of this RequestFunctionCreate.  # noqa: E501
        :rtype: str
        """
        return self._code_id

    @code_id.setter
    def code_id(self, code_id):
        """Sets the code_id of this RequestFunctionCreate.

        Codex ID.  Hic campus debet esse validus ID adhibet ad obiectum BLOB datum (alias, dID). (Verificatio validitatis nondum implementata est)  Non suadetur: Si haec functio anonyma nullam postulationem scripti requirit, uti potes 0 ut valor huius campi. In hoc systemate, 0 erit validus BLOB objectus ID qui normaliter per GET /data/0/blob potest descendi. (Nondum implementatum)  Hic ID debet esse integer signatus 64-bitum adhibet ad praesens obiectum BLOB datum, quia JSON non potest integer non signatum 64-bitum tractare, stringam utere.  # noqa: E501

        :param code_id: The code_id of this RequestFunctionCreate.  # noqa: E501
        :type: str
        """
        if code_id is None:
            raise ValueError("Invalid value for `code_id`, must not be `None`")  # noqa: E501

        self._code_id = code_id

    @property
    def runtime(self):
        """Gets the runtime of this RequestFunctionCreate.  # noqa: E501

        The runtime field corresponds to the interpreter that should be used by this anonymous function. Currently, the system does not perform any validity checks on this field, and using a runtime name that does not exist in the system will generate a new corresponding runtime. This runtime field will be used for capability checks, so it needs to match the field used for logging in the worker.  Campus `runtime` ad interpretatorem respondet, qui ab hac functione anonyma uti debet. Hactenus, systema nullas probationes de validitate in hoc campo agit, et nomen campus runtime, quod in systemate non existit, generabit novum campus runtime correspondens. Hic campus `runtime` ad probationes facultatis utetur, itaque congruere debet cum campo, qui ad logginum in opifice utitur.  # noqa: E501

        :return: The runtime of this RequestFunctionCreate.  # noqa: E501
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this RequestFunctionCreate.

        The runtime field corresponds to the interpreter that should be used by this anonymous function. Currently, the system does not perform any validity checks on this field, and using a runtime name that does not exist in the system will generate a new corresponding runtime. This runtime field will be used for capability checks, so it needs to match the field used for logging in the worker.  Campus `runtime` ad interpretatorem respondet, qui ab hac functione anonyma uti debet. Hactenus, systema nullas probationes de validitate in hoc campo agit, et nomen campus runtime, quod in systemate non existit, generabit novum campus runtime correspondens. Hic campus `runtime` ad probationes facultatis utetur, itaque congruere debet cum campo, qui ad logginum in opifice utitur.  # noqa: E501

        :param runtime: The runtime of this RequestFunctionCreate.  # noqa: E501
        :type: str
        """
        if runtime is None:
            raise ValueError("Invalid value for `runtime`, must not be `None`")  # noqa: E501

        self._runtime = runtime

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
        if issubclass(RequestFunctionCreate, dict):
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
        if not isinstance(other, RequestFunctionCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
