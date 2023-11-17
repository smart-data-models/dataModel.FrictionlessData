<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティDataPackageFrictionlessData    
=================================<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/DataPackageFrictionlessData/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな説明**データパッケージは、データへのアクセスと配信のためのシンプルな仕様です。スマートデータモデル構想のために、オリジナルのフリクションレスデータから変換されました。    
バージョン: 0.0.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `contributors[array]`: 貢献者この記述子の貢献者  - `created[string]`: 作成される。datetimeは、[RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6)に記述されているdatetimeの文字列フォーマットに準拠しなければならない。この記述子が作成された日時。  - `description[string]`: 説明.テキストの説明.Markdownを推奨します。  - `homepage[string]`: ホームページ..このデータパッケージに関連するウェブ上のホームページ  - `id[string]`: ID。データパッケージの一般的な使用パターンは、システムやプラットフォームの範囲内でのパッケージングフォーマットである。このような場合、既存のパッケージを更新するような一般的なデータ操作のワークフローでは、パッケージの一意な識別子が望まれる。仕様のレベルでは、グローバルな一意性を検証することはできないが、`id` プロパティを使用するコンシューマは、識別子がグローバルに一意であることを保証しなければならない（MUST）。グローバルに一意である識別子のために予約されたプロパティである。一意である識別子の例としては、UUIDやDOIがある。  - `image[string]`: イメージ.このパッケージを表す画像  - `keywords[array]`: キーワード.このパッケージを説明するキーワードのリスト  - `licenses[array]`: ライセンスこのプロパティは法的拘束力を持たず、パッケージがここで定義された条項の下でライセンスされていることを保証するものではありません。このパッケージが公開されているライセンスは以下の通りです。  - `name[string]`: 名前。これは理想的にはurlで使用可能で、人間が読める名前である。名前 `SHOULD` は不変であるべきであり、親ディスクリプタが更新されたときに `SHOULD NOT` 変更されるべきではないことを意味する。識別子文字列。.`、`_`、`-`、`/` の小文字が使用できる。  - `profile[string]`: プロファイル。すべての Package と Resource 記述子はプロファイルを持ちます。デフォルトのプロファイルは、何も宣言されていない場合、Packageでは `data-package`、Resourceでは `data-resource` です。この記述子のプロファイル  - `resources[array]`: データリソース。それぞれが[Data Resource](/data-resource/)仕様に準拠している。  - `sources[array]`: 情報源この資料の生の情報源  - `title[string]`: タイトル.人間が読めるタイトル  - `type[string]`: DataPackageFrictionlessData でなければならない。NGSIエンティティタイプ  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `id`  - `resources`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
このデータモデルは、https://frictionlessdata.io/ にあるオリジナルのフリクションレス・データから来ている。いくつかの変更点がある。1)idとtypeが必須になりました。 2)jsonスキーマの構造がスマートデータモデルの公式フォーマットに合わせられました。貢献マニュアル[https://bit.ly/contribution_manual](https://bit.ly/contribution_manual)を参照してください。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
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
## ペイロードの例    
#### DataPackageFrictionlessData NGSI-v2 キー値の例    
以下はDataPackageFrictionlessDataをJSON-LD形式でkey-valuesとした例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。    
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
#### DataPackageFrictionlessData NGSI-v2 正規化例    
以下は、正規化されたJSON-LD形式のDataPackageFrictionlessDataの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "uri:ngsi-ld:datapackage:001",  
  "type": "DataPackageFrictionlessData",  
  "name": {  
    "type": "Text",  
    "value": "cpi"  
  },  
  "title": {  
    "type": "Text",  
    "value": "Annual Consumer Price Index (CPI)"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Annual Consumer Price Index (CPI) for most countries in the world. Reference year is 2005."  
  },  
  "profile": {  
    "type": "Text",  
    "value": "tabular-data-package"  
  },  
  "licenses": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "name": "CC-BY-4.0",  
        "title": "Creative Commons Attribution 4.0",  
        "path": "https://creativecommons.org/licenses/by/4.0/"  
      }  
    ]  
  },  
  "keywords": {  
    "type": "StructuredValue",  
    "value": [  
      "CPI",  
      "World",  
      "Consumer Price Index",  
      "Annual Data",  
      "The World Bank"  
    ]  
  },  
  "version": {  
    "type": "Text",  
    "value": "2.0.0"  
  },  
  "sources": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "title": "The World Bank",  
        "path": "http://data.worldbank.org/indicator/FP.CPI.TOTL"  
      }  
    ]  
  },  
  "resources": {  
    "type": "StructuredValue",  
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
#### DataPackageFrictionlessData NGSI-LD キー値の例    
以下はDataPackageFrictionlessDataをJSON-LD形式でkey-valuesとした例である。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。    
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
#### DataPackageFrictionlessData NGSI-LD 正規化例    
以下は、正規化されたJSON-LD形式のDataPackageFrictionlessDataの例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
