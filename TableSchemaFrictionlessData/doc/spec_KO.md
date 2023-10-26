<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: TableSchemaFrictionlessData  
===================================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/TableSchemaFrictionlessData/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
전역 설명: **테이블 스키마 사양을 준수하는 이 리소스에 대한 테이블 스키마입니다. 원본 마찰 없는 데이터에서 스마트 데이터 모델 이니셔티브를 위해 변환됨**.  
버전: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `alternateName[string]`: 이 항목의 대체 이름  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `fields[array]`: 테이블 스키마 필드 개체 배열  - `foreignKeys[array]`:   - `id[*]`: 엔티티의 고유 식별자  - `missingValues[array]`: 많은 데이터 세트는 값이 수집되지 않았거나 존재하지 않았기 때문에 누락된 데이터 값과 함께 도착합니다. 누락된 값은 단순히 값이 비어 있는 것으로 표시될 수도 있고, '-', 'NaN', '0', '-9999' 등의 특수 값이 사용되었을 수도 있습니다. 'missingValues' 속성은 이러한 값이 null과 동등한 것으로 해석되어야 함을 나타내는 방법을 제공합니다. 'missingValues'는 특정 필드의 데이터 유형이 아닌 문자열입니다. 이를 통해 필드에 해당 유형이 아닌 누락된 값이 있는 경우(예: '숫자' 필드에 '-'로 표시된 누락된 값이 있는 경우) 캐스팅 전에 비교할 수 있으며, 문자열 유형이 아닌 필드에 대한 'missingValue'의 기본값은 빈 문자열 ''입니다. 문자열 유형 필드의 경우 'missingValue'에 대한 기본값이 없습니다(문자열 필드의 경우 빈 문자열 ''이 유효한 값이며 null을 표시할 필요가 없음). 소스에서 발견되면 'null', '없음' 또는 '빈' 값으로 간주해야 하는 값은 다음과 같습니다.  - `name[string]`: 이 항목의 이름  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `primaryKey[array]`: primaryKey의 필드 이름은 '반드시' 고유해야 하며, '반드시' 연결된 테이블의 필드 이름과 일치해야 합니다. 단일 필드의 값이 기본 키임을 나타내는 단일 값을 가진 배열을 사용할 수 있습니다. 기본 키는 필드 이름 또는 필드 이름의 배열로, 값이 '반드시' 테이블의 각 행을 고유하게 식별해야 합니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: TableSchemaFrictionlessData여야 합니다. NGSI 엔티티 유형  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `fields`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
이 데이터 모델은 https://frictionlessdata.io/ 에서 찾을 수 있는 원래의 마찰 없는 데이터에서 가져온 것입니다. 몇 가지 변경 사항이 있습니다. 1) 아이디와 타입이 NGSI 표준에 따라 필수 항목으로 변경되었습니다. 2) json 스키마의 구조가 스마트 데이터 모델의 공식 형식에 맞게 조정되었습니다. 기여 매뉴얼 참조 [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TableSchemaFrictionlessData:    
  description: 'A Table Schema for this resource, compliant with the Table Schema specification. Converted for Smart Data Models initiative from original frictionless data'    
  properties:    
    alternateName:    
      description: An alternative name for this item    
      type: string    
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
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    fields:    
      description: An array of Table Schema Field objects    
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
    missingValues:    
      description: 'Many datasets arrive with missing data values, either because a value was not collected or it never existed. Missing values may be indicated simply by the value being empty in other cases a special value may have been used e.g. ''-'', ''NaN'', ''0'', ''-9999'' etc.The ''missingValues'' property provides a way to indicate that these values should be interpreted as equivalent to null. The ''missingValues'' are strings rather than being the data type of the particular field. This allows for comparison prior to casting and for fields to have missing value which are not of their type, for example a ''number'' field to have missing values indicated by ''-''.The default value of ''missingValue'' for a non-string type field is the empty string ''''. For string type fields there is no default for ''missingValue'' (for string fields the empty string '''' is a valid value and need not indicate null). Values that when encountered in the source, should be considered as ''null'', ''not present'', or ''blank'' values'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
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
    primaryKey:    
      description: 'Field name in the primaryKey ''MUST'' be unique, and ''MUST'' match a field name in the associated table. It is acceptable to have an array with a single value, indicating that the value of a single field is the primary key. A primary key is a field name or an array of field names, whose values ''MUST'' uniquely identify each row in the table'    
      items:    
        type: string    
      minItems: 1    
      type: array    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: it has to be TableSchemaFrictionlessData. NGSI entity type    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - fields    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
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
## 페이로드 예시  
#### TableSchemaFrictionlessData NGSI-v2 키-값 예제  
다음은 키-값으로 JSON-LD 형식의 TableSchemaFrictionlessData의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### TableSchemaFrictionlessData NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 TableSchemaFrictionlessData의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### TableSchemaFrictionlessData NGSI-LD 키-값 예제  
다음은 키-값으로 JSON-LD 형식의 TableSchemaFrictionlessData의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### TableSchemaFrictionlessData NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 TableSchemaFrictionlessData의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
