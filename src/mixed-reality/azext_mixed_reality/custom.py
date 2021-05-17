# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
import json
from ._client_factory import cf_spatial_anchor_account, cf_remote_rendering_account


def spatial_anchor_account_list(cmd,
                                resource_group_name=None):
    client = cf_spatial_anchor_account(cmd.cli_ctx)
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def spatial_anchor_account_show(cmd,
                                resource_group_name,
                                account_name):
    client = cf_spatial_anchor_account(cmd.cli_ctx)
    return client.get(resource_group_name=resource_group_name,
                      account_name=account_name)


def spatial_anchor_account_create(cmd,
                                  resource_group_name,
                                  account_name,
                                  location=None,
                                  tags=None,
                                  sku=None,
                                  kind=None,
                                  storage_account_name=None):
    spatial_anchors_account = {}
    spatial_anchors_account['tags'] = tags
    spatial_anchors_account['location'] = location
    spatial_anchors_account['sku'] = sku
    spatial_anchors_account['kind'] = kind
    spatial_anchors_account['storage_account_name'] = storage_account_name
    client = cf_spatial_anchor_account(cmd.cli_ctx)
    return client.create(resource_group_name=resource_group_name,
                         account_name=account_name,
                         spatial_anchors_account=spatial_anchors_account)


def spatial_anchor_account_update(cmd,
                                  instance,
                                  location=None,
                                  tags=None,
                                  sku=None,
                                  kind=None,
                                  storage_account_name=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
        c.set_param('location', location)
        c.set_param('sku', sku)
        c.set_param('kind', kind)
        c.set_param('storage_account_name', storage_account_name)
    return instance


def spatial_anchor_account_delete(cmd,
                                  resource_group_name,
                                  account_name):
    client = cf_spatial_anchor_account(cmd.cli_ctx)
    return client.delete(resource_group_name=resource_group_name,
                         account_name=account_name)


def spatial_anchor_account_list_key(cmd,
                                    resource_group_name,
                                    account_name):
    client = cf_spatial_anchor_account(cmd.cli_ctx)
    return client.list_keys(resource_group_name=resource_group_name,
                            account_name=account_name)


def spatial_anchor_account_regenerate_key(cmd,
                                          resource_group_name,
                                          account_name,
                                          key=None):
    regenerate = {}
    regenerate['serial'] = ['primary', 'secondary'].index(key) + 1
    client = cf_spatial_anchor_account(cmd.cli_ctx)
    return client.regenerate_keys(resource_group_name=resource_group_name,
                                  account_name=account_name,
                                  regenerate=regenerate)


def remote_rendering_account_list(cmd,
                                  resource_group_name=None):
    client = cf_remote_rendering_account(cmd.cli_ctx)
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def remote_rendering_account_show(cmd,
                                  resource_group_name,
                                  account_name):
    client = cf_remote_rendering_account(cmd.cli_ctx)
    return client.get(resource_group_name=resource_group_name,
                      account_name=account_name)


def remote_rendering_account_create(cmd,
                                    resource_group_name,
                                    account_name,
                                    location=None,
                                    tags=None,
                                    sku=None,
                                    kind=None,
                                    storage_account_name=None):
    remote_rendering_account = {}
    remote_rendering_account['tags'] = tags
    remote_rendering_account['location'] = location
    remote_rendering_account['identity'] = json.loads("{\"type\": \"SystemAssigned\"}")
    remote_rendering_account['sku'] = sku
    remote_rendering_account['kind'] = kind
    remote_rendering_account['storage_account_name'] = storage_account_name
    client = cf_remote_rendering_account(cmd.cli_ctx)
    return client.create(resource_group_name=resource_group_name,
                         account_name=account_name,
                         remote_rendering_account=remote_rendering_account)


def remote_rendering_account_update(cmd,
                                    resource_group_name,
                                    account_name,
                                    location=None,
                                    tags=None,
                                    sku=None,
                                    kind=None,
                                    storage_account_name=None):
    remote_rendering_account = {}
    remote_rendering_account['tags'] = tags
    remote_rendering_account['location'] = location
    remote_rendering_account['identity'] = json.loads("{\"type\": \"SystemAssigned\"}")
    remote_rendering_account['sku'] = sku
    remote_rendering_account['kind'] = kind
    remote_rendering_account['storage_account_name'] = storage_account_name
    client = cf_remote_rendering_account(cmd.cli_ctx)
    return client.update(resource_group_name=resource_group_name,
                         account_name=account_name,
                         remote_rendering_account=remote_rendering_account)


def remote_rendering_account_delete(cmd,
                                    resource_group_name,
                                    account_name):
    client = cf_remote_rendering_account(cmd.cli_ctx)
    return client.delete(resource_group_name=resource_group_name,
                         account_name=account_name)


def remote_rendering_account_list_key(cmd,
                                      resource_group_name,
                                      account_name):
    client = cf_remote_rendering_account(cmd.cli_ctx)
    return client.list_keys(resource_group_name=resource_group_name,
                            account_name=account_name)


def remote_rendering_account_regenerate_key(cmd,
                                            resource_group_name,
                                            account_name,
                                            key=None):
    regenerate = {}
    regenerate['serial'] = ['primary', 'secondary'].index(key) + 1
    client = cf_remote_rendering_account(cmd.cli_ctx)
    return client.regenerate_keys(resource_group_name=resource_group_name,
                                  account_name=account_name,
                                  regenerate=regenerate)
