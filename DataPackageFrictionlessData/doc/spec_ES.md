Entidad: DataPackageFrictionlessData  
====================================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/DataPackageFrictionlessData/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **El paquete de datos es una especificación sencilla para el acceso y la entrega de datos.Convertido para la iniciativa Smart Data Models a partir de los datos originales sin fricción**  
versión: 0.0.1  

## Lista de propiedades  

- `contributors`: Colaboradores. . Los colaboradores de este descriptor  - `created`: Creado. La hora de la fecha debe ajustarse a los formatos de cadena para la hora de la fecha como se describe en [RFC3339](https://tools.ietf.org/html/rfc3339#section-5.6). La fecha en la que se creó este descriptor  - `description`: Descripción. . Una descripción de texto. Se recomienda el uso de Markdown  - `homepage`: Página de inicio. . El hogar en la web que está relacionado con este paquete de datos  - `id`: ID. Un patrón de uso común para los paquetes de datos es como formato de empaquetado dentro de los límites de un sistema o plataforma. En estos casos, se desea un identificador único para un paquete para los flujos de trabajo comunes de manejo de datos, como la actualización de un paquete existente. Aunque a nivel de la especificación no se puede validar la unicidad global, los consumidores que utilizan la propiedad `id` `DEBEN` asegurar que los identificadores son globalmente únicos. Una propiedad reservada para los identificadores únicos a nivel mundial. Ejemplos de identificadores que son únicos son los UUID y los DOI  - `image`: Imagen. . Una imagen para representar este paquete  - `keywords`: Palabras clave. . Una lista de palabras clave que describen este paquete  - `licenses`: Licencias. Esta propiedad no es legalmente vinculante y no garantiza que el paquete tenga una licencia en los términos aquí definidos. La(s) licencia(s) bajo las que se publica este paquete  - `name`: Nombre. Lo ideal es que sea un nombre utilizable en url y legible por humanos. El nombre `DEBE` ser invariable, lo que significa que `NO` debe cambiar cuando se actualiza su descriptor principal. Una cadena de identificación. Se permiten caracteres en minúsculas con `.`, `_`, `-` y `/`.  - `profile`: Perfil. Cada descriptor de Paquete y Recurso tiene un perfil. El perfil por defecto, si no se declara ninguno, es `data-package` para Package y `data-resource` para Resource. El perfil de este descriptor  - `resources`: Recursos de datos. . Un `array` de objetos de Recursos de Datos, cada uno de ellos conforme a la especificación [Data Resource](/data-resource/)  - `sources`: Fuentes. . Las fuentes brutas de este recurso  - `title`: Título. . Un título legible para el ser humano  - `type`: Tiene que ser DataPackageFrictionlessData. Tipo de entidad NGSI    
Propiedades requeridas  
- `id`  - `resources`  - `type`    
Este modelo de datos procede de los datos originales sin fricción que se pueden encontrar en https://frictionlessdata.io/. Hay un par de cambios. 1) el id y el tipo se han hecho obligatorios 2)la estructura del esquema json se ha adaptado al formato oficial de los modelos de datos inteligentes. Véase el manual de contribución [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual)  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
  version: 0.0.1    
```  
</details>    
## Ejemplo de carga útil  
#### DataPackageFrictionlessData NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un DataPackageFrictionlessData en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### DataPackageFrictionlessData NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un DataPackageFrictionlessData en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### DataPackageFrictionlessData NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un DataPackageFrictionlessData en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
  ],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### DataPackageFrictionlessData NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un DataPackageFrictionlessData en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "uri:ngsi-ld:datapackage:001",  
  "type": "DataPackageFrictionlessData",  
  "name": {  
    "type": "Property",  
    "value": "cpi"  
  },  
  "title": {  
    "type": "Property",  
    "value": "Annual Consumer Price Index (CPI)"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Annual Consumer Price Index (CPI) for most countries in the world. Reference year is 2005."  
  },  
  "profile": {  
    "type": "Property",  
    "value": "tabular-data-package"  
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
  "version": {  
    "type": "Property",  
    "value": "2.0.0"  
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
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
