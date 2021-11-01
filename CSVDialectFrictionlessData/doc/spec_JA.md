エンティティCSVDialectFrictionlessData  
================================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/CSVDialectFrictionlessData/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**オリジナルのFrictionless DataからSmart Data Modelsイニシアティブのために変換されたものです。  
バージョン: 0.0.1  

## プロパティのリスト  

- `alternateName`: このアイテムの別称  - `caseSensitiveHeader`: 大文字小文字を区別するヘッダー。ソースCSVファイルでの大文字・小文字の使い分けは、必ずしも意図的なものではありません。例えば、「CAT」と「猫」は同じ意味と考えるべきでしょう。ヘッダーの大文字小文字に意味があるかどうかを指定する  - `commentChar`: コメント文字。この1文字の文字列で始まる行は、先行するホワイトスペースを除いて、その行全体が無視されることを指定します。  - `csvddfVersion`: CSV Dialectのスキーマバージョン。CSV Dialectのスキーマバージョンを示す番号です。バージョン1.0はCSV Dialect Description Formatという名前で、異なるフィールド名を使用していました。  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `delimiter`: デリミター。フィールドの区切り文字として使用する文字列  - `description`: このアイテムの説明  - `doubleQuote`: ダブルクォートDouble Quoteがtrueに設定されている場合、2つの連続した引用符は1つとして解釈されなければなりません。フィールド内の引用符の扱いを指定します。  - `escapeChar`: エスケープ文字。エスケープ文字として使用する1文字の文字列を指定します。  - `header`: ヘッダーファイルにヘッダー行を含めるかどうかを指定します。  - `id`: エンティティのユニークな識別子  - `lineTerminator`: 行終端記号。行を終了させるために使用しなければならない文字列を指定します。  - `name`: このアイテムの名前です。  - `nullSequence`: Null Sequence。Null Sequenceを指定します。例えば、「\」の後に「N」を指定します。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `quoteChar`: 引用文字。クォート文字として使用する1文字の文字列を指定します。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `skipInitialSpace`: 最初のスペースをスキップする。区切り文字の直後にあるホワイトスペースの解釈を指定します。falseの場合、デリミタ直後のホワイトスペースは、後続のフィールドの一部として扱われます。  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type`: CSVDialectFrictionlessDataである必要があります。NGSIエンティティタイプ    
必須項目  
- `delimiter`  - `doubleQuote`  - `id`  - `type`    
このデータモデルは、https://frictionlessdata.io/ に掲載されているオリジナルのフリクションレスデータから来ています。いくつかのマイナーな変更点があります。1)idとtypeが必須になった 2)jsonスキーマの構造がスマートデータモデルの公式フォーマットに合わせられた。コントリビューションマニュアル[https://bit.ly/contribution_manual](https://bit.ly/contribution_manual)を参照してください。3) 互換性のため、いくつかのプロパティが追加されました。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CSVDialectFrictionlessData:    
  description: 'The CSV dialect descriptor.Converted for Smart Data Models initiative from original frictionless data'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
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
      description: 'CSV Dialect schema version. A number to indicate the schema version of CSV Dialect. Version 1.0 was named CSV Dialect Description Format and used different field names'    
      type: number    
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
    delimiter:    
      description: 'Delimiter. A character sequence to use as the field separator'    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    doubleQuote:    
      description: 'Double Quote. If Double Quote is set to true, two consecutive quotes must be interpreted as one. Specifies the handling of quotes inside fields'    
      type: boolean    
      x-ngsi:    
        type: Property    
    escapeChar:    
      description: 'Escape Character. Specifies a one-character string to use as the escape character'    
      type: string    
      x-ngsi:    
        type: Property    
    header:    
      description: 'Header. Specifies if the file includes a header row, always as the first row in the file'    
      type: boolean    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &csvdialectfrictionlessdata_-_properties_-_owner_-_items_-_anyof    
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
    lineTerminator:    
      description: 'Line Terminator. Specifies the character sequence that must be used to terminate rows'    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    nullSequence:    
      description: 'Null Sequence. Specifies the null sequence, for example, \ and then ''N'''    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *csvdialectfrictionlessdata_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    quoteChar:    
      description: 'Quote Character. Specifies a one-character string to use as the quoting character'    
      type: string    
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
    skipInitialSpace:    
      description: 'Skip Initial Space. Specifies the interpretation of whitespace immediately following a delimiter. If false, whitespace immediately after a delimiter should be treated as part of the subsequent field'    
      type: boolean    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'It has to be CSVDialectFrictionlessData. NGSI entity type'    
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
  version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### CSVDialectFrictionlessData NGSI-v2 key-values 例  
CSVDialectFrictionlessDataをJSON-LD形式でkey-valuesにした例を示します。これは、`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
  "delimiter": ";",  
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
#### CSVDialectFrictionlessData NGSI-v2 正規化された例。  
CSVDialectFrictionlessDataをJSON-LD形式で正規化した例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "value": ";"  
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
#### CSVDialectFrictionlessData NGSI-LDのキーバリューの例  
CSVDialectFrictionlessDataをkey-valuesとしてJSON-LD形式にした例を示します。これは、`options=keyValues`を使用した場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
  "delimiter": ";",  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### CSVDialectFrictionlessData NGSI-LDの正規化例  
CSVDialectFrictionlessDataをJSON-LD形式で正規化した例を示します。これはオプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "value": ";"  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
