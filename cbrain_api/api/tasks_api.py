# coding: utf-8

"""
    CBRAIN API

    API for interacting with the CBRAIN Platform  # noqa: E501

    OpenAPI spec version: 6.2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cbrain_api.api_client import ApiClient


class TasksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def tasks_get(self, **kwargs):  # noqa: E501
        """Get the list of Tasks.  # noqa: E501

        This method returns the list of Tasks accessible to the current user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tasks_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number when paginating. See also the per_page parameter
        :param int per_page: Size of each page when paginating. See also the page parameter
        :return: list[CbrainTask]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tasks_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.tasks_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def tasks_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get the list of Tasks.  # noqa: E501

        This method returns the list of Tasks accessible to the current user.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tasks_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number when paginating. See also the per_page parameter
        :param int per_page: Size of each page when paginating. See also the page parameter
        :return: list[CbrainTask]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tasks_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BrainPortalSession']  # noqa: E501

        return self.api_client.call_api(
            '/tasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CbrainTask]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tasks_id_get(self, id, **kwargs):  # noqa: E501
        """Get information on a Task.  # noqa: E501

        This method returns information on a Task, including its status, Task restartability and information on where the results are kept.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tasks_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID number of the Task to delete. (required)
        :return: CbrainTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tasks_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.tasks_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def tasks_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get information on a Task.  # noqa: E501

        This method returns information on a Task, including its status, Task restartability and information on where the results are kept.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tasks_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID number of the Task to delete. (required)
        :return: CbrainTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tasks_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `tasks_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BrainPortalSession']  # noqa: E501

        return self.api_client.call_api(
            '/tasks/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CbrainTask',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tasks_post(self, cbrain_task, **kwargs):  # noqa: E501
        """Create a new Task.  # noqa: E501

        This method allows the creation of a new Task.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tasks_post(cbrain_task, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CbrainTaskModReq cbrain_task: The task to create. (required)
        :return: list[CbrainTask]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.tasks_post_with_http_info(cbrain_task, **kwargs)  # noqa: E501
        else:
            (data) = self.tasks_post_with_http_info(cbrain_task, **kwargs)  # noqa: E501
            return data

    def tasks_post_with_http_info(self, cbrain_task, **kwargs):  # noqa: E501
        """Create a new Task.  # noqa: E501

        This method allows the creation of a new Task.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tasks_post_with_http_info(cbrain_task, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CbrainTaskModReq cbrain_task: The task to create. (required)
        :return: list[CbrainTask]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cbrain_task']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tasks_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cbrain_task' is set
        if self.api_client.client_side_validation and ('cbrain_task' not in params or
                                                       params['cbrain_task'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `cbrain_task` when calling `tasks_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cbrain_task' in params:
            body_params = params['cbrain_task']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BrainPortalSession']  # noqa: E501

        return self.api_client.call_api(
            '/tasks', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[CbrainTask]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
