<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : DataPackageFrictionlessData    
====================================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/DataPackageFrictionlessData/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Le paquet de données est une spécification simple pour l'accès aux données et leur livraison. Converti pour l'initiative Smart Data Models à partir des données originales frictionless**.    
version : 0.0.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `contributors[array]`: Les contributeurs. Les contributeurs à ce descripteur  - `created[string]`: Créé. L'heure de la date doit être conforme aux formats de chaîne pour l'heure de la date décrits dans [RFC3339] (https://tools.ietf.org/html/rfc3339#section-5.6). Date à laquelle ce descripteur a été créé.  - `description[string]`: Description. . Une description textuelle. Le format Markdown est encouragé  - `homepage[string]`: Page d'accueil. . La page d'accueil sur le web qui est liée à ce paquet de données  - `id[string]`: ID. Les paquets de données sont souvent utilisés comme format d'emballage dans les limites d'un système ou d'une plateforme. Dans ce cas, un identifiant unique pour un paquet est souhaité pour les flux de travail courants de manipulation des données, tels que la mise à jour d'un paquet existant. Bien qu'au niveau de la spécification, l'unicité globale ne puisse pas être validée, les consommateurs utilisant la propriété `id` `MUST` s'assurent que les identifiants sont globalement uniques. Propriété réservée aux identificateurs globalement uniques. Les UUID et les DOI sont des exemples d'identifiants uniques.  - `image[string]`: Image. . Une image pour représenter ce paquet  - `keywords[array]`: Mots clés. . Une liste de mots-clés qui décrivent ce paquet  - `licenses[array]`: Licences. Cette propriété n'est pas juridiquement contraignante et ne garantit pas que le paquet est sous licence selon les termes définis ici. La (les) licence(s) sous laquelle (lesquelles) ce paquet est publié  - `name[string]`: Nom. Il s'agit idéalement d'un nom utilisable en url et lisible par l'homme. Le nom `SHOULD` est invariant, ce qui signifie qu'il `SHOULD` ne doit pas changer lorsque son descripteur parent est mis à jour. Une chaîne d'identification. Les caractères minuscules avec `.`, `_`, `-` et `/` sont autorisés.  - `profile[string]`: Profil. Chaque descripteur de paquetage et de ressource a un profil. Le profil par défaut, si aucun n'est déclaré, est `data-package` pour Package et `data-resource` pour Resource. Le profil de ce descripteur  - `resources[array]`: Ressources de données. Un "tableau" d'objets de ressources de données, chacun conforme à la spécification [Data Resource] (/data-resource/).  - `sources[array]`: Sources. Les sources brutes de cette ressource  - `title[string]`: Titre. . Un titre lisible par l'homme  - `type[string]`: Il doit s'agir de DataPackageFrictionlessData. Type d'entité NGSI  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propriétés requises    
- `id`  - `resources`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Ce modèle de données provient des données frictionless originales que l'on peut trouver à l'adresse https://frictionlessdata.io/. Il y a quelques changements. 1) l'id et le type ont été rendus obligatoires 2) la structure du schéma json a été adaptée au format officiel des Smart Data Models. Voir le manuel de contribution [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual)    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modèle de données description des propriétés    
Classés par ordre alphabétique (cliquez pour plus de détails)    
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
## Exemples de charges utiles    
#### DataPackageFrictionlessData Valeurs clés NGSI-v2 Exemple    
Voici un exemple de DataPackageFrictionlessData au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
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
#### DataPackageFrictionlessData NGSI-v2 normalisé Exemple    
Voici un exemple de DataPackageFrictionlessData au format JSON-LD tel que normalisé. Il est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
#### DataPackageFrictionlessData Valeurs clés NGSI-LD Exemple    
Voici un exemple de DataPackageFrictionlessData au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
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
#### DataPackageFrictionlessData NGSI-LD normalisé Exemple    
Voici un exemple de DataPackageFrictionlessData au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
