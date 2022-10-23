<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: PacchettoDatiSenzaFrequenzeDati  
=======================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/DataPackageFrictionlessData/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Pacchetto di dati è una semplice specifica per l'accesso e la consegna dei dati.Convertito per l'iniziativa Smart Data Models da dati originali senza attrito**  
versione: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `contributors[array]`: Collaboratori. . I collaboratori di questo descrittore  - `created[string]`: Creato. Il datetime deve essere conforme ai formati di stringa per il datetime descritti in [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6). Il datetime in cui è stato creato questo descrittore  - `description[string]`: Descrizione. . Una descrizione testuale. Si consiglia l'uso di Markdown  - `homepage[string]`: Pagina iniziale. . La pagina web relativa a questo pacchetto di dati.  - `id[string]`: ID. Un modello di utilizzo comune dei pacchetti di dati è il formato di impacchettamento all'interno di un sistema o di una piattaforma. In questi casi, si desidera un identificatore univoco per un pacchetto per i flussi di lavoro comuni di gestione dei dati, come l'aggiornamento di un pacchetto esistente. Sebbene a livello di specifica non sia possibile convalidare l'unicità globale, i consumatori che utilizzano la proprietà `id` devono garantire che gli identificatori siano unici a livello globale. Proprietà riservata agli identificatori globalmente unici. Esempi di identificatori unici sono gli UUID e i DOI.  - `image[string]`: Immagine. . Un'immagine per rappresentare questo pacchetto  - `keywords[array]`: Parole chiave. . Un elenco di parole chiave che descrivono questo pacchetto  - `licenses[array]`: Licenze. Questa proprietà non è legalmente vincolante e non garantisce che il pacchetto sia concesso in licenza secondo i termini qui definiti. La licenza (o le licenze) con cui questo pacchetto è pubblicato  - `name[string]`: Nome. Idealmente si tratta di un nome utilizzabile via url e leggibile dall'uomo. Il nome `DOVREBBE' essere invariante, cioè NON dovrebbe cambiare quando il descrittore padre viene aggiornato. Una stringa identificativa. Sono ammessi i caratteri minuscoli con `.`, `_`, `-` e `/`.  - `profile[string]`: Profilo. Ogni descrittore di pacchetto e risorsa ha un profilo. Il profilo predefinito, se non viene dichiarato, è `data-package` per i pacchetti e `data-resource` per le risorse. Il profilo di questo descrittore  - `resources[array]`: Risorse dati. . Un `array` di oggetti Data Resource, ciascuno conforme alla specifica [Data Resource](/data-resource/).  - `sources[array]`: Fonti. . Le fonti grezze per questa risorsa  - `title[string]`: Titolo. . Un titolo leggibile dall'uomo  - `type[string]`: Deve essere DataPackageFrictionlessData. Tipo di entità NGSI  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `resources`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Questo modello di dati deriva dai dati originali di frictionless che si possono trovare su https://frictionlessdata.io/. Ci sono un paio di modifiche. 1) id e tipo sono stati resi obbligatori 2) la struttura dello schema json è stata adattata al formato ufficiale degli Smart Data Models. Vedere il manuale del contributo [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.FrictionlessData/blob/master/DataPackageFrictionlessData/LICENSE.md    
  x-model-schema: ""    
  x-model-tags: SDG    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### DataPackageFrictionlessData Valori chiave NGSI-v2 Esempio  
Ecco un esempio di DataPackageFrictionlessData in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### DataPackageFrictionlessData NGSI-v2 normalizzato Esempio  
Ecco un esempio di DataPackageFrictionlessData in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### DataPackageFrictionlessData Valori chiave NGSI-LD Esempio  
Ecco un esempio di DataPackageFrictionlessData in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### DataPackageFrictionlessData NGSI-LD normalizzato Esempio  
Ecco un esempio di DataPackageFrictionlessData in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
