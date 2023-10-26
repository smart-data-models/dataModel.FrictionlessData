<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 데이터자원 마찰없는데이터  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/DataResourceFrictionlessData/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **데이터 리소스.스마트 데이터 모델 이니셔티브를 위해 원래의 마찰 없는 데이터에서 변환됨**  
버전: 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역에 속한 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `bytes[number]`: 바이트. 이 리소스의 크기(바이트)  - `data[array]`: 데이터. 이 리소스에 대한 인라인 데이터  - `description[string]`: 설명. 텍스트 설명입니다. 마크다운을 권장합니다.  - `encoding[string]`: 인코딩. 이 리소스의 파일 인코딩  - `format[string]`: 형식. 'CSV', 'XLS', 'JSON'이 일반적인 형식의 예입니다. 이 리소스의 파일 형식  - `hash[string]`: 해시. 이 리소스의 MD5 해시입니다. 알고리즘}:{해시} 형식을 사용하여 다른 해싱 알고리즘을 표시합니다.  - `homepage[string]`: 홈 페이지. 이 데이터 패키지와 관련된 웹상의 홈페이지  - `id[*]`: 엔티티의 고유 식별자  - `licenses[array]`: 라이선스. 이 속성은 법적 구속력이 없으며 여기에 정의된 조건에 따라 패키지의 라이선스가 부여되었음을 보장하지 않습니다. 리소스가 게시되는 라이선스(들)  - `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인 문자열, 다각형, 멀티포인트, 멀티라인 문자열 또는 멀티폴리곤일 수 있습니다.  - `mediatype[string]`: 미디어 유형. 이 리소스의 미디어 유형입니다. IANA](https://www.iana.org/assignments/media-types/media-types.xhtml)에 나열된 모든 유효한 미디어 유형일 수 있습니다.  - `name[string]`: 이름. URL에서 사용할 수 있고 사람이 읽을 수 있는 이름이 이상적입니다. 이름은 '불변'이어야 합니다. 즉, 상위 설명자가 업데이트될 때 '변경되지 않아야' 합니다. 식별자 문자열입니다. '.', '_', '-' 및 '/'가 포함된 소문자만 허용됩니다.  - `path[array]`: 경로. '경로'에서 참조된 각 데이터 소스의 역참조된 값은 리소스가 설명하는 데이터의 역참조된 네이티브 표현에 상응하는 값이어야 합니다. 예를 들어, *표 형식* 데이터 리소스에서 '경로'의 역참조된 값은 반드시 배열이어야 한다는 의미입니다. 이 리소스의 데이터에 대한 참조는 문자열로서의 경로 또는 문자열로서의 경로 배열입니다. 유효한 URI의 수  - `profile[string]`: 프로필. 모든 패키지 및 리소스 설명자에는 프로필이 있습니다. 선언된 프로필이 없는 경우 기본 프로필은 패키지의 경우 'data-package', 리소스의 경우 'data-resource'입니다. 이 디스크립터의 프로필  - `schema[object]`: 스키마. 이 리소스에 대한 스키마  - `sources[array]`: 출처. . 이 리소스의 원시 소스  - `title[string]`: 제목. 사람이 읽을 수 있는 제목  - `type[string]`: NGSI 엔티티 유형. DataResourceFrictionlessData여야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
이 데이터 모델은 https://frictionlessdata.io/ 에서 찾을 수 있는 원래의 마찰 없는 데이터에서 가져온 것입니다. 몇 가지 변경 사항이 있습니다. 1) 아이디와 타입은 NGSI-LD 표준에서 요구하는 대로 필수 항목이 되었습니다. 2) json 스키마의 구조는 스마트 데이터 모델의 공식 형식에 맞게 조정되었습니다. 기여 매뉴얼 [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual) 참조. 호환성을 위해 데이터 속성과 소스 속성을 객체 배열로 정의했습니다. 또한 유형도 포함되었습니다.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DataResourceFrictionlessData:    
  description: Data Resource.Converted for Smart Data Models initiative from original frictionless data    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    bytes:    
      description: Bytes. The size of this resource in bytes    
      type: number    
      x-ngsi:    
        type: Property    
    data:    
      description: Data. Inline data for this resource    
      items:    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    description:    
      description: Description. A text description. Markdown is encouraged    
      type: string    
      x-ngsi:    
        type: Property    
    encoding:    
      description: Encoding. The file encoding of this resource    
      type: string    
      x-ngsi:    
        type: Property    
    format:    
      description: 'Format. ''csv'', ''xls'', ''json'' are examples of common formats. The file format of this resource'    
      type: string    
      x-ngsi:    
        type: Property    
    hash:    
      description: 'Hash. The MD5 hash of this resource. Indicate other hashing algorithms with the {algorithm}:{hash} format'    
      pattern: ^([^:]+:[a-fA-F0-9]+|[a-fA-F0-9]{32}|)$    
      type: string    
      x-ngsi:    
        type: Property    
    homepage:    
      description: Home Page. The home on the web that is related to this data package    
      type: string    
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
    licenses:    
      description: Licenses. This property is not legally binding and does not guarantee that the package is licensed under the terms defined herein. The license(s) under which the resource is published    
      items:    
        properties:    
          name:    
            type: string    
          path:    
            type: string    
          title:    
            type: string    
        type: object    
      minItems: 1    
      type: array    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    mediatype:    
      description: 'Media Type. The media type of this resource. Can be any valid media type listed with [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml)'    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: 'Name. This is ideally a url-usable and human-readable name. Name ''SHOULD'' be invariant, meaning it ''SHOULD NOT'' change when its parent descriptor is updated. An identifier string. Lower case characters with ''.'', ''_'', ''-'' and ''/'' are allowed'    
      type: string    
      x-ngsi:    
        type: Property    
    path:    
      description: 'Path. The dereferenced value of each referenced data source in ''path'' ''MUST'' be commensurate with a native, dereferenced representation of the data the resource describes. For example, in a *Tabular* Data Resource, this means that the dereferenced value of ''path'' ''MUST'' be an array. A reference to the data for this resource, as either a path as a string, or an array of paths as strings. of valid URIs'    
      items:    
        type: string    
      minItems: 1    
      type: array    
      x-ngsi:    
        type: Property    
    profile:    
      description: 'Profile. Every Package and Resource descriptor has a profile. The default profile, if none is declared, is ''data-package'' for Package and ''data-resource'' for Resource. The profile of this descriptor'    
      type: string    
      x-ngsi:    
        type: Property    
    schema:    
      description: Schema. A schema for this resource    
      type: object    
      x-ngsi:    
        type: Property    
    sources:    
      description: Sources. . The raw sources for this resource    
      items:    
        properties:    
          email:    
            format: idn-email    
            type: string    
          path:    
            type: string    
          title:    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    title:    
      description: Title. A human-readable title    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be DataResourceFrictionlessData    
      enum:    
        - DataResourceFrictionlessData    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - name    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.FrictionlessData/blob/master/DataResourceFrictionlessData/LICENSE.md    
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
#### DataResourceFrictionlessData NGSI-v2 키 값 예시  
다음은 키-값으로 JSON-LD 형식의 DataResourceFrictionlessData의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:dataresource:AECS:1234",  
  "type": "DataResourceFrictionlessData",  
  "bytes": 2082,  
  "data": [  
    {},  
    {}  
  ],  
  "description": "My favourite data about the solar system.",  
  "encoding": "utf-8",  
  "format": "csv",  
  "hash": "SHA256:5262f12512590031bbcc9a430452bfd75c2791ad6771320bb4b5728bfb78c4d0",  
  "homepage": "https://smartdatamodels.org",  
  "licenses": [  
    {  
      "name": "CC-BY",  
      "title": "creative commons attribution",  
      "path": "https://creativecommons.org/licenses/by/4.0/deed.en"  
    },  
    {  
      "name": "odc-pddl-1.0",  
      "path": "http://opendatacommons.org/licenses/pddl/",  
      "title": "Open Data Commons Public Domain Dedication and License v1.0"  
    }  
  ],  
  "mediatype": "text/csv",  
  "name": "solar-system",  
  "path": [  
    "http://example.com/solar-system.csv"  
  ],  
  "profile": "tabular-data-package",  
  "schema": {  
  },  
  "sources": [  
    {  
      "title": "Venus",  
      "path": "https://smartdatamodels.org/venus",  
      "email": "venus@smartdatamodels.org"  
    },  
    {  
      "title": "Jupiter",  
      "path": "https://smartdatamodels.org/jupiter",  
      "email": "jupiter@smartdatamodels.org"  
    }  
  ],  
  "title": "The Solar System"  
}  
```  
</details>  
#### DataResourceFrictionlessData NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 DataResourceFrictionlessData의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:dataresource:AECS:1234",  
  "type": "DataResourceFrictionlessData",  
  "bytes": {  
    "type": "number",  
    "value": 2082  
  },  
  "data": {  
    "type": "array",  
    "value": [  
      {},  
      {}  
    ]  
  },  
  "description": {  
    "type": "Text",  
    "value": "My favourite data about the solar system."  
  },  
  "encoding": {  
    "type": "Text",  
    "value": "utf-8"  
  },  
  "format": {  
    "type": "Text",  
    "value": "csv"  
  },  
  "hash": {  
    "type": "Text",  
    "value": "SHA256:5262f12512590031bbcc9a430452bfd75c2791ad6771320bb4b5728bfb78c4d0"  
  },  
  "homepage": {  
    "type": "Text",  
    "value": "https://smartdatamodels.org"  
  },  
  "licenses": {  
    "type": "array",  
    "value": [  
      {  
        "name": "CC-BY",  
        "title": "creative commons attribution",  
        "path": "https://creativecommons.org/licenses/by/4.0/deed.en"  
      },  
      {  
        "name": "odc-pddl-1.0",  
        "path": "http://opendatacommons.org/licenses/pddl/",  
        "title": "Open Data Commons Public Domain Dedication and License v1.0"  
      }  
    ]  
  },  
  "mediatype": {  
    "type": "Text",  
    "value": "text/csv"  
  },  
  "name": {  
    "type": "Text",  
    "value": "solar-system"  
  },  
  "path": {  
    "type": "array",  
    "value": [  
      "http://example.com/solar-system.csv"  
    ]  
  },  
  "profile": {  
    "type": "Text",  
    "value": "tabular-data-package"  
  },  
  "schema": {  
    "type": "object",  
    "value": {}  
  },  
  "sources": {  
    "type": "array",  
    "value": [  
      {  
        "title": "Venus",  
        "path": "https://smartdatamodels.org/venus",  
        "email": "venus@smartdatamodels.org"  
      },  
      {  
        "title": "Jupiter",  
        "path": "https://smartdatamodels.org/jupiter",  
        "email": "jupiter@smartdatamodels.org"  
      }  
    ]  
  },  
  "title": {  
    "type": "Text",  
    "value": "The Solar System"  
  }  
}  
```  
</details>  
#### DataResourceFrictionlessData NGSI-LD 키 값 예시  
다음은 키-값으로 JSON-LD 형식의 DataResourceFrictionlessData의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:dataresource:AECS:1234",  
    "type": "DataResourceFrictionlessData",  
    "bytes": 2082,  
    "data": [  
        {},  
        {}  
    ],  
    "description": "My favourite data about the solar system.",  
    "encoding": "utf-8",  
    "format": "csv",  
    "hash": "SHA256:5262f12512590031bbcc9a430452bfd75c2791ad6771320bb4b5728bfb78c4d0",  
    "homepage": "https://smartdatamodels.org",  
    "licenses": [  
        {  
            "name": "CC-BY",  
            "title": "creative commons attribution",  
            "path": "https://creativecommons.org/licenses/by/4.0/deed.en"  
        },  
        {  
            "name": "odc-pddl-1.0",  
            "path": "http://opendatacommons.org/licenses/pddl/",  
            "title": "Open Data Commons Public Domain Dedication and License v1.0"  
        }  
    ],  
    "mediatype": "text/csv",  
    "name": "solar-system",  
    "path": [  
        "http://example.com/solar-system.csv"  
    ],  
    "profile": "tabular-data-package",  
    "schema": {},  
    "sources": [  
        {  
            "title": "Venus",  
            "path": "https://smartdatamodels.org/venus",  
            "email": "venus@smartdatamodels.org"  
        },  
        {  
            "title": "Jupiter",  
            "path": "https://smartdatamodels.org/jupiter",  
            "email": "jupiter@smartdatamodels.org"  
        }  
    ],  
    "title": "The Solar System",  
    "@context": [  
        "https://smartdatamodels.org/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.FrictionlessData/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### DataResourceFrictionlessData NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 DataResourceFrictionlessData의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:dataresource:AECS:1234",  
    "type": "DataResourceFrictionlessData",  
    "bytes": {  
        "type": "Property",  
        "value": 2082  
    },  
    "data": {  
        "type": "Property",  
        "value": [  
            {},  
            {}  
        ]  
    },  
    "description": {  
        "type": "Property",  
        "value": "My favourite data about the solar system."  
    },  
    "encoding": {  
        "type": "Property",  
        "value": "utf-8"  
    },  
    "format": {  
        "type": "Property",  
        "value": "csv"  
    },  
    "hash": {  
        "type": "Property",  
        "value": "SHA256:5262f12512590031bbcc9a430452bfd75c2791ad6771320bb4b5728bfb78c4d0"  
    },  
    "homepage": {  
        "type": "Property",  
        "value": "https://smartdatamodels.org"  
    },  
    "licenses": {  
        "type": "Property",  
        "value": [  
            {  
                "name": "CC-BY",  
                "title": "creative commons attribution",  
                "path": "https://creativecommons.org/licenses/by/4.0/deed.en"  
            },  
            {  
                "name": "odc-pddl-1.0",  
                "path": "http://opendatacommons.org/licenses/pddl/",  
                "title": "Open Data Commons Public Domain Dedication and License v1.0"  
            }  
        ]  
    },  
    "mediatype": {  
        "type": "Property",  
        "value": "text/csv"  
    },  
    "name": {  
        "type": "Property",  
        "value": "solar-system"  
    },  
    "path": {  
        "type": "Property",  
        "value": [  
            "http://example.com/solar-system.csv"  
        ]  
    },  
    "profile": {  
        "type": "Property",  
        "value": "tabular-data-package"  
    },  
    "schema": {  
        "type": "Property",  
        "value": {}  
    },  
    "sources": {  
        "type": "Property",  
        "value": [  
            {  
                "title": "Venus",  
                "path": "https://smartdatamodels.org/venus",  
                "email": "venus@smartdatamodels.org"  
            },  
            {  
                "title": "Jupiter",  
                "path": "https://smartdatamodels.org/jupiter",  
                "email": "jupiter@smartdatamodels.org"  
            }  
        ]  
    },  
    "title": {  
        "type": "Property",  
        "value": "The Solar System"  
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
