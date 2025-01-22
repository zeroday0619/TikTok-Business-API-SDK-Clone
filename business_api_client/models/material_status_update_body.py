# coding: utf-8

"""
 Copyright 2023 TikTok Pte. Ltd.

 This source code is licensed under the MIT license found in
 the LICENSE file in the root directory of this source tree.
"""
import pprint
import re  # noqa: F401

import six

class MaterialStatusUpdateBody(object):
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
        'ad_group_id': 'str',
        'advertiser_id': 'str',
        'material_ids': 'list[str]',
        'material_status': 'str'
    }

    attribute_map = {
        'ad_group_id': 'ad_group_id',
        'advertiser_id': 'advertiser_id',
        'material_ids': 'material_ids',
        'material_status': 'material_status'
    }

    def __init__(self, ad_group_id=None, advertiser_id=None, material_ids=None, material_status=None):  # noqa: E501
        """MaterialStatusUpdateBody - a model defined in Swagger"""  # noqa: E501
        self._ad_group_id = None
        self._advertiser_id = None
        self._material_ids = None
        self._material_status = None
        self.discriminator = None
        self.ad_group_id = ad_group_id
        self.advertiser_id = advertiser_id
        self.material_ids = material_ids
        self.material_status = material_status

    @property
    def ad_group_id(self):
        """Gets the ad_group_id of this MaterialStatusUpdateBody.  # noqa: E501

        Adgroup ID  # noqa: E501

        :return: The ad_group_id of this MaterialStatusUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._ad_group_id

    @ad_group_id.setter
    def ad_group_id(self, ad_group_id):
        """Sets the ad_group_id of this MaterialStatusUpdateBody.

        Adgroup ID  # noqa: E501

        :param ad_group_id: The ad_group_id of this MaterialStatusUpdateBody.  # noqa: E501
        :type: str
        """
        if ad_group_id is None:
            raise ValueError("Invalid value for `ad_group_id`, must not be `None`")  # noqa: E501

        self._ad_group_id = ad_group_id

    @property
    def advertiser_id(self):
        """Gets the advertiser_id of this MaterialStatusUpdateBody.  # noqa: E501

        Advertiser ID  # noqa: E501

        :return: The advertiser_id of this MaterialStatusUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._advertiser_id

    @advertiser_id.setter
    def advertiser_id(self, advertiser_id):
        """Sets the advertiser_id of this MaterialStatusUpdateBody.

        Advertiser ID  # noqa: E501

        :param advertiser_id: The advertiser_id of this MaterialStatusUpdateBody.  # noqa: E501
        :type: str
        """
        if advertiser_id is None:
            raise ValueError("Invalid value for `advertiser_id`, must not be `None`")  # noqa: E501

        self._advertiser_id = advertiser_id

    @property
    def material_ids(self):
        """Gets the material_ids of this MaterialStatusUpdateBody.  # noqa: E501

        Material ID  # noqa: E501

        :return: The material_ids of this MaterialStatusUpdateBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._material_ids

    @material_ids.setter
    def material_ids(self, material_ids):
        """Sets the material_ids of this MaterialStatusUpdateBody.

        Material ID  # noqa: E501

        :param material_ids: The material_ids of this MaterialStatusUpdateBody.  # noqa: E501
        :type: list[str]
        """
        if material_ids is None:
            raise ValueError("Invalid value for `material_ids`, must not be `None`")  # noqa: E501

        self._material_ids = material_ids

    @property
    def material_status(self):
        """Gets the material_status of this MaterialStatusUpdateBody.  # noqa: E501

        Material status  # noqa: E501

        :return: The material_status of this MaterialStatusUpdateBody.  # noqa: E501
        :rtype: str
        """
        return self._material_status

    @material_status.setter
    def material_status(self, material_status):
        """Sets the material_status of this MaterialStatusUpdateBody.

        Material status  # noqa: E501

        :param material_status: The material_status of this MaterialStatusUpdateBody.  # noqa: E501
        :type: str
        """
        if material_status is None:
            raise ValueError("Invalid value for `material_status`, must not be `None`")  # noqa: E501

        self._material_status = material_status

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
        if issubclass(MaterialStatusUpdateBody, dict):
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
        if not isinstance(other, MaterialStatusUpdateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
