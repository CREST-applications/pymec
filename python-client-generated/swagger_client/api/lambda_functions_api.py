# coding: utf-8

"""
    MEC-RM API

    This is the MEC Recource Manager API specification.  Current Version: v0.5.0.2 (Major: 0.5, Minor: 0, Patch: 2)  As a general-purpose stateless middleware, we have designed this system with a high level of flexibility. There is no predefined API invocation flow in this system. Application developers have the freedom to creatively develop different invocation flows based on their specific needs. In fact, this application-centric flexible development is what we advocate and one of the main driving forces behind our transition from RPC-based APIs to stateless APIs.  The document covers not-fixed fields which may not compatable between versions. (espesilly version change greater than minor version)  For implement of non-published APIs, you can reference the source code by your own responsibility.  ## Documents: * [API Document](https://mecdoc.dolylab.cc/)  # noqa: E501

    OpenAPI spec version: v0.5.0.2
    Contact: nb22509@shibaura-it.ac.jp
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class LambdaFunctionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def pleiades_lambda_create(self, **kwargs):  # noqa: E501
        """Create an anonymous function  # noqa: E501

        Create an anonymous function object.   This endpoint will allocate a globally unique identifier. The identifier given by this endpoint will be called `fID` in this system which stands for \"anonymouns **f**unction **ID**\"  This method requests for an exist BLOB data object as the function literal (which shows as `code_id` field).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pleiades_lambda_create(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestFunctionCreate body:
        :return: ResponseFunctionCreate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pleiades_lambda_create_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.pleiades_lambda_create_with_http_info(**kwargs)  # noqa: E501
            return data

    def pleiades_lambda_create_with_http_info(self, **kwargs):  # noqa: E501
        """Create an anonymous function  # noqa: E501

        Create an anonymous function object.   This endpoint will allocate a globally unique identifier. The identifier given by this endpoint will be called `fID` in this system which stands for \"anonymouns **f**unction **ID**\"  This method requests for an exist BLOB data object as the function literal (which shows as `code_id` field).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pleiades_lambda_create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestFunctionCreate body:
        :return: ResponseFunctionCreate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pleiades_lambda_create" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/lambda', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseFunctionCreate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def pleiades_lambda_info(self, f_id, **kwargs):  # noqa: E501
        """Get anymous function object metadata  # noqa: E501

        Get anonymous function object metadata.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pleiades_lambda_info(f_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str f_id: Function ID.  This field must be a valid functione object ID. (required)
        :return: ResponseFunctionInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pleiades_lambda_info_with_http_info(f_id, **kwargs)  # noqa: E501
        else:
            (data) = self.pleiades_lambda_info_with_http_info(f_id, **kwargs)  # noqa: E501
            return data

    def pleiades_lambda_info_with_http_info(self, f_id, **kwargs):  # noqa: E501
        """Get anymous function object metadata  # noqa: E501

        Get anonymous function object metadata.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pleiades_lambda_info_with_http_info(f_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str f_id: Function ID.  This field must be a valid functione object ID. (required)
        :return: ResponseFunctionInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['f_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pleiades_lambda_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'f_id' is set
        if ('f_id' not in params or
                params['f_id'] is None):
            raise ValueError("Missing the required parameter `f_id` when calling `pleiades_lambda_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'f_id' in params:
            path_params['fID'] = params['f_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/lambda/{fID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseFunctionInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
