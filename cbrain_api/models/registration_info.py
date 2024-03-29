# coding: utf-8

"""
    CBRAIN API

    API for interacting with the CBRAIN Platform  # noqa: E501

    OpenAPI spec version: 6.2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from cbrain_api.configuration import Configuration


class RegistrationInfo(object):
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
        'notice': 'str',
        'error': 'str',
        'newly_registered_userfiles': 'list[Userfile]',
        'previously_registered_userfiles': 'list[Userfile]',
        'userfiles_in_transit': 'list[Userfile]',
        'num_unregistered': 'int',
        'num_erased': 'int'
    }

    attribute_map = {
        'notice': 'notice',
        'error': 'error',
        'newly_registered_userfiles': 'newly_registered_userfiles',
        'previously_registered_userfiles': 'previously_registered_userfiles',
        'userfiles_in_transit': 'userfiles_in_transit',
        'num_unregistered': 'num_unregistered',
        'num_erased': 'num_erased'
    }

    def __init__(self, notice=None, error=None, newly_registered_userfiles=None, previously_registered_userfiles=None, userfiles_in_transit=None, num_unregistered=None, num_erased=None, _configuration=None):  # noqa: E501
        """RegistrationInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._notice = None
        self._error = None
        self._newly_registered_userfiles = None
        self._previously_registered_userfiles = None
        self._userfiles_in_transit = None
        self._num_unregistered = None
        self._num_erased = None
        self.discriminator = None

        if notice is not None:
            self.notice = notice
        if error is not None:
            self.error = error
        if newly_registered_userfiles is not None:
            self.newly_registered_userfiles = newly_registered_userfiles
        if previously_registered_userfiles is not None:
            self.previously_registered_userfiles = previously_registered_userfiles
        if userfiles_in_transit is not None:
            self.userfiles_in_transit = userfiles_in_transit
        if num_unregistered is not None:
            self.num_unregistered = num_unregistered
        if num_erased is not None:
            self.num_erased = num_erased

    @property
    def notice(self):
        """Gets the notice of this RegistrationInfo.  # noqa: E501


        :return: The notice of this RegistrationInfo.  # noqa: E501
        :rtype: str
        """
        return self._notice

    @notice.setter
    def notice(self, notice):
        """Sets the notice of this RegistrationInfo.


        :param notice: The notice of this RegistrationInfo.  # noqa: E501
        :type: str
        """

        self._notice = notice

    @property
    def error(self):
        """Gets the error of this RegistrationInfo.  # noqa: E501


        :return: The error of this RegistrationInfo.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this RegistrationInfo.


        :param error: The error of this RegistrationInfo.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def newly_registered_userfiles(self):
        """Gets the newly_registered_userfiles of this RegistrationInfo.  # noqa: E501


        :return: The newly_registered_userfiles of this RegistrationInfo.  # noqa: E501
        :rtype: list[Userfile]
        """
        return self._newly_registered_userfiles

    @newly_registered_userfiles.setter
    def newly_registered_userfiles(self, newly_registered_userfiles):
        """Sets the newly_registered_userfiles of this RegistrationInfo.


        :param newly_registered_userfiles: The newly_registered_userfiles of this RegistrationInfo.  # noqa: E501
        :type: list[Userfile]
        """

        self._newly_registered_userfiles = newly_registered_userfiles

    @property
    def previously_registered_userfiles(self):
        """Gets the previously_registered_userfiles of this RegistrationInfo.  # noqa: E501


        :return: The previously_registered_userfiles of this RegistrationInfo.  # noqa: E501
        :rtype: list[Userfile]
        """
        return self._previously_registered_userfiles

    @previously_registered_userfiles.setter
    def previously_registered_userfiles(self, previously_registered_userfiles):
        """Sets the previously_registered_userfiles of this RegistrationInfo.


        :param previously_registered_userfiles: The previously_registered_userfiles of this RegistrationInfo.  # noqa: E501
        :type: list[Userfile]
        """

        self._previously_registered_userfiles = previously_registered_userfiles

    @property
    def userfiles_in_transit(self):
        """Gets the userfiles_in_transit of this RegistrationInfo.  # noqa: E501


        :return: The userfiles_in_transit of this RegistrationInfo.  # noqa: E501
        :rtype: list[Userfile]
        """
        return self._userfiles_in_transit

    @userfiles_in_transit.setter
    def userfiles_in_transit(self, userfiles_in_transit):
        """Sets the userfiles_in_transit of this RegistrationInfo.


        :param userfiles_in_transit: The userfiles_in_transit of this RegistrationInfo.  # noqa: E501
        :type: list[Userfile]
        """

        self._userfiles_in_transit = userfiles_in_transit

    @property
    def num_unregistered(self):
        """Gets the num_unregistered of this RegistrationInfo.  # noqa: E501


        :return: The num_unregistered of this RegistrationInfo.  # noqa: E501
        :rtype: int
        """
        return self._num_unregistered

    @num_unregistered.setter
    def num_unregistered(self, num_unregistered):
        """Sets the num_unregistered of this RegistrationInfo.


        :param num_unregistered: The num_unregistered of this RegistrationInfo.  # noqa: E501
        :type: int
        """

        self._num_unregistered = num_unregistered

    @property
    def num_erased(self):
        """Gets the num_erased of this RegistrationInfo.  # noqa: E501


        :return: The num_erased of this RegistrationInfo.  # noqa: E501
        :rtype: int
        """
        return self._num_erased

    @num_erased.setter
    def num_erased(self, num_erased):
        """Sets the num_erased of this RegistrationInfo.


        :param num_erased: The num_erased of this RegistrationInfo.  # noqa: E501
        :type: int
        """

        self._num_erased = num_erased

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
        if issubclass(RegistrationInfo, dict):
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
        if not isinstance(other, RegistrationInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegistrationInfo):
            return True

        return self.to_dict() != other.to_dict()
