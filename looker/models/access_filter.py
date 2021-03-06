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


class AccessFilter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AccessFilter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'model': 'str',
            'field': 'str',
            'value': 'str',
            'url': 'str',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'model': 'model',
            'field': 'field',
            'value': 'value',
            'url': 'url',
            'can': 'can'
        }

        self._id = None
        self._model = None
        self._field = None
        self._value = None
        self._url = None
        self._can = None

    @property
    def id(self):
        """
        Gets the id of this AccessFilter.
        ID of this AccessFilter

        :return: The id of this AccessFilter.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AccessFilter.
        ID of this AccessFilter

        :param id: The id of this AccessFilter.
        :type: int
        """
        self._id = id

    @property
    def model(self):
        """
        Gets the model of this AccessFilter.
        Model to which this filter applies

        :return: The model of this AccessFilter.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this AccessFilter.
        Model to which this filter applies

        :param model: The model of this AccessFilter.
        :type: str
        """
        self._model = model

    @property
    def field(self):
        """
        Gets the field of this AccessFilter.
        Field to which this filter applies

        :return: The field of this AccessFilter.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this AccessFilter.
        Field to which this filter applies

        :param field: The field of this AccessFilter.
        :type: str
        """
        self._field = field

    @property
    def value(self):
        """
        Gets the value of this AccessFilter.
        Value for this filter

        :return: The value of this AccessFilter.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AccessFilter.
        Value for this filter

        :param value: The value of this AccessFilter.
        :type: str
        """
        self._value = value

    @property
    def url(self):
        """
        Gets the url of this AccessFilter.
        Link to get this item

        :return: The url of this AccessFilter.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this AccessFilter.
        Link to get this item

        :param url: The url of this AccessFilter.
        :type: str
        """
        self._url = url

    @property
    def can(self):
        """
        Gets the can of this AccessFilter.
        Operations the current user is able to perform on this object

        :return: The can of this AccessFilter.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this AccessFilter.
        Operations the current user is able to perform on this object

        :param can: The can of this AccessFilter.
        :type: dict(str, bool)
        """
        self._can = can

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

