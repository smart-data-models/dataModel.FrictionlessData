<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : DataResourceFrictionlessData  
=====================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/DataResourceFrictionlessData/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Ressource de données converties pour l'initiative Smart Data Models à partir des données originales frictionless**.  
version : 0.0.3  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `bytes[number]`: Octets. La taille de cette ressource en octets  - `data[array]`: Données. Données en ligne pour cette ressource  - `description[string]`: Description. Une description textuelle. Le format Markdown est encouragé  - `encoding[string]`: Encodage. Le codage du fichier de cette ressource  - `format[string]`: Format. Les formats "csv", "xls" et "json" sont des exemples de formats courants. Le format de fichier de cette ressource  - `hash[string]`: Hash. Le hachage MD5 de cette ressource. Indiquer d'autres algorithmes de hachage avec le format {algorithme}:{hash}.  - `homepage[string]`: Page d'accueil. La page d'accueil sur le web qui est liée à ce paquet de données.  - `id[*]`: Identifiant unique de l'entité  - `licenses[array]`: Licences. Cette propriété n'est pas juridiquement contraignante et ne garantit pas que le paquet est sous licence selon les termes définis ici. La (les) licence(s) sous laquelle (lesquelles) la ressource est publiée  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `mediatype[string]`: Type de média. Le type de média de cette ressource. Il peut s'agir de n'importe quel type de média valide répertorié par l'[IANA] (https://www.iana.org/assignments/media-types/media-types.xhtml).  - `name[string]`: Nom. Il s'agit idéalement d'un nom utilisable en url et lisible par l'homme. Le nom "DEVRAIT" être invariant, c'est-à-dire qu'il "NE DEVRAIT PAS" changer lorsque son descripteur parent est mis à jour. Une chaîne d'identification. Les caractères minuscules avec '.', '_', '-' et '/' sont autorisés.  - `path[array]`: Chemin d'accès. La valeur déréférencée de chaque source de données référencée dans "path" "DOIT" correspondre à une représentation native déréférencée des données décrites par la ressource. Par exemple, dans une ressource de données *Tabular*, cela signifie que la valeur déréférencée de "path" "DOIT" être un tableau. Une référence aux données de cette ressource, sous la forme d'un chemin d'accès en tant que chaîne de caractères ou d'un tableau de chemins d'accès en tant que chaînes de caractères. d'URI valides  - `profile[string]`: Profil. Chaque descripteur de paquet et de ressource a un profil. Le profil par défaut, si aucun n'est déclaré, est "data-package" pour les paquets et "data-resource" pour les ressources. Le profil de ce descripteur  - `schema[object]`: Schéma. Un schéma pour cette ressource  - `sources[array]`: Sources. . Les sources brutes de cette ressource  - `title[string]`: Titre. Un titre lisible par l'homme  - `type[string]`: Type d'entité NGSI. Il doit s'agir de DataResourceFrictionlessData.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `name`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Ce modèle de données provient des données frictionless originales que l'on peut trouver à l'adresse https://frictionlessdata.io/. Il y a quelques changements. 1) l'id et le type ont été rendus obligatoires comme l'exige la norme NGSI-LD 2) la structure du schéma json a été adaptée au format officiel des modèles de données intelligents. Voir le manuel de contribution [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual). Afin de le rendre compatible, la propriété des données et la propriété de la source ont été définies comme un tableau d'objets. Le type a également été inclus.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### DataResourceFrictionlessData Valeurs clés NGSI-v2 Exemple  
Voici un exemple de DataResourceFrictionlessData au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
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
</details>  
#### DataResourceFrictionlessData NGSI-v2 normalisé Exemple  
Voici un exemple de DataResourceFrictionlessData au format JSON-LD tel que normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### DataResourceFrictionlessData Valeurs clés NGSI-LD Exemple  
Voici un exemple de DataResourceFrictionlessData au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### DataResourceFrictionlessData NGSI-LD normalisé Exemple  
Voici un exemple de DataResourceFrictionlessData au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
