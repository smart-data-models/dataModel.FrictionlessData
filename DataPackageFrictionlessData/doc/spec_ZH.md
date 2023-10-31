<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体数据包无摩擦数据  
==========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/DataPackageFrictionlessData/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**数据包是一种用于数据访问和交付的简单规范。  
版本： 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `contributors[array]`: 贡献者。本说明的撰稿人  - `created[string]`: 已创建。日期时间必须符合 [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6) 中描述的日期时间字符串格式。创建该描述符的日期时间  - `description[string]`: 说明..文本描述。鼓励使用 Markdown  - `homepage[string]`: 主页..与该数据包相关的网络主页  - `id[string]`: ID数据包的常见使用模式是在系统或平台范围内作为一种打包格式。在这种情况下，需要为数据包提供唯一标识符，以便进行常见的数据处理工作流，如更新现有数据包。虽然在规范层面上无法验证全局唯一性，但使用 `id` 属性 `MUST` 的消费者可确保标识符的全局唯一性。为全球唯一标识符保留的属性。唯一标识符的例子包括 UUID 和 DOI。  - `image[string]`: 图片..代表此软件包的图像  - `keywords[array]`: 关键词.描述此软件包的关键字列表  - `licenses[array]`: 许可证。此属性不具有法律约束力，也不保证软件包已获得此处定义的许可。发布本软件包所依据的许可证  - `name[string]`: 名称。理想情况下，这是一个 url 可用且人类可读的名称。名称 "应 "是不变的，也就是说，当父描述符更新时，它 "不应 "改变。标识符字符串。允许使用带 `.`、`_`、`-` 和 `/` 的小写字符。  - `profile[string]`: 简介。每个包和资源描述符都有一个配置文件。如果未声明配置文件，则默认配置文件为 "包 "的 "数据-包 "和 "资源 "的 "数据-资源"。该描述符的配置文件  - `resources[array]`: 数据资源。数据资源对象的 "数组"，每个对象都符合 [数据资源](/data-resource/) 规范  - `sources[array]`: 资料来源。本资源的原始资料来源  - `title[string]`: 标题..人类可读的标题  - `type[string]`: 必须是 DataPackageFrictionlessData。NGSI 实体类型  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `resources`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
该数据模型来自原始的无摩擦数据，可在 https://frictionlessdata.io/ 上找到。其中有几处改动。1）id 和类型已成为必填项 2）json 模式的结构已调整为智能数据模型的官方格式。参见贡献手册 [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DataPackageFrictionlessData:    
  description: Data Package is a simple specification for data access and delivery.Converted for Smart Data Models initiative from original frictionless data    
  properties:    
    contributors:    
      description: Contributors. The contributors to this descriptor    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    created:    
      description: "Created. The datetime must conform to the string formats for datetime as described in [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6). The datetime on which this descriptor was created"    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: Description. . A text description. Markdown is encouraged    
      type: string    
      x-ngsi:    
        type: Property    
    homepage:    
      description: Home Page. . The home on the web that is related to this data package    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      description: 'ID. A common usage pattern for Data Packages is as a packaging format within the bounds of a system or platform. In these cases, a unique identifier for a package is desired for common data handling workflows, such as updating an existing package. While at the level of the specification, global uniqueness cannot be validated, consumers using the `id` property `MUST` ensure identifiers are globally unique. A property reserved for globally unique identifiers. Examples of identifiers that are unique include UUIDs and DOIs'    
      type: string    
      x-ngsi:    
        type: Property    
    image:    
      description: Image. A image to represent this package    
      type: string    
      x-ngsi:    
        type: Property    
    keywords:    
      description: Keywords. . A list of keywords that describe this package    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    licenses:    
      description: Licenses. This property is not legally binding and does not guarantee that the package is licensed under the terms defined herein. The license(s) under which this package is published    
      items:    
        description: A license for this descriptor    
        properties:    
          name:    
            description: 'MUST be an Open Definition license identifier, see http://licenses.opendefinition.org/'    
            pattern: ^([-a-zA-Z0-9._])+$    
            type: string    
            x-ngsi:    
              type: Property    
          path:    
            description: 'A fully qualified URL, or a POSIX file path'    
            pattern: ^(?=^[^./~])(^((?!\.{2}).)*$).*$    
            type: string    
            x-ngsi:    
              type: Property    
          title:    
            description: A human-readable title    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    name:    
      description: 'Name. This is ideally a url-usable and human-readable name. Name `SHOULD` be invariant, meaning it `SHOULD NOT` change when its parent descriptor is updated. An identifier string. Lower case characters with `.`, `_`, `-` and `/` are allowed'    
      type: string    
      x-ngsi:    
        type: Property    
    profile:    
      description: 'Profile. Every Package and Resource descriptor has a profile. The default profile, if none is declared, is `data-package` for Package and `data-resource` for Resource. The profile of this descriptor'    
      type: string    
      x-ngsi:    
        type: Property    
    resources:    
      description: 'Data Resources. An `array` of Data Resource objects, each compliant with the [Data Resource](/data-resource/) specification'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    sources:    
      description: Sources. The raw sources for this resource    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    title:    
      description: Title. . A human-readable title    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: It has to be DataPackageFrictionlessData. NGSI entity type    
      enum:    
        - DataPackageFrictionlessData    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - resources    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.FrictionlessData/blob/master/DataPackageFrictionlessData/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.FrictionlessData/DataPackageFrictionlessData/schema.json    
  x-model-tags: SDG    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
#### DataPackageFrictionlessData NGSI-v2 key-values 示例  
下面是一个以 JSON-LD 格式作为键值的 DataPackageFrictionlessData 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "uri:ngsi-ld:datapackage:001",  
  "type": "DataPackageFrictionlessData",  
  "name": "cpi",  
  "title": "Annual Consumer Price Index (CPI)",  
  "description": "Annual Consumer Price Index (CPI) for most countries in the world. Reference year is 2005.",  
  "profile": "tabular-data-package",  
  "licenses": [  
    {  
      "name": "CC-BY-4.0",  
      "title": "Creative Commons Attribution 4.0",  
      "path": "https://creativecommons.org/licenses/by/4.0/"  
    }  
  ],  
  "keywords": [  
    "CPI",  
    "World",  
    "Consumer Price Index",  
    "Annual Data",  
    "The World Bank"  
  ],  
  "version": "2.0.0",  
  "sources": [  
    {  
      "title": "The World Bank",  
      "path": "http://data.worldbank.org/indicator/FP.CPI.TOTL"  
    }  
  ],  
  "resources": [  
    {  
      "path": "data/cpi.csv",  
      "name": "cpi",  
      "profile": "tabular-data-resource",  
      "schema": {  
        "fields": [  
          {  
            "name": "Country Name",  
            "type": "string"  
          },  
          {  
            "name": "Country Code",  
            "type": "string"  
          },  
          {  
            "name": "Year",  
            "type": "year"  
          },  
          {  
            "name": "CPI",  
            "description": "CPI (where 2005=100)",  
            "type": "number"  
          }  
        ]  
      }  
    }  
  ]  
}  
```  
</details>  
#### DataPackageFrictionlessData NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 DataPackageFrictionlessData 示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "uri:ngsi-ld:datapackage:001",  
  "type": "DataPackageFrictionlessData",  
  "name": {  
    "type": "string",  
    "value": "cpi"  
  },  
  "title": {  
    "type": "string",  
    "value": "Annual Consumer Price Index (CPI)"  
  },  
  "description": {  
    "type": "string",  
    "value": "Annual Consumer Price Index (CPI) for most countries in the world. Reference year is 2005."  
  },  
  "profile": {  
    "type": "string",  
    "value": "tabular-data-package"  
  },  
  "licenses": {  
    "type": "array",  
    "value": [  
      {  
        "name": "CC-BY-4.0",  
        "title": "Creative Commons Attribution 4.0",  
        "path": "https://creativecommons.org/licenses/by/4.0/"  
      }  
    ]  
  },  
  "keywords": {  
    "type": "array",  
    "value": [  
      "CPI",  
      "World",  
      "Consumer Price Index",  
      "Annual Data",  
      "The World Bank"  
    ]  
  },  
  "version": {  
    "type": "string",  
    "value": "2.0.0"  
  },  
  "sources": {  
    "type": "array",  
    "value": [  
      {  
        "title": "The World Bank",  
        "path": "http://data.worldbank.org/indicator/FP.CPI.TOTL"  
      }  
    ]  
  },  
  "resources": {  
    "type": "array",  
    "value": [  
      {  
        "path": "data/cpi.csv",  
        "name": "cpi",  
        "profile": "tabular-data-resource",  
        "schema": {  
          "fields": [  
            {  
              "name": "Country Name",  
              "type": "string"  
            },  
            {  
              "name": "Country Code",  
              "type": "string"  
            },  
            {  
              "name": "Year",  
              "type": "year"  
            },  
            {  
              "name": "CPI",  
              "description": "CPI (where 2005=100)",  
              "type": "number"  
            }  
          ]  
        }  
      }  
    ]  
  }  
}  
```  
</details>  
#### DataPackageFrictionlessData NGSI-LD 键值示例  
下面是一个以 JSON-LD 格式作为键值的 DataPackageFrictionlessData 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "uri:ngsi-ld:datapackage:001",  
    "type": "DataPackageFrictionlessData",  
    "description": "Annual Consumer Price Index (CPI) for most countries in the world. Reference year is 2005.",  
    "keywords": [  
        "CPI",  
        "World",  
        "Consumer Price Index",  
        "Annual Data",  
        "The World Bank"  
    ],  
    "licenses": [  
        {  
            "name": "CC-BY-4.0",  
            "title": "Creative Commons Attribution 4.0",  
            "path": "https://creativecommons.org/licenses/by/4.0/"  
        }  
    ],  
    "name": "cpi",  
    "profile": "tabular-data-package",  
    "resources": [  
        {  
            "path": "data/cpi.csv",  
            "name": "cpi",  
            "profile": "tabular-data-resource",  
            "schema": {  
                "fields": [  
                    {  
                        "name": "Country Name",  
                        "type": "string"  
                    },  
                    {  
                        "name": "Country Code",  
                        "type": "string"  
                    },  
                    {  
                        "name": "Year",  
                        "type": "year"  
                    },  
                    {  
                        "name": "CPI",  
                        "description": "CPI (where 2005=100)",  
                        "type": "number"  
                    }  
                ]  
            }  
        }  
    ],  
    "sources": [  
        {  
            "title": "The World Bank",  
            "path": "http://data.worldbank.org/indicator/FP.CPI.TOTL"  
        }  
    ],  
    "title": "Annual Consumer Price Index (CPI)",  
    "version": "2.0.0",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.FrictionlessData/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### DataPackageFrictionlessData NGSI-LD 标准化示例  
下面是一个规范化 JSON-LD 格式的 DataPackageFrictionlessData 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "uri:ngsi-ld:datapackage:001",  
    "type": "DataPackageFrictionlessData",  
    "description": {  
        "type": "Property",  
        "value": "Annual Consumer Price Index (CPI) for most countries in the world. Reference year is 2005."  
    },  
    "keywords": {  
        "type": "Property",  
        "value": [  
            "CPI",  
            "World",  
            "Consumer Price Index",  
            "Annual Data",  
            "The World Bank"  
        ]  
    },  
    "licenses": {  
        "type": "Property",  
        "value": [  
            {  
                "name": "CC-BY-4.0",  
                "title": "Creative Commons Attribution 4.0",  
                "path": "https://creativecommons.org/licenses/by/4.0/"  
            }  
        ]  
    },  
    "name": {  
        "type": "Property",  
        "value": "cpi"  
    },  
    "profile": {  
        "type": "Property",  
        "value": "tabular-data-package"  
    },  
    "resources": {  
        "type": "Property",  
        "value": [  
            {  
                "path": "data/cpi.csv",  
                "name": "cpi",  
                "profile": "tabular-data-resource",  
                "schema": {  
                    "fields": [  
                        {  
                            "name": "Country Name",  
                            "type": "string"  
                        },  
                        {  
                            "name": "Country Code",  
                            "type": "string"  
                        },  
                        {  
                            "name": "Year",  
                            "type": "year"  
                        },  
                        {  
                            "name": "CPI",  
                            "description": "CPI (where 2005=100)",  
                            "type": "number"  
                        }  
                    ]  
                }  
            }  
        ]  
    },  
    "sources": {  
        "type": "Property",  
        "value": [  
            {  
                "title": "The World Bank",  
                "path": "http://data.worldbank.org/indicator/FP.CPI.TOTL"  
            }  
        ]  
    },  
    "title": {  
        "type": "Property",  
        "value": "Annual Consumer Price Index (CPI)"  
    },  
    "version": {  
        "type": "Property",  
        "value": "2.0.0"  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
