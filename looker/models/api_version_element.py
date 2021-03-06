# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class ApiVersionElement(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ApiVersionElement - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'version': 'str',
            'full_version': 'str',
            'status': 'str',
            'swagger_url': 'str'
        }

        self.attribute_map = {
            'version': 'version',
            'full_version': 'full_version',
            'status': 'status',
            'swagger_url': 'swagger_url'
        }

        self._version = None
        self._full_version = None
        self._status = None
        self._swagger_url = None

    @property
    def version(self):
        """
        Gets the version of this ApiVersionElement.
        Version number as it appears in '/api/xxx/' urls

        :return: The version of this ApiVersionElement.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ApiVersionElement.
        Version number as it appears in '/api/xxx/' urls

        :param version: The version of this ApiVersionElement.
        :type: str
        """
        self._version = version

    @property
    def full_version(self):
        """
        Gets the full_version of this ApiVersionElement.
        Full version number including minor version

        :return: The full_version of this ApiVersionElement.
        :rtype: str
        """
        return self._full_version

    @full_version.setter
    def full_version(self, full_version):
        """
        Sets the full_version of this ApiVersionElement.
        Full version number including minor version

        :param full_version: The full_version of this ApiVersionElement.
        :type: str
        """
        self._full_version = full_version

    @property
    def status(self):
        """
        Gets the status of this ApiVersionElement.
        Status of this version

        :return: The status of this ApiVersionElement.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ApiVersionElement.
        Status of this version

        :param status: The status of this ApiVersionElement.
        :type: str
        """
        self._status = status

    @property
    def swagger_url(self):
        """
        Gets the swagger_url of this ApiVersionElement.
        Url for swagger.json for this version

        :return: The swagger_url of this ApiVersionElement.
        :rtype: str
        """
        return self._swagger_url

    @swagger_url.setter
    def swagger_url(self, swagger_url):
        """
        Sets the swagger_url of this ApiVersionElement.
        Url for swagger.json for this version

        :param swagger_url: The swagger_url of this ApiVersionElement.
        :type: str
        """
        self._swagger_url = swagger_url

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

