<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: CSVDialectFrictionlessData  
===============================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/CSVDialectFrictionlessData/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **원본 마찰 없는 데이터에서 스마트 데이터 모델 이니셔티브를 위해 변환된 CSV 방언 설명자**.  
버전: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `alternateName[string]`: 이 항목의 대체 이름  - `caseSensitiveHeader[boolean]`: 대소문자 구분 헤더. 소스 CSV 파일에서 대소문자를 사용하는 것이 항상 의도적으로 결정되는 것은 아닙니다. 예를 들어, 'CAT'과 'Cat'은 같은 의미로 간주해야 할까요? 헤더의 대소문자가 의미가 있는지 지정합니다.  - `commentChar[string]`: 주석 문자. 앞의 공백 없이 이 한 글자 문자열로 시작하는 행이 있으면 전체 행을 무시하도록 지정합니다.  - `csvddfVersion[number]`: CSV Dialect 스키마 버전. CSV Dialect의 스키마 버전을 나타내는 숫자입니다. 버전 1.0은 CSV Dialect Description Format으로 명명되었으며 다른 필드 이름을 사용했습니다.  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `delimiter[string]`: 구분 기호. 필드 구분 기호로 사용할 문자 시퀀스  - `description[string]`: 이 항목에 대한 설명  - `doubleQuote[boolean]`: 큰따옴표. 큰따옴표가 true로 설정되어 있으면 연속된 두 개의 따옴표는 하나로 해석되어야 합니다. 필드 내부의 따옴표 처리를 지정합니다.  - `escapeChar[string]`: 이스케이프 문자. 이스케이프 문자로 사용할 한 문자 문자열을 지정합니다.  - `header[boolean]`: 헤더. 파일에 헤더 행이 포함되는지(항상 파일의 첫 번째 행으로) 지정합니다.  - `id[*]`: 엔티티의 고유 식별자  - `lineTerminator[string]`: 줄 종결자. 행을 종료하는 데 사용해야 하는 문자 시퀀스를 지정합니다.  - `name[string]`: 이 항목의 이름  - `nullSequence[string]`: 널 시퀀스. 예를 들어 \ 다음에 'N'과 같은 널 시퀀스를 지정합니다.  - `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `quoteChar[string]`: 인용 문자. 인용 문자로 사용할 한 글자 문자열을 지정합니다.  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `skipInitialSpace[boolean]`: 초기 공백 건너뛰기. 구분 기호 바로 뒤에 오는 공백의 해석을 지정합니다. 거짓이면 구분 기호 바로 뒤의 공백을 후속 필드의 일부로 처리합니다.  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `type[string]`: CSVDialectFrictionlessData여야 합니다. NGSI 엔티티 유형  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `delimiter`  - `doubleQuote`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
이 데이터 모델은 https://frictionlessdata.io/ 에서 찾을 수 있는 원래의 마찰 없는 데이터에서 가져온 것입니다. 몇 가지 사소한 변경 사항이 있습니다. 1) 아이디와 타입이 필수로 추가되었습니다. 2) json 스키마의 구조가 스마트 데이터 모델의 공식 형식에 맞게 조정되었습니다. 기여 매뉴얼 [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual)을 참조하세요. 3) 호환성을 위해 몇 가지 추가 속성이 추가되었습니다.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
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
## 페이로드 예시  
#### CSVDialectFrictionlessData NGSI-v2 키 값 예제  
다음은 키-값으로 JSON-LD 형식의 CSVDialectFrictionlessData의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
  "escapeChar": "\\",  
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
#### CSVDialectFrictionlessData NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 CSVDialectFrictionlessData의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:CSVDialect:items:YPBX:70706198",  
      "urn:ngsi-ld:CSVDialect:items:MABG:25535507"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:CSVDialect:items:YNLD:15120048",  
      "urn:ngsi-ld:CSVDialect:items:EFIZ:80683325"  
    ]  
  },  
  "csvddfVersion": {  
    "type": "number",  
    "value": 1.2  
  },  
  "delimiter": {  
    "type": "Text",  
    "value": "%3B"  
  },  
  "doubleQuote": {  
    "type": "boolean",  
    "value": true  
  },  
  "lineTerminator": {  
    "type": "Text",  
    "value": "\\r\\n"  
  },  
  "nullSequence": {  
    "type": "Text",  
    "value": "\\N"  
  },  
  "quoteChar": {  
    "type": "Text",  
    "value": "'"  
  },  
  "escapeChar": {  
    "type": "Text",  
    "value": "\\\\"  
  },  
  "skipInitialSpace": {  
    "type": "boolean",  
    "value": false  
  },  
  "header": {  
    "type": "boolean",  
    "value": false  
  },  
  "commentChar": {  
    "type": "Text",  
    "value": "#"  
  },  
  "caseSensitiveHeader": {  
    "type": "boolean",  
    "value": true  
  }  
}  
```  
</details>  
#### CSVDialectFrictionlessData NGSI-LD 키 값 예시  
다음은 키-값으로 JSON-LD 형식의 CSVDialectFrictionlessData의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
    "escapeChar": "\\",  
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
#### CSVDialectFrictionlessData NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 CSVDialectFrictionlessData의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
        "value": "\\N"  
    },  
    "quoteChar": {  
        "type": "Property",  
        "value": "'"  
    },  
    "escapeChar": {  
        "type": "Property",  
        "value": "\\"  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
