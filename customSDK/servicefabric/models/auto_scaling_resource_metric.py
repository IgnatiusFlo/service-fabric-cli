# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .auto_scaling_metric import AutoScalingMetric


class AutoScalingResourceMetric(AutoScalingMetric):
    """Describes the resource that is used for triggering auto scaling.

    :param kind: Constant filled by server.
    :type kind: str
    :param name: Name of the resource (like cpu or memoryInGB). Possible
     values include: 'cpu', 'memoryInGB'
    :type name: str or ~azure.servicefabric.models.enum
    """

    _validation = {
        'kind': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, name):
        super(AutoScalingResourceMetric, self).__init__()
        self.name = name
        self.kind = 'Resource'