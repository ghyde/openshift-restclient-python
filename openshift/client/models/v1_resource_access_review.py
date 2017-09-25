# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'metav1.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1ResourceAccessReview(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_version=None, content=None, is_non_resource_url=None, kind=None, namespace=None, path=None, resource=None, resource_api_group=None, resource_api_version=None, resource_name=None, verb=None):
        """
        V1ResourceAccessReview - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_version': 'str',
            'content': 'RuntimeRawExtension',
            'is_non_resource_url': 'bool',
            'kind': 'str',
            'namespace': 'str',
            'path': 'str',
            'resource': 'str',
            'resource_api_group': 'str',
            'resource_api_version': 'str',
            'resource_name': 'str',
            'verb': 'str'
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'content': 'content',
            'is_non_resource_url': 'isNonResourceURL',
            'kind': 'kind',
            'namespace': 'namespace',
            'path': 'path',
            'resource': 'resource',
            'resource_api_group': 'resourceAPIGroup',
            'resource_api_version': 'resourceAPIVersion',
            'resource_name': 'resourceName',
            'verb': 'verb'
        }

        self._api_version = api_version
        self._content = content
        self._is_non_resource_url = is_non_resource_url
        self._kind = kind
        self._namespace = namespace
        self._path = path
        self._resource = resource
        self._resource_api_group = resource_api_group
        self._resource_api_version = resource_api_version
        self._resource_name = resource_name
        self._verb = verb

    @property
    def api_version(self):
        """
        Gets the api_version of this V1ResourceAccessReview.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :return: The api_version of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1ResourceAccessReview.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1ResourceAccessReview.
        :type: str
        """

        self._api_version = api_version

    @property
    def content(self):
        """
        Gets the content of this V1ResourceAccessReview.
        Content is the actual content of the request for create and update

        :return: The content of this V1ResourceAccessReview.
        :rtype: RuntimeRawExtension
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this V1ResourceAccessReview.
        Content is the actual content of the request for create and update

        :param content: The content of this V1ResourceAccessReview.
        :type: RuntimeRawExtension
        """

        self._content = content

    @property
    def is_non_resource_url(self):
        """
        Gets the is_non_resource_url of this V1ResourceAccessReview.
        IsNonResourceURL is true if this is a request for a non-resource URL (outside of the resource hieraarchy)

        :return: The is_non_resource_url of this V1ResourceAccessReview.
        :rtype: bool
        """
        return self._is_non_resource_url

    @is_non_resource_url.setter
    def is_non_resource_url(self, is_non_resource_url):
        """
        Sets the is_non_resource_url of this V1ResourceAccessReview.
        IsNonResourceURL is true if this is a request for a non-resource URL (outside of the resource hieraarchy)

        :param is_non_resource_url: The is_non_resource_url of this V1ResourceAccessReview.
        :type: bool
        """
        if is_non_resource_url is None:
            raise ValueError("Invalid value for `is_non_resource_url`, must not be `None`")

        self._is_non_resource_url = is_non_resource_url

    @property
    def kind(self):
        """
        Gets the kind of this V1ResourceAccessReview.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :return: The kind of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1ResourceAccessReview.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1ResourceAccessReview.
        :type: str
        """

        self._kind = kind

    @property
    def namespace(self):
        """
        Gets the namespace of this V1ResourceAccessReview.
        Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces

        :return: The namespace of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this V1ResourceAccessReview.
        Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces

        :param namespace: The namespace of this V1ResourceAccessReview.
        :type: str
        """
        if namespace is None:
            raise ValueError("Invalid value for `namespace`, must not be `None`")

        self._namespace = namespace

    @property
    def path(self):
        """
        Gets the path of this V1ResourceAccessReview.
        Path is the path of a non resource URL

        :return: The path of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this V1ResourceAccessReview.
        Path is the path of a non resource URL

        :param path: The path of this V1ResourceAccessReview.
        :type: str
        """
        if path is None:
            raise ValueError("Invalid value for `path`, must not be `None`")

        self._path = path

    @property
    def resource(self):
        """
        Gets the resource of this V1ResourceAccessReview.
        Resource is one of the existing resource types

        :return: The resource of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this V1ResourceAccessReview.
        Resource is one of the existing resource types

        :param resource: The resource of this V1ResourceAccessReview.
        :type: str
        """
        if resource is None:
            raise ValueError("Invalid value for `resource`, must not be `None`")

        self._resource = resource

    @property
    def resource_api_group(self):
        """
        Gets the resource_api_group of this V1ResourceAccessReview.
        Group is the API group of the resource Serialized as resourceAPIGroup to avoid confusion with the 'groups' field when inlined

        :return: The resource_api_group of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._resource_api_group

    @resource_api_group.setter
    def resource_api_group(self, resource_api_group):
        """
        Sets the resource_api_group of this V1ResourceAccessReview.
        Group is the API group of the resource Serialized as resourceAPIGroup to avoid confusion with the 'groups' field when inlined

        :param resource_api_group: The resource_api_group of this V1ResourceAccessReview.
        :type: str
        """
        if resource_api_group is None:
            raise ValueError("Invalid value for `resource_api_group`, must not be `None`")

        self._resource_api_group = resource_api_group

    @property
    def resource_api_version(self):
        """
        Gets the resource_api_version of this V1ResourceAccessReview.
        Version is the API version of the resource Serialized as resourceAPIVersion to avoid confusion with TypeMeta.apiVersion and ObjectMeta.resourceVersion when inlined

        :return: The resource_api_version of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._resource_api_version

    @resource_api_version.setter
    def resource_api_version(self, resource_api_version):
        """
        Sets the resource_api_version of this V1ResourceAccessReview.
        Version is the API version of the resource Serialized as resourceAPIVersion to avoid confusion with TypeMeta.apiVersion and ObjectMeta.resourceVersion when inlined

        :param resource_api_version: The resource_api_version of this V1ResourceAccessReview.
        :type: str
        """
        if resource_api_version is None:
            raise ValueError("Invalid value for `resource_api_version`, must not be `None`")

        self._resource_api_version = resource_api_version

    @property
    def resource_name(self):
        """
        Gets the resource_name of this V1ResourceAccessReview.
        ResourceName is the name of the resource being requested for a \"get\" or deleted for a \"delete\"

        :return: The resource_name of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """
        Sets the resource_name of this V1ResourceAccessReview.
        ResourceName is the name of the resource being requested for a \"get\" or deleted for a \"delete\"

        :param resource_name: The resource_name of this V1ResourceAccessReview.
        :type: str
        """
        if resource_name is None:
            raise ValueError("Invalid value for `resource_name`, must not be `None`")

        self._resource_name = resource_name

    @property
    def verb(self):
        """
        Gets the verb of this V1ResourceAccessReview.
        Verb is one of: get, list, watch, create, update, delete

        :return: The verb of this V1ResourceAccessReview.
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        """
        Sets the verb of this V1ResourceAccessReview.
        Verb is one of: get, list, watch, create, update, delete

        :param verb: The verb of this V1ResourceAccessReview.
        :type: str
        """
        if verb is None:
            raise ValueError("Invalid value for `verb`, must not be `None`")

        self._verb = verb

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
        if not isinstance(other, V1ResourceAccessReview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
