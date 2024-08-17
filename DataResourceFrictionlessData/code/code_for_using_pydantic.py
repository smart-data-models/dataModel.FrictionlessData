from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, BaseModel, EmailStr, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class License(BaseModel):
    name: Optional[str] = None
    path: Optional[str] = None
    title: Optional[str] = None


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class Source(BaseModel):
    email: Optional[EmailStr] = None
    path: Optional[str] = None
    title: Optional[str] = None


class Type6(Enum):
    DataResourceFrictionlessData = 'DataResourceFrictionlessData'


class DataResourceFrictionlessData(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    bytes: Optional[float] = Field(
        None, description='Bytes. The size of this resource in bytes'
    )
    data: Optional[List[Dict[str, Any]]] = Field(
        None, description='Data. Inline data for this resource'
    )
    description: Optional[str] = Field(
        None, description='Description. A text description. Markdown is encouraged'
    )
    encoding: Optional[str] = Field(
        None, description='Encoding. The file encoding of this resource'
    )
    format: Optional[str] = Field(
        None,
        description="Format. 'csv', 'xls', 'json' are examples of common formats. The file format of this resource",
    )
    hash: Optional[constr(pattern=r'^([^:]+:[a-fA-F0-9]+|[a-fA-F0-9]{32}|)$')] = Field(
        None,
        description='Hash. The MD5 hash of this resource. Indicate other hashing algorithms with the {algorithm}:{hash} format',
    )
    homepage: Optional[str] = Field(
        None,
        description='Home Page. The home on the web that is related to this data package',
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    licenses: Optional[List[License]] = Field(
        None,
        description='Licenses. This property is not legally binding and does not guarantee that the package is licensed under the terms defined herein. The license(s) under which the resource is published',
        min_length=1,
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    mediatype: Optional[str] = Field(
        None,
        description='Media Type. The media type of this resource. Can be any valid media type listed with [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml)',
    )
    name: Optional[str] = Field(
        None,
        description="Name. This is ideally a url-usable and human-readable name. Name 'SHOULD' be invariant, meaning it 'SHOULD NOT' change when its parent descriptor is updated. An identifier string. Lower case characters with '.', '_', '-' and '/' are allowed",
    )
    path: Optional[List[str]] = Field(
        None,
        description="Path. The dereferenced value of each referenced data source in 'path' 'MUST' be commensurate with a native, dereferenced representation of the data the resource describes. For example, in a *Tabular* Data Resource, this means that the dereferenced value of 'path' 'MUST' be an array. A reference to the data for this resource, as either a path as a string, or an array of paths as strings. of valid URIs",
        min_length=1,
    )
    profile: Optional[str] = Field(
        None,
        description="Profile. Every Package and Resource descriptor has a profile. The default profile, if none is declared, is 'data-package' for Package and 'data-resource' for Resource. The profile of this descriptor",
    )
    schema_: Optional[Dict[str, Any]] = Field(
        None, alias='schema', description='Schema. A schema for this resource'
    )
    sources: Optional[List[Source]] = Field(
        None, description='Sources. . The raw sources for this resource'
    )
    title: Optional[str] = Field(None, description='Title. A human-readable title')
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be DataResourceFrictionlessData'
    )
