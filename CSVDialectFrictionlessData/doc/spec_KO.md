<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

===============================
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `alternateName[string]`: 이 항목의 대체 이름  
<!-- 35-RequiredProperties -->

- `delimiter`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

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



<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
