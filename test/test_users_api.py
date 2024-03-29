# coding: utf-8

"""
    CBRAIN API

    API for interacting with the CBRAIN Platform  # noqa: E501

    OpenAPI spec version: 6.2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cbrain_api
from cbrain_api.api.users_api import UsersApi  # noqa: E501
from cbrain_api.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = cbrain_api.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_users_get(self):
        """Test case for users_get

        Returns all of the users in CBRAIN. Only available to admins.  # noqa: E501
        """
        pass

    def test_users_id_delete(self):
        """Test case for users_id_delete

        Deletes a CBRAIN user  # noqa: E501
        """
        pass

    def test_users_id_get(self):
        """Test case for users_id_get

        Returns information about a user  # noqa: E501
        """
        pass

    def test_users_id_patch(self):
        """Test case for users_id_patch

        Update information about a user  # noqa: E501
        """
        pass

    def test_users_post(self):
        """Test case for users_post

        Create a new user in CBRAIN. Only available to admins.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
