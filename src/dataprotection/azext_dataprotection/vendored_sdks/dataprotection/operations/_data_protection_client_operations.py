# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6370, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class DataProtectionClientOperationsMixin(object):

    def get_operation_status(
        self,
        location,  # type: str
        operation_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.OperationResource"
        """Gets the operation status for a resource.

        Gets the operation status for a resource.

        :param location:
        :type location: str
        :param operation_id:
        :type operation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: OperationResource, or the result of cls(response)
        :rtype: ~data_protection_client.models.OperationResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.OperationResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"
        accept = "application/json"

        # Construct URL
        url = self.get_operation_status.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'location': self._serialize.url("location", location, 'str'),
            'operationId': self._serialize.url("operation_id", operation_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('OperationResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_operation_status.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DataProtection/locations/{location}/operationStatus/{operationId}'}  # type: ignore

    def get_operation_result_patch(
        self,
        vault_name,  # type: str
        resource_group_name,  # type: str
        operation_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.BackupVaultResource"
        """get_operation_result_patch.

        :param vault_name: The name of the backup vault.
        :type vault_name: str
        :param resource_group_name: The name of the resource group where the backup vault is present.
        :type resource_group_name: str
        :param operation_id:
        :type operation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BackupVaultResource, or the result of cls(response)
        :rtype: ~data_protection_client.models.BackupVaultResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.BackupVaultResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"
        accept = "application/json"

        # Construct URL
        url = self.get_operation_result_patch.metadata['url']  # type: ignore
        path_format_arguments = {
            'vaultName': self._serialize.url("vault_name", vault_name, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'operationId': self._serialize.url("operation_id", operation_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('BackupVaultResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_operation_result_patch.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataProtection/backupVaults/{vaultName}/operationResults/{operationId}'}  # type: ignore

    def check_feature_support(
        self,
        location,  # type: str
        parameters,  # type: "models.FeatureValidationRequestBase"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.FeatureValidationResponseBase"
        """Validates if a feature is supported.

        Validates if a feature is supported.

        :param location:
        :type location: str
        :param parameters: Feature support request object.
        :type parameters: ~data_protection_client.models.FeatureValidationRequestBase
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: FeatureValidationResponseBase, or the result of cls(response)
        :rtype: ~data_protection_client.models.FeatureValidationResponseBase
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.FeatureValidationResponseBase"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.check_feature_support.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'location': self._serialize.url("location", location, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'FeatureValidationRequestBase')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('FeatureValidationResponseBase', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    check_feature_support.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.DataProtection/locations/{location}/checkFeatureSupport'}  # type: ignore