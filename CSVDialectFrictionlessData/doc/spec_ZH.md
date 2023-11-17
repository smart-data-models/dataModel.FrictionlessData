<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体CSVDialectFrictionlessData    
============================<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/CSVDialectFrictionlessData/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**从原始无摩擦数据转换而来，用于智能数据模型计划**。    
版本： 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `alternateName[string]`: 该项目的替代名称  - `caseSensitiveHeader[boolean]`: 大小写敏感的标题。在 CSV 源文件中使用大小写并非总是有意为之。例如，"CAT "和 "Cat "的含义是否相同。指定标题的大小写是否有意义  - `commentChar[string]`: 注释字符。指定以该单字符字符串开头的任何行，如果前面没有空白，整行将被忽略  - `csvddfVersion[number]`: CSV Dialect 模式版本。表示 CSV Dialect 模式版本的数字。1.0 版被命名为 CSV 方言描述格式，并使用不同的字段名称  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `delimiter[string]`: 分隔符。用作字段分隔符的字符序列  - `description[string]`: 项目描述  - `doubleQuote[boolean]`: 双引号。如果双引号设置为 "true"，则两个连续引号必须解释为一个引号。指定字段内引号的处理方式  - `escapeChar[string]`: 转义字符。指定一个字符串作为转义字符  - `header[boolean]`: 标题。指定文件是否包含标题行，总是作为文件的第一行  - `id[*]`: 实体的唯一标识符  - `lineTerminator[string]`: 行结束符。指定终止行时必须使用的字符序列  - `name[string]`: 该项目的名称  - `nullSequence[string]`: 空序列。指定空序列，例如：\，然后是'N'。  - `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `quoteChar[string]`: 引号字符。指定一个字符串作为引号字符  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `skipInitialSpace[boolean]`: 跳过初始空格。指定对分隔符后空白的解释。如果为假，则分隔符后的空白应被视为后续字段的一部分  - `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `type[string]`: 必须是 CSVDialectFrictionlessData。NGSI 实体类型  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `delimiter`  - `doubleQuote`  - `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
该数据模型来自原始的无摩擦数据，可在 https://frictionlessdata.io/ 上找到。其中有几处小改动。1）id 和类型为必填项 2）json 模式的结构已调整为智能数据模型的官方格式。参见贡献手册 [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual)。3) 出于兼容性考虑，增加了一些属性    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
CSVDialectFrictionlessData:      
  description: The CSV dialect descriptor.Converted for Smart Data Models initiative from original frictionless data      
  properties:      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    caseSensitiveHeader:      
      description: 'Case Sensitive Header. Use of case in source CSV files is not always an intentional decision. For example, should ''CAT'' and ''Cat'' be considered to have the same meaning. Specifies if the case of headers is meaningful'      
      type: boolean      
      x-ngsi:      
        type: Property      
    commentChar:      
      description: 'Comment Character. Specifies that any row beginning with this one-character string, without preceding whitespace, causes the entire line to be ignored'      
      type: string      
      x-ngsi:      
        type: Property      
    csvddfVersion:      
      description: CSV Dialect schema version. A number to indicate the schema version of CSV Dialect. Version 1.0 was named CSV Dialect Description Format and used different field names      
      type: number      
      x-ngsi:      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    delimiter:      
      description: Delimiter. A character sequence to use as the field separator      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    doubleQuote:      
      description: 'Double Quote. If Double Quote is set to true, two consecutive quotes must be interpreted as one. Specifies the handling of quotes inside fields'      
      type: boolean      
      x-ngsi:      
        type: Property      
    escapeChar:      
      description: Escape Character. Specifies a one-character string to use as the escape character      
      type: string      
      x-ngsi:      
        type: Property      
    header:      
      description: 'Header. Specifies if the file includes a header row, always as the first row in the file'      
      type: boolean      
      x-ngsi:      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    lineTerminator:      
      description: Line Terminator. Specifies the character sequence that must be used to terminate rows      
      type: string      
      x-ngsi:      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    nullSequence:      
      description: 'Null Sequence. Specifies the null sequence, for example, \ and then ''N'''      
      type: string      
      x-ngsi:      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    quoteChar:      
      description: Quote Character. Specifies a one-character string to use as the quoting character      
      type: string      
      x-ngsi:      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
      oneOf:      
        - items:      
            format: uri      
            type: string      
          minItems: 1      
          type: array      
        - format: uri      
          type: string      
      x-ngsi:      
        type: Property      
    skipInitialSpace:      
      description: 'Skip Initial Space. Specifies the interpretation of whitespace immediately following a delimiter. If false, whitespace immediately after a delimiter should be treated as part of the subsequent field'      
      type: boolean      
      x-ngsi:      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: It has to be CSVDialectFrictionlessData. NGSI entity type      
      enum:      
        - CSVDialectFrictionlessData      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - delimiter      
    - doubleQuote      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.FrictionlessData/blob/master/CSVDialectFrictionlessData/LICENSE.md      
  x-model-schema: ""      
  x-model-tags: SDG      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### CSVDialectFrictionlessData NGSI-v2 密钥值示例    
下面是以 JSON-LD 格式作为键值的 CSVDialectFrictionlessData 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CSVDialect:id:OAPS:03889914",  
  "type": "CSVDialectFrictionlessData",  
  "alternateName": "",  
  "caseSensitiveHeader": true,  
  "commentChar": "#",  
  "csvddfVersion": 1.2,  
  "dataProvider": "",  
  "dateCreated": "1986-03-01T17:11:28Z",  
  "dateModified": "2017-04-29T03:29:41Z",  
  "delimiter": "",  
  "description": "",  
  "doubleQuote": true,  
  "escapeChar": "\",  
  "header": false,  
  "name": "",  
  "owner": [  
    "urn:ngsi-ld:CSVDialect:items:YPBX:70706198",  
    "urn:ngsi-ld:CSVDialect:items:MABG:25535507"  
  ],  
  "quoteChar": "'",  
  "seeAlso": [  
    "urn:ngsi-ld:CSVDialect:items:YNLD:15120048",  
    "urn:ngsi-ld:CSVDialect:items:EFIZ:80683325"  
  ],  
  "skipInitialSpace": false,  
  "source": ""  
}  
```  
</details>    
#### CSVDialectFrictionlessData NGSI-v2 标准化示例    
下面是一个 CSVDialectFrictionlessData 的示例，采用 JSON-LD 格式规范化。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CSVDialect:id:OAPS:03889914",  
  "type": "CSVDialectFrictionlessData",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1986-03-01T17:11:28Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-04-29T03:29:41Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": ""  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": ""  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": ""  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:CSVDialect:items:YPBX:70706198",  
      "urn:ngsi-ld:CSVDialect:items:MABG:25535507"  
    ]  
  },  
  "seeAlso": {  
    "type": "StructuredValue",  
    "value": [  
      "urn:ngsi-ld:CSVDialect:items:YNLD:15120048",  
      "urn:ngsi-ld:CSVDialect:items:EFIZ:80683325"  
    ]  
  },  
  "csvddfVersion": {  
    "type": "Number",  
    "value": 1.2  
  },  
  "delimiter": {  
    "type": "Text",  
    "value": "%3B"  
  },  
  "doubleQuote": {  
    "type": "Boolean",  
    "value": true  
  },  
  "lineTerminator": {  
    "type": "Text",  
    "value": "\r\n"  
  },  
  "nullSequence": {  
    "type": "Text",  
    "value": "\N"  
  },  
  "quoteChar": {  
    "type": "Text",  
    "value": "'"  
  },  
  "escapeChar": {  
    "type": "Text",  
    "value": "\\"  
  },  
  "skipInitialSpace": {  
    "type": "Boolean",  
    "value": false  
  },  
  "header": {  
    "type": "Boolean",  
    "value": false  
  },  
  "commentChar": {  
    "type": "Text",  
    "value": "#"  
  },  
  "caseSensitiveHeader": {  
    "type": "Boolean",  
    "value": true  
  }  
}  
```  
</details>    
#### CSVDialectFrictionlessData NGSI-LD 键值 示例    
下面是以 JSON-LD 格式作为键值的 CSVDialectFrictionlessData 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CSVDialect:id:OAPS:03889914",  
  "type": "CSVDialectFrictionlessData",  
  "alternateName": "",  
  "caseSensitiveHeader": true,  
  "commentChar": "#",  
  "csvddfVersion": 1.2,  
  "dataProvider": "",  
  "dateCreated": "1986-03-01T17:11:28Z",  
  "dateModified": "2017-04-29T03:29:41Z",  
  "delimiter": "%3B",  
  "description": "",  
  "doubleQuote": true,  
  "escapeChar": "\",  
  "header": false,  
  "name": "",  
  "owner": [  
    "urn:ngsi-ld:CSVDialect:items:YPBX:70706198",  
    "urn:ngsi-ld:CSVDialect:items:MABG:25535507"  
  ],  
  "quoteChar": "'",  
  "seeAlso": [  
    "urn:ngsi-ld:CSVDialect:items:YNLD:15120048",  
    "urn:ngsi-ld:CSVDialect:items:EFIZ:80683325"  
  ],  
  "skipInitialSpace": false,  
  "source": "",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.FrictionlessData/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### CSVDialectFrictionlessData NGSI-LD 归一化示例    
下面是一个 CSVDialectFrictionlessData 的示例，采用 JSON-LD 格式并已规范化。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:CSVDialect:id:OAPS:03889914",  
    "type": "CSVDialectFrictionlessData",  
    "dateCreated": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "1986-03-01T17:11:28Z"  
        }  
    },  
    "dateModified": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2017-04-29T03:29:41Z"  
        }  
    },  
    "source": {  
        "type": "Property",  
        "value": ""  
    },  
    "name": {  
        "type": "Property",  
        "value": ""  
    },  
    "alternateName": {  
        "type": "Property",  
        "value": ""  
    },  
    "description": {  
        "type": "Property",  
        "value": ""  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": ""  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:CSVDialect:items:YPBX:70706198",  
            "urn:ngsi-ld:CSVDialect:items:MABG:25535507"  
        ]  
    },  
    "seeAlso": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:CSVDialect:items:YNLD:15120048",  
            "urn:ngsi-ld:CSVDialect:items:EFIZ:80683325"  
        ]  
    },  
    "csvddfVersion": {  
        "type": "Property",  
        "value": 1.2  
    },  
    "delimiter": {  
        "type": "Property",  
        "value": "%3B"  
    },  
    "doubleQuote": {  
        "type": "Property",  
        "value": true  
    },  
    "lineTerminator": {  
        "type": "Property",  
        "value": ""  
    },  
    "nullSequence": {  
        "type": "Property",  
        "value": "\N"  
    },  
    "quoteChar": {  
        "type": "Property",  
        "value": "'"  
    },  
    "escapeChar": {  
        "type": "Property",  
        "value": "\"  
    },  
    "skipInitialSpace": {  
        "type": "Property",  
        "value": false  
    },  
    "header": {  
        "type": "Property",  
        "value": false  
    },  
    "commentChar": {  
        "type": "Property",  
        "value": "#"  
    },  
    "caseSensitiveHeader": {  
        "type": "Property",  
        "value": true  
    },  
    "@context": [  
        "https://smartdatamodels.org/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.FrictionlessData/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
