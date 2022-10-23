<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティTableSchemaFrictionlessData  
=================================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/TableSchemaFrictionlessData/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**テーブルスキーマ仕様に準拠した、このリソースのテーブルスキーマ。オリジナルのフリクションレスデータからスマートデータモデル構想のために変換された**。  
バージョン: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `alternateName[string]`: この項目の別称  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `fields[array]`: テーブルスキーマフィールドオブジェクトの配列  - `foreignKeys[array]`:   - `id[*]`: エンティティの一意な識別子  - `missingValues[array]`: 多くのデータセットでは、値が欠落しています。欠落している値を表すには、単に値が空である場合と '-'、'NaN'、'0'、'-9999' などの特殊な値を使用する場合があります。missingValues' は、特定のフィールドのデータ型ではなく文字列です。これにより、キャストする前に比較したり、フィールドのデータ型とは異なる値が欠落している場合、例えば 'number' フィールドでは '-' で示される値が欠落していることになります。文字列型フィールドの場合、'missingValue' のデフォルト値はありません (文字列フィールドの場合、空文字列 '' は有効な値であり、NULL を示す必要はありません)。ソースで遭遇したときに 'null'、'not present'、または 'blank' 値として考慮される必要がある値  - `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `primaryKey[array]`: primaryKey のフィールド名は一意でなければならず (MUST)、関連するテーブルのフィールド名と 'MUST' 一致しなければならない (訳注: 「一意でなければならない」)。一つの値を持つ配列があってもかまいません。これは、一つのフィールドの値が主キーであることを示すものです。主キーとは、フィールド名またはフィールド名の配列のことで、 その値はテーブルの各行を一意に識別するものでなければなりません (MUST)。  - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type[string]`: は，TableSchemaFrictionlessDataでなければならない。NGSIエンティティタイプ  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `fields`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
このデータモデルは、https://frictionlessdata.io/ にあるオリジナルのfrictionlessデータに由来しています。いくつかの変更点があります。1) id と type は NGSI 標準で必須である限り、必須としました。 2) json スキーマの構造は、Smart Data Models の公式フォーマットに適応させました。寄稿マニュアル[https://bit.ly/contribution_manual](https://bit.ly/contribution_manual)を参照してください。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
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
## ペイロードの例  
#### TableSchemaFrictionlessData NGSI-v2 key-value 例  
ここでは、TableSchemaFrictionlessDataをJSON-LD形式でkey-valueとした場合の例を示す。これは `options=keyValues` を使用した場合に NGSI-v2 と互換性があり、個々のエンティティのコンテキストデータが返される。  
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
#### TableSchemaFrictionlessData NGSI-v2 正規化例  
TableSchemaFrictionlessData を JSON-LD 形式で正規化した例を示す。これはオプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。  
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
#### TableSchemaFrictionlessData NGSI-LD キー値の例  
TableSchemaFrictionlessDataをJSON-LD形式でkey-valueとした例である。これは `options=keyValues` を使用した場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返す。  
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
#### TableSchemaFrictionlessData NGSI-LD 正規化例  
TableSchemaFrictionlessData を JSON-LD 形式で正規化した例を示す。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
