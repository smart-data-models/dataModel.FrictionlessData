Entität: DataResourceFrictionlessData  
=====================================









- `id`  



<details><summary><strong>full yaml details</strong></summary>    

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