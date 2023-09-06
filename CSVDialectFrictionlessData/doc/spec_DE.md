<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: CSVDialectFrictionlessData  
===================================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/CSVDialectFrictionlessData/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Der CSV-Dialekt-Deskriptor, der für die Initiative "Intelligente Datenmodelle" aus den ursprünglichen reibungslosen Daten konvertiert wurde**  
Version: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `caseSensitiveHeader[boolean]`: Groß- und Kleinschreibung in der Kopfzeile. Die Verwendung von Groß- und Kleinschreibung in CSV-Quelldateien ist nicht immer eine bewusste Entscheidung. Soll zum Beispiel 'CAT' und 'Cat' als gleichbedeutend angesehen werden. Gibt an, ob die Groß-/Kleinschreibung von Kopfzeilen sinnvoll ist  - `commentChar[string]`: Kommentarzeichen. Legt fest, dass jede Zeile, die mit dieser einstelligen Zeichenfolge beginnt, ohne vorangestelltes Leerzeichen, dazu führt, dass die gesamte Zeile ignoriert wird  - `csvddfVersion[number]`: CSV Dialect Schema-Version. Eine Zahl zur Angabe der Schemaversion von CSV Dialect. Version 1.0 trug den Namen CSV Dialect Description Format und verwendete andere Feldnamen  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `delimiter[string]`: Begrenzungszeichen. Eine Zeichenfolge, die als Feldtrennzeichen verwendet wird  - `description[string]`: Eine Beschreibung dieses Artikels  - `doubleQuote[boolean]`: Doppelte Anführungszeichen. Wenn Doppelte Anführungszeichen auf true gesetzt sind, müssen zwei aufeinander folgende Anführungszeichen als eines interpretiert werden. Legt die Behandlung von Anführungszeichen innerhalb von Feldern fest  - `escapeChar[string]`: Escape-Zeichen. Gibt eine einstellige Zeichenfolge an, die als Escape-Zeichen verwendet werden soll  - `header[boolean]`: Kopfzeile. Gibt an, ob die Datei eine Kopfzeile enthält, immer als erste Zeile in der Datei  - `id[*]`: Eindeutiger Bezeichner der Entität  - `lineTerminator[string]`: Zeilenabschlusszeichen. Gibt die Zeichenfolge an, die zum Beenden von Zeilen verwendet werden muss  - `name[string]`: Der Name dieses Artikels  - `nullSequence[string]`: Null-Sequenz. Gibt die Nullsequenz an, z. B. \ und dann 'N'.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `quoteChar[string]`: Anführungszeichen. Gibt eine einstellige Zeichenfolge an, die als Anführungszeichen verwendet werden soll  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `skipInitialSpace[boolean]`: Anfängliches Leerzeichen überspringen. Gibt die Interpretation von Leerzeichen unmittelbar nach einem Begrenzungszeichen an. Bei false werden Leerzeichen unmittelbar nach einem Begrenzungszeichen als Teil des nachfolgenden Feldes behandelt  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: Es muss CSVDialectFrictionlessData sein. NGSI-Entitätstyp  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `delimiter`  - `doubleQuote`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Dieses Datenmodell stammt von den ursprünglichen reibungslosen Daten, die unter https://frictionlessdata.io/ zu finden sind. Es gibt einige kleinere Änderungen. 1) id und type wurden obligatorisch gemacht 2) die Struktur des json-Schemas wurde an das offizielle Format der Smart Data Models angepasst. Siehe Beitrag Handbuch [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual). 3) Einige zusätzliche Eigenschaften wurden aus Gründen der Kompatibilität hinzugefügt  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### CSVDialectFrictionlessData NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein CSVDialectFrictionlessData im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### CSVDialectFrictionlessData NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein CSVDialectFrictionlessData im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### CSVDialectFrictionlessData NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein CSVDialectFrictionlessData im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### CSVDialectFrictionlessData NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein CSVDialectFrictionlessData im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
