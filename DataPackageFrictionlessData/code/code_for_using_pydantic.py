from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field, constr


class License(BaseModel):
    model_config = ConfigDict(
        regex_engine="python-re",
    )
    name: Optional[constr(pattern=r'^([-a-zA-Z0-9._])+$')] = Field(
        None,
        description='MUST be an Open Definition license identifier, see http://licenses.opendefinition.org/',
    )
    path: Optional[constr(pattern=r'^(?=^[^./~])(^((?!\\.{2}).)*$).*$')] = Field(
        None, description='A fully qualified URL, or a POSIX file path'
    )
    title: Optional[str] = Field(None, description='A human-readable title')


class Resource(BaseModel):
    model_config = ConfigDict(
        regex_engine="python-re",
    )
    name: Optional[constr(pattern=r'^([-a-zA-Z0-9._])+$')] = Field(
        None,
        description='MUST be an Open Definition license identifier, see http://licenses.opendefinition.org/',
    )
    path: Optional[constr(pattern=r'^(?=^[^./~])(^((?!\\.{2}).)*$).*$')] = Field(
        None, description='A fully qualified URL, or a POSIX file path'
    )
    profile: Optional[str] = Field(None, description='The profile of this descriptor.')


class Source(BaseModel):
    model_config = ConfigDict(
        regex_engine="python-re",
    )
    email: Optional[EmailStr] = Field(None, description='An email address')
    path: Optional[constr(pattern=r'^(?=^[^./~])(^((?!\\.{2}).)*$).*$')] = Field(
        None, description='A fully qualified URL, or a POSIX file path'
    )
    title: str = Field(..., description='A human-readable title')


class Type(Enum):
    DataPackageFrictionlessData = 'DataPackageFrictionlessData'


class DataPackageFrictionlessData(BaseModel):
    contributors: Optional[List[str]] = Field(
        None, description='Contributors. The contributors to this descriptor'
    )
    created: Optional[str] = Field(
        None,
        description='Created. The datetime must conform to the string formats for datetime as described in [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6). The datetime on which this descriptor was created',
    )
    description: Optional[str] = Field(
        None, description='Description. . A text description. Markdown is encouraged'
    )
    homepage: Optional[str] = Field(
        None,
        description='Home Page. . The home on the web that is related to this data package',
    )
    id: Optional[str] = Field(
        None,
        description='ID. A common usage pattern for Data Packages is as a packaging format within the bounds of a system or platform. In these cases, a unique identifier for a package is desired for common data handling workflows, such as updating an existing package. While at the level of the specification, global uniqueness cannot be validated, consumers using the `id` property `MUST` ensure identifiers are globally unique. A property reserved for globally unique identifiers. Examples of identifiers that are unique include UUIDs and DOIs',
    )
    image: Optional[str] = Field(
        None, description='Image. A image to represent this package'
    )
    keywords: Optional[List[str]] = Field(
        None, description='Keywords. . A list of keywords that describe this package'
    )
    licenses: Optional[List[License]] = Field(
        None,
        description='Licenses. This property is not legally binding and does not guarantee that the package is licensed under the terms defined herein. The license(s) under which this package is published',
    )
    name: Optional[str] = Field(
        None,
        description='Name. This is ideally a url-usable and human-readable name. Name `SHOULD` be invariant, meaning it `SHOULD NOT` change when its parent descriptor is updated. An identifier string. Lower case characters with `.`, `_`, `-` and `/` are allowed',
    )
    profile: Optional[str] = Field(
        None,
        description='Profile. Every Package and Resource descriptor has a profile. The default profile, if none is declared, is `data-package` for Package and `data-resource` for Resource. The profile of this descriptor',
    )
    resources: Optional[List[Resource]] = Field(
        None,
        description='Data Resources. An `array` of Data Resource objects, each compliant with the [Data Resource](/data-resource/) specification',
        min_length=1,
    )
    sources: Optional[List[Source]] = Field(
        None, description='Sources. The raw sources for this resource'
    )
    title: Optional[str] = Field(None, description='Title. . A human-readable title')
    type: Optional[Type] = Field(
        None, description='It has to be DataPackageFrictionlessData. NGSI entity type'
    )
