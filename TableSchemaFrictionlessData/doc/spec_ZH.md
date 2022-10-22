<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。表格式无摩擦数据（TableSchemaFrictionlessData  
=======================================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/TableSchemaFrictionlessData/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**该资源的表模式，符合表模式规范。为智能数据模型倡议而转换的原始无摩擦数据**。  
版本：0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `alternateName[string]`: 这个项目的一个替代名称  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `fields[array]`: 一个表模式字段对象的数组  - `foreignKeys[array]`:   - `id[*]`: 实体的唯一标识符  - `missingValues[array]`: 许多数据集都有缺失的数据值，要么是因为没有收集到某个值，要么是因为它从未存在过。缺失的值可以简单地通过值为空来表示，在其他情况下，可能使用了一个特殊的值，例如'-'、'NaN'、'0'、'-9999'等。"missingValues "属性提供了一种方法来表示这些值应被解释为等同于null。missingValues "是字符串，而不是特定字段的数据类型。这允许在铸造之前进行比较，并允许字段拥有不属于其类型的缺失值，例如，"数字 "字段的缺失值由"-"表示。对于非字符串类型的字段，"缺失值 "的默认值是空字符串""。对于字符串类型的字段，'missingValue'没有默认值（对于字符串字段，空字符串''是一个有效值，不需要表示空）。在源中遇到的值应被视为 "空"、"不存在 "或 "空白 "值  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `primaryKey[array]`: primaryKey中的字段名 "必须 "是唯一的，并且 "必须 "与相关表中的字段名相匹配。有一个具有单一值的数组是可以接受的，表明单一字段的值是主键。主键是一个字段名或字段名的数组，其值 "必须 "唯一地识别表中的每一行。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: 它必须是TableSchemaFrictionlessData。NGSI实体类型  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `fields`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
这个数据模型来自于原始的无摩擦数据，可以在https://frictionlessdata.io/。有几个变化。1)id和type已经成为强制性的，只要它们在NGSI标准中是强制性的 2)json模式的结构已经被调整为智能数据模型的官方格式。见贡献手册[https://bit.ly/contribution_manual](https://bit.ly/contribution_manual)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TableSchemaFrictionlessData:    
  description: 'A Table Schema for this resource, compliant with the Table Schema specification. Converted for Smart Data Models initiative from original frictionless data'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    fields:    
      description: 'An array of Table Schema Field objects'    
      items:    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    foreignKeys:    
      description: ""    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &tableschemafrictionlessdata_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    missingValues:    
      description: 'Many datasets arrive with missing data values, either because a value was not collected or it never existed. Missing values may be indicated simply by the value being empty in other cases a special value may have been used e.g. ''-'', ''NaN'', ''0'', ''-9999'' etc.The ''missingValues'' property provides a way to indicate that these values should be interpreted as equivalent to null. The ''missingValues'' are strings rather than being the data type of the particular field. This allows for comparison prior to casting and for fields to have missing value which are not of their type, for example a ''number'' field to have missing values indicated by ''-''.The default value of ''missingValue'' for a non-string type field is the empty string ''''. For string type fields there is no default for ''missingValue'' (for string fields the empty string '''' is a valid value and need not indicate null). Values that when encountered in the source, should be considered as ''null'', ''not present'', or ''blank'' values'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *tableschemafrictionlessdata_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    primaryKey:    
      description: 'Field name in the primaryKey ''MUST'' be unique, and ''MUST'' match a field name in the associated table. It is acceptable to have an array with a single value, indicating that the value of a single field is the primary key. A primary key is a field name or an array of field names, whose values ''MUST'' uniquely identify each row in the table'    
      items:    
        type: string    
      minItems: 1    
      type: array    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'it has to be TableSchemaFrictionlessData. NGSI entity type'    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - fields    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.FrictionlessData/blob/master/TableSchemaFrictionlessData/LICENSE.md    
  x-model-schema: ""    
  x-model-tags: SDG    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### TableSchemaFrictionlessData NGSI-v2关键值示例  
下面是一个以JSON-LD格式作为关键值的TableSchemaFrictionlessData的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TableSchemaFrictionlessData:XVFE:0034",  
  "type": "TableSchemaFrictionlessData",  
  "fields": [  
    {  
      "name": "first_name",  
      "type": "string",  
      "constraints": {  
        "required": true  
      }  
    },  
    {  
      "name": "age",  
      "type": "integer"  
    }  
  ],  
  "primaryKey": [  
    "name"  
  ]  
}  
```  
</details>  
#### TableSchemaFrictionlessData NGSI-v2规范化示例  
这里有一个JSON-LD格式的TableSchemaFrictionlessData的例子，是规范化的。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TableSchemaFrictionlessData:XVFE:0034",  
  "type": "TableSchemaFrictionlessData",  
  "fields": {  
    "type": "array",  
    "value": [  
      {  
        "name": "first_name",  
        "type": "string",  
        "constraints": {  
          "required": true  
        }  
      },  
      {  
        "name": "age",  
        "type": "integer"  
      }  
    ]  
  },  
  "primaryKey": {  
    "type": "array",  
    "value": [  
      "name"  
    ]  
  }  
}  
```  
</details>  
#### TableSchemaFrictionlessData NGSI-LD关键值示例  
这里是一个以JSON-LD格式作为key-values的TableSchemaFrictionlessData的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:TableSchemaFrictionlessData:XVFE:0034",  
    "type": "TableSchemaFrictionlessData",  
    "fields": [  
        {  
            "name": "first_name",  
            "type": "string",  
            "constraints": {  
                "required": true  
            }  
        },  
        {  
            "name": "age",  
            "type": "integer"  
        }  
    ],  
    "primaryKey": [  
        "name"  
    ],  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.FrictionlessData/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### TableSchemaFrictionlessData NGSI-LD规范化示例  
这里有一个JSON-LD格式的TableSchemaFrictionlessData的例子，是规范化的。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TableSchemaFrictionlessData:XVFE:0034",  
  "type": "TableSchemaFrictionlessData",  
  "fields": {  
    "type": "Property",  
    "value": [  
      {  
        "name": "first_name",  
        "type": "string",  
        "constraints": {  
          "required": true  
        }  
      },  
      {  
        "name": "age",  
        "type": "integer"  
      }  
    ]  
  },  
  "primaryKey": {  
    "type": "Property",  
    "value": [  
      "name"  
    ]  
  },  
  "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.FrictionlessData/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
