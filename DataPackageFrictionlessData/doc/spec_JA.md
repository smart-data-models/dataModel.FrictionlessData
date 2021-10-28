エンティティDataPackageFrictionlessData  
=================================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/DataPackageFrictionlessData/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**データパッケージは、データへのアクセスと配信のためのシンプルな仕様です。スマートデータモデル構想のために、オリジナルのフリクションレスデータから変換されました。  
バージョン: 0.0.1  

## プロパティのリスト  

- `contributors`: 投稿者.このディスクリプターの貢献者は  - `created`: 作成されます。datetimeは、[RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6)に記載されているdatetimeの文字列フォーマットに準拠しなければならない。この記述子が作成された日時  - `description`: 説明.テキストによる説明。Markdownを推奨します。  - `homepage`: ホームページです。.このデータパッケージに関連するウェブ上のホーム  - `id`: IDです。データパッケージの一般的な使用パターンは、システムやプラットフォームの範囲内でのパッケージフォーマットとしての使用です。このような場合、既存のパッケージを更新するような一般的なデータ処理のワークフローのために、パッケージのためのユニークな識別子が望まれます。仕様のレベルでは、グローバルな一意性を検証することはできませんが、`id` プロパティを使用する消費者は、識別子がグローバルに一意であることを保証しなければなりません（`MUST`）。グローバルにユニークな識別子のために用意されたプロパティです。ユニークな識別子の例としては、UUIDやDOIなどがあります。  - `image`: 画像を表示します。.このパッケージを表現するためのイメージ  - `keywords`: .キーワード.このパッケージを説明するキーワードのリスト  - `licenses`: ライセンスについて本プロパティは法的拘束力を持たず、本パッケージがここで定義された条件でライセンスされていることを保証するものではありません。本パッケージが公開されているライセンス(複数可)  - `name`: 名前です。これは理想的には、URLで使用可能な、人間が読める名前です。名前は `SHOULD` 不変であり、親ディスクリプターが更新されても `SHOULD NOT` 変わらないことを意味します。識別子の文字列です。小文字で `.`, `_`, `-`, `/` が使用できます。  - `profile`: プロファイルすべてのパッケージとリソースの記述子は、プロファイルを持っています。デフォルトのプロファイルは、何も宣言されていなければ、Packageでは`data-package`、Resourceでは`data-resource`です。この記述子のプロファイルは  - `resources`: データリソース..データリソース](/data-resource/)の仕様に準拠したデータリソースオブジェクトの `array` です。  - `sources`: ソース.このリソースの生のソースは  - `title`: タイトルは.人間が読めるタイトル  - `type`: DataPackageFrictionlessDataでなければならない。NGSIエンティティタイプ    
必須項目  
- `id`  - `resources`  - `type`    
このデータモデルは、https://frictionlessdata.io/ に掲載されているオリジナルのフリクションレスデータから来ています。いくつかの変更点があります。1)idとtypeが必須になった 2)jsonスキーマの構造がスマートデータモデルの公式フォーマットに合わせられた。コントリビューションマニュアル[https://bit.ly/contribution_manual](https://bit.ly/contribution_manual)をご覧ください。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DataPackageFrictionlessData:    
  description: 'Data Package is a simple specification for data access and delivery.Converted for Smart Data Models initiative from original frictionless data'    
  properties:    
    contributors:    
      description: 'Contributors. . The contributors to this descriptor'    
      type: array    
      x-ngsi:    
        type: Property    
    created:    
      description: "Created. The datetime must conform to the string formats for datetime as described in [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6). The datetime on which this descriptor was created"    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'Description. . A text description. Markdown is encouraged'    
      type: string    
      x-ngsi:    
        type: Property    
    homepage:    
      description: 'Home Page. . The home on the web that is related to this data package'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      description: 'ID. A common usage pattern for Data Packages is as a packaging format within the bounds of a system or platform. In these cases, a unique identifier for a package is desired for common data handling workflows, such as updating an existing package. While at the level of the specification, global uniqueness cannot be validated, consumers using the `id` property `MUST` ensure identifiers are globally unique. A property reserved for globally unique identifiers. Examples of identifiers that are unique include UUIDs and DOIs'    
      type: string    
      x-ngsi:    
        type: Property    
    image:    
      description: 'Image. . A image to represent this package'    
      type: string    
      x-ngsi:    
        type: Property    
    keywords:    
      description: 'Keywords. . A list of keywords that describe this package'    
      type: array    
      x-ngsi:    
        type: Property    
    licenses:    
      description: 'Licenses. This property is not legally binding and does not guarantee that the package is licensed under the terms defined herein. The license(s) under which this package is published'    
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
      description: 'Data Resources. . An `array` of Data Resource objects, each compliant with the [Data Resource](/data-resource/) specification'    
      type: array    
      x-ngsi:    
        type: Property    
    sources:    
      description: 'Sources. . The raw sources for this resource'    
      type: array    
      x-ngsi:    
        type: Property    
    title:    
      description: 'Title. . A human-readable title'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'It has to be DataPackageFrictionlessData. NGSI entity type'    
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
  version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### DataPackageFrictionlessData NGSI-v2 key-valuesの例。  
ここではDataPackageFrictionlessDataをJSON-LD形式でkey-valuesにした例を紹介します。これは、`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### DataPackageFrictionlessData NGSI-v2 normalized Example  
ここでは、正規化されたJSON-LD形式のDataPackageFrictionlessDataの例を示す。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### DataPackageFrictionlessData NGSI-LD key-valuesの例。  
ここでは、DataPackageFrictionlessDataをJSON-LD形式でkey-valuesにした例を紹介します。これは、`options=keyValues`を使用した場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
  ],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### DataPackageFrictionlessData NGSI-LD normalized Example  
ここでは、正規化されたJSON-LD形式のDataPackageFrictionlessDataの例を示す。これは、オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "uri:ngsi-ld:datapackage:001",  
  "type": "DataPackageFrictionlessData",  
  "name": {  
    "type": "Property",  
    "value": "cpi"  
  },  
  "title": {  
    "type": "Property",  
    "value": "Annual Consumer Price Index (CPI)"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Annual Consumer Price Index (CPI) for most countries in the world. Reference year is 2005."  
  },  
  "profile": {  
    "type": "Property",  
    "value": "tabular-data-package"  
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
  "version": {  
    "type": "Property",  
    "value": "2.0.0"  
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
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
