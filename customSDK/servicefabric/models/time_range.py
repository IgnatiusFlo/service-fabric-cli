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

from msrest.serialization import Model


class TimeRange(Model):
    """Defines a time range in a 24 hour day specified by a start and end time.

    :param start_time: Defines an hour and minute of the day specified in 24
     hour time.
    :type start_time: ~azure.servicefabric.models.TimeOfDay
    :param end_time: Defines an hour and minute of the day specified in 24
     hour time.
    :type end_time: ~azure.servicefabric.models.TimeOfDay
    """

    _attribute_map = {
        'start_time': {'key': 'StartTime', 'type': 'TimeOfDay'},
        'end_time': {'key': 'EndTime', 'type': 'TimeOfDay'},
    }

    def __init__(self, start_time=None, end_time=None):
        super(TimeRange, self).__init__()
        self.start_time = start_time
        self.end_time = end_time
