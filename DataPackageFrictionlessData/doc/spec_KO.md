<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

=====================
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `contributors[array]`: 기여자. 이 설명자의 기여자  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

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
      description: Image. . A image to represent this package    
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
        type: string    
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
  x-model-schema: ""    
  x-model-tags: SDG    
  x-version: 0.0.3    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
