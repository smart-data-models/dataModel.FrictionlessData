<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: DataResourceFrictionlessData    
====================================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/DataResourceFrictionlessData/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Risorsa di dati.Convertita per l'iniziativa Modelli di dati intelligenti da dati originali senza attriti**    
versione: 0.0.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.      
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `bytes[number]`: Byte. La dimensione della risorsa in byte  - `data[array]`: Dati. Dati in linea per questa risorsa  - `description[string]`: Descrizione. Una descrizione testuale. Si consiglia l'uso di Markdown  - `encoding[string]`: Codifica. La codifica del file di questa risorsa  - `format[string]`: Formato. csv", "xls", "json" sono esempi di formati comuni. Il formato del file di questa risorsa  - `hash[string]`: Hash. L'hash MD5 di questa risorsa. Indicare altri algoritmi di hashing con il formato {algoritmo}:{hash}.  - `homepage[string]`: Pagina iniziale. La pagina web relativa a questo pacchetto di dati.  - `id[*]`: Identificatore univoco dell'entità  - `licenses[array]`: Licenze. Questa proprietà non è legalmente vincolante e non garantisce che il pacchetto sia concesso in licenza secondo i termini qui definiti. La licenza o le licenze sotto le quali la risorsa è pubblicata  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `mediatype[string]`: Tipo di supporto. Il tipo di supporto di questa risorsa. Può essere qualsiasi tipo di supporto valido elencato in [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml).  - `name[string]`: Nome. Idealmente, si tratta di un nome utilizzabile tramite url e leggibile dall'uomo. Il nome "DOVREBBE" essere invariante, cioè "NON DOVREBBE" cambiare quando il descrittore padre viene aggiornato. Una stringa identificativa. Sono ammessi i caratteri minuscoli con '.', '_', '-' e '/'.  - `path[array]`: Percorso. Il valore dereferenziato di ciascuna origine dati referenziata in 'percorso' 'DEVE' essere commisurato a una rappresentazione nativa e dereferenziata dei dati che la risorsa descrive. Ad esempio, in una risorsa di dati *Tabular*, ciò significa che il valore dereferenziato di 'path' 'DEVE' essere un array. Un riferimento ai dati di questa risorsa, sia come percorso come stringa, sia come array di percorsi come stringhe. di URI validi  - `profile[string]`: Profilo. Ogni descrittore di pacchetto e di risorsa ha un profilo. Il profilo predefinito, se non viene dichiarato, è "data-package" per i pacchetti e "data-resource" per le risorse. Il profilo di questo descrittore  - `schema[object]`: Schema. Uno schema per questa risorsa  - `sources[array]`: Fonti. . Le fonti grezze per questa risorsa  - `title[string]`: Titolo. Un titolo leggibile dall'uomo  - `type[string]`: Tipo di entità NGSI. Deve essere DataResourceFrictionlessData  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Questo modello di dati proviene dai dati originali di frictionless che si possono trovare su https://frictionlessdata.io/. Ci sono un paio di modifiche. 1) id e tipo sono stati resi obbligatori come richiesto dallo standard NGSI-LD 2) la struttura dello schema json è stata adattata al formato ufficiale degli Smart Data Models. Si veda il manuale del contributo [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual). Per renderla compatibile, la proprietà dei dati e la proprietà della fonte sono state definite come un array di oggetti. È stato incluso anche il tipo.    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
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
## Esempi di payload    
#### DataResourceFrictionlessData Valori chiave NGSI-v2 Esempio    
Ecco un esempio di DataResourceFrictionlessData in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
  "title": "The Solar System"  
}  
```  
</details>    
#### DataResourceFrictionlessData NGSI-v2 normalizzato Esempio    
Ecco un esempio di DataResourceFrictionlessData in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:dataresource:AECS:1234",  
  "type": "DataResourceFrictionlessData",  
  "bytes": {  
    "type": "Number",  
    "value": 2082  
  },  
  "data": {  
    "type": "StructuredValue",  
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
    "type": "StructuredValue",  
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
    "type": "StructuredValue",  
    "value": [  
      "http://example.com/solar-system.csv"  
    ]  
  },  
  "profile": {  
    "type": "Text",  
    "value": "tabular-data-package"  
  },  
  "schema": {  
    "type": "StructuredValue",  
    "value": {}  
  },  
  "sources": {  
    "type": "StructuredValue",  
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
#### DataResourceFrictionlessData Valori chiave NGSI-LD Esempio    
Ecco un esempio di DataResourceFrictionlessData in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
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
#### DataResourceFrictionlessData NGSI-LD normalizzato Esempio    
Ecco un esempio di DataResourceFrictionlessData in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
