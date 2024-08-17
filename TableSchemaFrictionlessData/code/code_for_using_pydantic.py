from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, constr


class TableSchemaFrictionlessData(BaseModel):
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    fields: Optional[List[Dict[str, Any]]] = Field(
        None, description='An array of Table Schema Field objects'
    )
    foreignKeys: Optional[List[str]] = Field(None, description='')
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
    missingValues: Optional[List[str]] = Field(
        None,
        description="Many datasets arrive with missing data values, either because a value was not collected or it never existed. Missing values may be indicated simply by the value being empty in other cases a special value may have been used e.g. '-', 'NaN', '0', '-9999' etc.The 'missingValues' property provides a way to indicate that these values should be interpreted as equivalent to null. The 'missingValues' are strings rather than being the data type of the particular field. This allows for comparison prior to casting and for fields to have missing value which are not of their type, for example a 'number' field to have missing values indicated by '-'.The default value of 'missingValue' for a non-string type field is the empty string ''. For string type fields there is no default for 'missingValue' (for string fields the empty string '' is a valid value and need not indicate null). Values that when encountered in the source, should be considered as 'null', 'not present', or 'blank' values",
    )
    name: Optional[str] = Field(None, description='The name of this item')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    primaryKey: Optional[List[str]] = Field(
        None,
        description="Field name in the primaryKey 'MUST' be unique, and 'MUST' match a field name in the associated table. It is acceptable to have an array with a single value, indicating that the value of a single field is the primary key. A primary key is a field name or an array of field names, whose values 'MUST' uniquely identify each row in the table",
        min_length=1,
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[str] = Field(
        None, description='it has to be TableSchemaFrictionlessData. NGSI entity type'
    )
