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


class Group(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Group - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'user_count': 'int',
            'contains_current_user': 'bool',
            'externally_managed': 'bool',
            'include_by_default': 'bool',
            'external_group_id': 'str',
            'can_add_to_content_metadata': 'bool',
            'can': 'dict(str, bool)'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'user_count': 'user_count',
            'contains_current_user': 'contains_current_user',
            'externally_managed': 'externally_managed',
            'include_by_default': 'include_by_default',
            'external_group_id': 'external_group_id',
            'can_add_to_content_metadata': 'can_add_to_content_metadata',
            'can': 'can'
        }

        self._id = None
        self._name = None
        self._user_count = None
        self._contains_current_user = None
        self._externally_managed = None
        self._include_by_default = None
        self._external_group_id = None
        self._can_add_to_content_metadata = None
        self._can = None

    @property
    def id(self):
        """
        Gets the id of this Group.
        Unique Id

        :return: The id of this Group.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Group.
        Unique Id

        :param id: The id of this Group.
        :type: int
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Group.
        Name of group

        :return: The name of this Group.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Group.
        Name of group

        :param name: The name of this Group.
        :type: str
        """
        self._name = name

    @property
    def user_count(self):
        """
        Gets the user_count of this Group.
        Number of users included in this group

        :return: The user_count of this Group.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """
        Sets the user_count of this Group.
        Number of users included in this group

        :param user_count: The user_count of this Group.
        :type: int
        """
        self._user_count = user_count

    @property
    def contains_current_user(self):
        """
        Gets the contains_current_user of this Group.
        Currently logged in user is group member

        :return: The contains_current_user of this Group.
        :rtype: bool
        """
        return self._contains_current_user

    @contains_current_user.setter
    def contains_current_user(self, contains_current_user):
        """
        Sets the contains_current_user of this Group.
        Currently logged in user is group member

        :param contains_current_user: The contains_current_user of this Group.
        :type: bool
        """
        self._contains_current_user = contains_current_user

    @property
    def externally_managed(self):
        """
        Gets the externally_managed of this Group.
        Group membership controlled outside of Looker

        :return: The externally_managed of this Group.
        :rtype: bool
        """
        return self._externally_managed

    @externally_managed.setter
    def externally_managed(self, externally_managed):
        """
        Sets the externally_managed of this Group.
        Group membership controlled outside of Looker

        :param externally_managed: The externally_managed of this Group.
        :type: bool
        """
        self._externally_managed = externally_managed

    @property
    def include_by_default(self):
        """
        Gets the include_by_default of this Group.
        New users are added to this group by default

        :return: The include_by_default of this Group.
        :rtype: bool
        """
        return self._include_by_default

    @include_by_default.setter
    def include_by_default(self, include_by_default):
        """
        Sets the include_by_default of this Group.
        New users are added to this group by default

        :param include_by_default: The include_by_default of this Group.
        :type: bool
        """
        self._include_by_default = include_by_default

    @property
    def external_group_id(self):
        """
        Gets the external_group_id of this Group.
        External Id group if embed group

        :return: The external_group_id of this Group.
        :rtype: str
        """
        return self._external_group_id

    @external_group_id.setter
    def external_group_id(self, external_group_id):
        """
        Sets the external_group_id of this Group.
        External Id group if embed group

        :param external_group_id: The external_group_id of this Group.
        :type: str
        """
        self._external_group_id = external_group_id

    @property
    def can_add_to_content_metadata(self):
        """
        Gets the can_add_to_content_metadata of this Group.
        Group can be used in content access controls

        :return: The can_add_to_content_metadata of this Group.
        :rtype: bool
        """
        return self._can_add_to_content_metadata

    @can_add_to_content_metadata.setter
    def can_add_to_content_metadata(self, can_add_to_content_metadata):
        """
        Sets the can_add_to_content_metadata of this Group.
        Group can be used in content access controls

        :param can_add_to_content_metadata: The can_add_to_content_metadata of this Group.
        :type: bool
        """
        self._can_add_to_content_metadata = can_add_to_content_metadata

    @property
    def can(self):
        """
        Gets the can of this Group.
        Operations the current user is able to perform on this object

        :return: The can of this Group.
        :rtype: dict(str, bool)
        """
        return self._can

    @can.setter
    def can(self, can):
        """
        Sets the can of this Group.
        Operations the current user is able to perform on this object

        :param can: The can of this Group.
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

