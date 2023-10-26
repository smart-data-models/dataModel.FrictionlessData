<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 데이터 패키지 마찰없는 데이터  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/DataPackageFrictionlessData/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **데이터 패키지는 데이터 액세스 및 전송을 위한 간단한 사양으로, 원래의 마찰 없는 데이터에서 스마트 데이터 모델 이니셔티브를 위해 변환되었습니다**.  
버전: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `contributors[array]`: 기여자. 이 설명자의 기여자  - `created[string]`: 생성되었습니다. 날짜/시간은 [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6)에 설명된 날짜/시간에 대한 문자열 형식을 준수해야 합니다. 이 설명자가 생성된 날짜/시간입니다.  - `description[string]`: 설명. . 텍스트 설명입니다. 마크다운 권장  - `homepage[string]`: 홈 페이지. . 이 데이터 패키지와 관련된 웹상의 홈입니다.  - `id[string]`: ID. 데이터 패키지의 일반적인 사용 패턴은 시스템 또는 플랫폼의 범위 내에서 패키징 형식으로 사용하는 것입니다. 이러한 경우, 기존 패키지 업데이트와 같은 일반적인 데이터 처리 워크플로우를 위해 패키지에 대한 고유 식별자가 필요합니다. 사양 수준에서는 전역 고유성을 검증할 수 없지만, `id` 속성을 사용하는 소비자는 식별자가 전역적으로 고유한지 확인해야 합니다. 전 세계적으로 고유한 식별자를 위해 예약된 속성입니다. 고유 식별자의 예로는 UUID와 DOI가 있습니다.  - `image[string]`: 이미지. . 이 패키지를 나타내는 이미지  - `keywords[array]`: 키워드. . 이 패키지를 설명하는 키워드 목록  - `licenses[array]`: 라이선스. 이 속성은 법적 구속력이 없으며 여기에 정의된 조건에 따라 패키지의 라이선스가 부여되었음을 보장하지 않습니다. 이 패키지가 게시되는 라이선스(들)  - `name[string]`: 이름. URL에서 사용할 수 있고 사람이 읽을 수 있는 이름이 이상적입니다. 이름은 '불변'이어야 합니다. 즉, 상위 설명자가 업데이트될 때 '변경되지 않아야' 합니다. 식별자 문자열입니다. .`, `_`, `-` 및 `/`가 포함된 소문자만 허용됩니다.  - `profile[string]`: 프로필. 모든 패키지 및 리소스 설명자에는 프로필이 있습니다. 기본 프로필이 선언되지 않은 경우 기본 프로필은 패키지의 경우 `데이터-패키지`, 리소스의 경우 `데이터-리소스`입니다. 이 설명자의 프로필  - `resources[array]`: 데이터 리소스. 데이터 리소스 객체의 '배열'로, 각각 [데이터 리소스](/data-resource/) 사양을 준수합니다.  - `sources[array]`: 출처. 이 리소스의 원시 소스  - `title[string]`: 제목. . 사람이 읽을 수 있는 제목  - `type[string]`: DataPackageFrictionlessData여야 합니다. NGSI 엔티티 유형  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `resources`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
이 데이터 모델은 https://frictionlessdata.io/ 에서 찾을 수 있는 원래의 마찰 없는 데이터에서 가져온 것입니다. 몇 가지 변경 사항이 있습니다. 1) 아이디와 타입이 필수로 추가되었습니다. 2) json 스키마의 구조가 스마트 데이터 모델의 공식 형식에 맞게 조정되었습니다. 기여 매뉴얼 참조 [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
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
      description: Image. . A image to represent this package    
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
        type: string    
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
  x-model-schema: ""    
  x-model-tags: SDG    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### DataPackageFrictionlessData NGSI-v2 키 값 예시  
다음은 키-값으로 JSON-LD 형식의 데이터 패키지 무결성 데이터의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### DataPackageFrictionlessData NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 데이터 패키지 마찰없는 데이터의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### DataPackageFrictionlessData NGSI-LD 키 값 예시  
다음은 키-값으로 JSON-LD 형식의 데이터 패키지 무결성 데이터의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### DataPackageFrictionlessData NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 데이터 패키지 마찰없는 데이터의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
