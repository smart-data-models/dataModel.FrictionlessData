<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: TableSchemaFrictionlessData    
====================================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/TableSchemaFrictionlessData/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Ein Tabellenschema für diese Ressource, das mit der Spezifikation für Tabellenschemata übereinstimmt. Konvertiert für die Initiative Smart Data Models aus den ursprünglichen friktionsfreien Daten**    
Version: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `fields[array]`: Ein Array von Tabellenschema-Feldobjekten  - `foreignKeys[array]`:   - `id[*]`: Eindeutiger Bezeichner der Entität  - `missingValues[array]`: Viele Datensätze enthalten fehlende Werte, entweder weil ein Wert nicht erfasst wurde oder weil er nie existierte. Fehlende Werte können einfach dadurch angezeigt werden, dass der Wert leer ist, in anderen Fällen kann ein spezieller Wert verwendet worden sein, z. B. "-", "NaN", "0", "-9999" usw. Die Eigenschaft "missingValues" bietet eine Möglichkeit, anzugeben, dass diese Werte als gleichwertig mit null interpretiert werden sollten. Bei den "missingValues" handelt es sich um Strings und nicht um den Datentyp des jeweiligen Feldes. Dies ermöglicht einen Vergleich vor dem Casting und die Angabe fehlender Werte in Feldern, die nicht zu ihrem Typ gehören, z. B. in einem "Zahlen"-Feld, in dem fehlende Werte durch "-" angezeigt werden. Für Felder vom Typ "String" gibt es keinen Standardwert für "missingValue" (für String-Felder ist die leere Zeichenkette '' ein gültiger Wert und muss nicht null anzeigen). Werte, die, wenn sie in der Quelle angetroffen werden, als "null", "nicht vorhanden" oder "leer" betrachtet werden sollten  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `primaryKey[array]`: Der Feldname im primaryKey 'MUSS' eindeutig sein und 'MUSS' einem Feldnamen in der zugehörigen Tabelle entsprechen. Es ist akzeptabel, ein Array mit einem einzigen Wert zu haben, das anzeigt, dass der Wert eines einzelnen Feldes der Primärschlüssel ist. Ein Primärschlüssel ist ein Feldname oder ein Array von Feldnamen, dessen Werte jede Zeile in der Tabelle eindeutig identifizieren "MÜSSEN".  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: muss es TableSchemaFrictionlessData sein. NGSI-Entitätstyp  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `fields`  - `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Dieses Datenmodell stammt von den ursprünglichen reibungslosen Daten, die unter https://frictionlessdata.io/ zu finden sind. Es gibt mehrere Änderungen. 1) id und type wurden obligatorisch gemacht, solange sie für den NGSI-Standard obligatorisch sind. 2) Die Struktur des json-Schemas wurde an das offizielle Format der Smart Data Models angepasst. Siehe Beitrag Handbuch [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
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
## Beispiel-Nutzlasten    
#### TableSchemaFrictionlessData NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für ein TableSchemaFrictionlessData im JSON-LD Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### TableSchemaFrictionlessData NGSI-v2 normalized Beispiel    
Hier ist ein Beispiel für ein TableSchemaFrictionlessData im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:TableSchemaFrictionlessData:XVFE:0034",  
  "type": "TableSchemaFrictionlessData",  
  "fields": {  
    "type": "StructuredValue",  
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
    "type": "StructuredValue",  
    "value": [  
      "name"  
    ]  
  }  
}  
```  
</details>    
#### TableSchemaFrictionlessData NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für ein TableSchemaFrictionlessData im JSON-LD Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### TableSchemaFrictionlessData NGSI-LD normalized Beispiel    
Hier ist ein Beispiel für ein TableSchemaFrictionlessData im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
