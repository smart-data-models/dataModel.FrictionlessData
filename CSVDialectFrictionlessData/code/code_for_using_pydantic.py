from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, constr


class Type(Enum):
    CSVDialectFrictionlessData = 'CSVDialectFrictionlessData'


class CSVDialectFrictionlessData(BaseModel):
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    caseSensitiveHeader: Optional[bool] = Field(
        None,
        description="Case Sensitive Header. Use of case in source CSV files is not always an intentional decision. For example, should 'CAT' and 'Cat' be considered to have the same meaning. Specifies if the case of headers is meaningful",
    )
    commentChar: Optional[str] = Field(
        None,
        description='Comment Character. Specifies that any row beginning with this one-character string, without preceding whitespace, causes the entire line to be ignored',
    )
    csvddfVersion: Optional[float] = Field(
        None,
        description='CSV Dialect schema version. A number to indicate the schema version of CSV Dialect. Version 1.0 was named CSV Dialect Description Format and used different field names',
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
    delimiter: Optional[str] = Field(
        None,
        description='Delimiter. A character sequence to use as the field separator',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    doubleQuote: Optional[bool] = Field(
        None,
        description='Double Quote. If Double Quote is set to true, two consecutive quotes must be interpreted as one. Specifies the handling of quotes inside fields',
    )
    escapeChar: Optional[str] = Field(
        None,
        description='Escape Character. Specifies a one-character string to use as the escape character',
    )
    header: Optional[bool] = Field(
        None,
        description='Header. Specifies if the file includes a header row, always as the first row in the file',
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
    lineTerminator: Optional[str] = Field(
        None,
        description='Line Terminator. Specifies the character sequence that must be used to terminate rows',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    nullSequence: Optional[str] = Field(
        None,
        description="Null Sequence. Specifies the null sequence, for example, \\ and then 'N'",
    )
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
    quoteChar: Optional[str] = Field(
        None,
        description='Quote Character. Specifies a one-character string to use as the quoting character',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    skipInitialSpace: Optional[bool] = Field(
        None,
        description='Skip Initial Space. Specifies the interpretation of whitespace immediately following a delimiter. If false, whitespace immediately after a delimiter should be treated as part of the subsequent field',
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type] = Field(
        None, description='It has to be CSVDialectFrictionlessData. NGSI entity type'
    )
