<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: DataPackageFrictionlessData    
====================================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/DataPackageFrictionlessData/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Datenpaket ist eine einfache Spezifikation für den Zugang zu und die Bereitstellung von Daten, die für die Initiative "Smart Data Models" aus den ursprünglichen friktionsfreien Daten umgewandelt wurde**    
Version: 0.0.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `contributors[array]`: Mitwirkende. Die Mitwirkenden an diesem Deskriptor  - `created[string]`: Erstellt. Die Datetime muss den in [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6) beschriebenen String-Formaten für datetime entsprechen. Der Zeitpunkt, zu dem dieser Deskriptor erstellt wurde  - `description[string]`: Beschreibung. . Eine Textbeschreibung. Markdown wird empfohlen  - `homepage[string]`: Home Page. . Die Homepage im Web, die sich auf dieses Datenpaket bezieht  - `id[string]`: ID. Ein gängiges Verwendungsmuster für Datenpakete ist die Verwendung als Paketierungsformat innerhalb der Grenzen eines Systems oder einer Plattform. In diesen Fällen ist ein eindeutiger Identifikator für ein Paket für allgemeine Datenverarbeitungsabläufe, wie z. B. die Aktualisierung eines bestehenden Pakets, erwünscht. Während auf der Ebene der Spezifikation die globale Eindeutigkeit nicht validiert werden kann, müssen Verbraucher, die die Eigenschaft `id` verwenden, sicherstellen, dass die Bezeichner global eindeutig sind. Eine Eigenschaft, die für global eindeutige Bezeichner reserviert ist. Beispiele für eindeutige Bezeichner sind UUIDs und DOIs.  - `image[string]`: Bild. . Ein Bild zur Darstellung dieses Pakets  - `keywords[array]`: Schlüsselwörter. . Eine Liste von Schlüsselwörtern, die dieses Paket beschreiben  - `licenses[array]`: Lizenzen. Diese Eigenschaft ist nicht rechtsverbindlich und garantiert nicht, dass das Paket unter den hier definierten Bedingungen lizenziert ist. Die Lizenz(en), unter denen dieses Paket veröffentlicht wird  - `name[string]`: Name. Dies ist idealerweise ein url-verwendbarer und von Menschen lesbarer Name. Der Name `SOLLTE` invariant sein, d.h. er `SOLLTE` sich NICHT ändern, wenn der übergeordnete Deskriptor aktualisiert wird. Ein Bezeichner-String. Kleinbuchstaben mit `.`, `_`, `-` und `/` sind erlaubt.  - `profile[string]`: Profil. Jeder Package- und Resource-Deskriptor hat ein Profil. Das Standardprofil, wenn keines deklariert ist, ist `data-package` für Package und `data-resource` für Resource. Das Profil für diesen Deskriptor  - `resources[array]`: Daten-Ressourcen. Ein "Array" von Datenressourcen-Objekten, die jeweils der Spezifikation [Datenressource](/data-resource/) entsprechen  - `sources[array]`: Quellen. Die Rohquellen für diese Ressource  - `title[string]`: Titel. . Ein von Menschen lesbarer Titel  - `type[string]`: Es muss DataPackageFrictionlessData sein. NGSI-Entitätstyp  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `id`  - `resources`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Dieses Datenmodell stammt von den ursprünglichen reibungslosen Daten, die unter https://frictionlessdata.io/ zu finden sind. Es gibt eine Reihe von Änderungen. 1) id und type wurden obligatorisch gemacht 2) die Struktur des json Schemas wurde an das offizielle Format der Smart Data Models angepasst. Siehe Beitrag Handbuch [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
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
## Beispiel-Nutzlasten    
#### DataPackageFrictionlessData NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für ein DataPackageFrictionlessData im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### DataPackageFrictionlessData NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für ein DataPackageFrictionlessData im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
#### DataPackageFrictionlessData NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für ein DataPackageFrictionlessData im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### DataPackageFrictionlessData NGSI-LD normalized Beispiel    
Hier ist ein Beispiel für ein DataPackageFrictionlessData im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
