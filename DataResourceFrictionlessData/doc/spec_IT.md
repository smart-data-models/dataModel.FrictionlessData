Entità: DataResourceFrictionlessData  
====================================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/DataResourceFrictionlessData/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Risorsa di dati.Convertito per l'iniziativa Smart Data Models da dati originali senza attrito**  
versione: 0.0.1  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `bytes`: Bytes. La dimensione di questa risorsa in byte  - `data`: Dati. Dati in linea per questa risorsa  - `description`: Descrizione. Una descrizione testuale. Markdown è incoraggiato  - `encoding`: Codifica. La codifica del file di questa risorsa  - `format`: Formato. 'csv', 'xls', 'json' sono esempi di formati comuni. Il formato del file di questa risorsa  - `hash`: Hash. L'hash MD5 di questa risorsa. Indica altri algoritmi di hashing con il formato {algoritmo}:{hash}  - `homepage`: Home Page. La home sul web che si riferisce a questo pacchetto di dati  - `id`: Identificatore unico dell'entità  - `licenses`: Licenze. Questa proprietà non è legalmente vincolante e non garantisce che il pacchetto sia concesso in licenza nei termini qui definiti. La licenza o le licenze sotto le quali la risorsa è pubblicata  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `mediatype`: Tipo di media. Il tipo di media di questa risorsa. Può essere qualsiasi tipo di media valido elencato con [IANA](https://www.iana.org/assignments/media-types/media-types.xhtml)  - `name`: Nome. Questo è idealmente un nome utilizzabile da url e leggibile dall'uomo. Il nome "DOVREBBE" essere invariante, cioè "NON DOVREBBE" cambiare quando il suo descrittore padre viene aggiornato. Una stringa identificativa. Sono ammessi caratteri minuscoli con '.', '_', '-' e '/'.  - `path`: Percorso. Il valore dereferenziato di ogni fonte di dati referenziata in 'path' 'DEVE' essere commisurato ad una rappresentazione nativa e dereferenziata dei dati che la risorsa descrive. Per esempio, in una risorsa di dati *Tabular*, questo significa che il valore dereferenziato di "path" "DEVE" essere un array. Un riferimento ai dati per questa risorsa, sia come un percorso come stringa, o un array di percorsi come stringhe. di URI validi  - `profile`: Profilo. Ogni descrittore di Pacchetto e Risorsa ha un profilo. Il profilo predefinito, se non è dichiarato, è "data-package" per Package e "data-resource" per Resource. Il profilo di questo descrittore  - `schema`: Schema. Uno schema per questa risorsa  - `sources`: Fonti. . Le fonti grezze per questa risorsa  - `title`: Titolo. Un titolo leggibile dall'uomo  - `type`: Tipo di entità NGSI - deve essere DataResourceFrictionlessData    
Proprietà richieste  
- `id`  - `name`  - `type`    
Questo modello di dati proviene dai dati originali di frictionless che possono essere trovati su https://frictionlessdata.io/. Ci sono un paio di cambiamenti. 1) id e type sono stati resi obbligatori come richiesto dallo standard NGSI-LD 2) la struttura dello schema json è stata adattata al formato ufficiale degli Smart Data Models. Vedere il manuale dei contributi [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual). Per renderlo compatibile, la proprietà dati e la proprietà sorgente sono state definite come un array di oggetti. Anche il tipo è stato incluso.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DataResourceFrictionlessData:    
  description: 'Data Resource.Converted for Smart Data Models initiative from original frictionless data'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    bytes:    
      description: 'Bytes. The size of this resource in bytes'    
      type: integer    
      x-ngsi:    
        type: Property    
    data:    
      description: 'Data. Inline data for this resource'    
      items:    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    description:    
      description: 'Description. A text description. Markdown is encouraged'    
      type: string    
      x-ngsi:    
        type: Property    
    encoding:    
      description: 'Encoding. The file encoding of this resource'    
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
      description: 'Home Page. The home on the web that is related to this data package'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
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
    licenses:    
      description: 'Licenses. This property is not legally binding and does not guarantee that the package is licensed under the terms defined herein. The license(s) under which the resource is published'    
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
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
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
      description: 'Schema. A schema for this resource'    
      type: object    
      x-ngsi:    
        type: Property    
    sources:    
      description: 'Sources. . The raw sources for this resource'    
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
      description: 'Title. A human-readable title'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity type· It has to be DataResourceFrictionlessData'    
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
  version: 0.0.1    
```  
</details>    
## Esempio di payloads  
#### DataResourceFrictionlessData NGSI-v2 valori chiave Esempio  
Ecco un esempio di un DataResourceFrictionlessData in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
  "schema": {  
  },  
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
#### DataResourceFrictionlessData NGSI-v2 normalizzato Esempio  
Ecco un esempio di un DataResourceFrictionlessData in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:dataresource:AECS:1234",  
  "type": "DataResourceFrictionlessData",  
  "bytes": {  
    "type": "number",  
    "value": 2082  
  },  
  "data": {  
    "type": "array",  
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
    "type": "array",  
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
    "type": "array",  
    "value": [  
      "http://example.com/solar-system.csv"  
    ]  
  },  
  "profile": {  
    "type": "Text",  
    "value": "tabular-data-package"  
  },  
  "schema": {  
    "type": "object",  
    "value": {}  
  },  
  "sources": {  
    "type": "array",  
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
#### DataResourceFrictionlessData Valori chiave NGSI-LD Esempio  
Ecco un esempio di un DataResourceFrictionlessData in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
  "schema": {  
  },  
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
  "@context": "https://smartdatamodels.org/context.jsonld"  
}  
```  
#### DataResourceFrictionlessData NGSI-LD normalizzato Esempio  
Ecco un esempio di un DataResourceFrictionlessData in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
