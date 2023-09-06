<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: TableSchemaFrictionlessData  
====================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/TableSchemaFrictionlessData/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Un Esquema de Tabla para este recurso, conforme con la especificación de Esquema de Tabla. Convertido para la iniciativa Smart Data Models a partir de datos originales sin fricción**.  
versión: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `alternateName[string]`: Un nombre alternativo para este artículo  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `fields[array]`: Una matriz de objetos Campo de esquema de tabla  - `foreignKeys[array]`:   - `id[*]`: Identificador único de la entidad  - `missingValues[array]`: Muchos conjuntos de datos contienen valores que faltan, ya sea porque un valor no se recogió o porque nunca existió. Los valores que faltan pueden indicarse simplemente con un valor vacío; en otros casos, puede haberse utilizado un valor especial, como "-", "NaN", "0", "-9999", etc. La propiedad "missingValues" permite indicar que estos valores deben interpretarse como equivalentes a null. Los 'missingValues' son cadenas en lugar del tipo de datos del campo en cuestión. Esto permite realizar comparaciones antes de la selección y que los campos tengan valores perdidos que no sean de su tipo, por ejemplo, que un campo "numérico" tenga valores perdidos indicados por "-". El valor predeterminado de "missingValue" para un campo que no sea de tipo cadena es la cadena vacía ''. Para los campos de tipo cadena no hay valor por defecto para 'missingValue' (para los campos de tipo cadena la cadena vacía '' es un valor válido y no tiene por qué indicar null). Valores que, cuando se encuentran en la fuente, deben considerarse valores "nulos", "no presentes" o "en blanco  - `name[string]`: El nombre de este artículo  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `primaryKey[array]`: El nombre del campo en la primaryKey 'DEBE' ser único, y 'DEBE' coincidir con un nombre de campo en la tabla asociada. Es aceptable tener una matriz con un único valor, indicando que el valor de un único campo es la clave primaria. Una clave primaria es un nombre de campo o una matriz de nombres de campo, cuyos valores "DEBEN" identificar de forma única cada fila de la tabla.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: tiene que ser TableSchemaFrictionlessData. Tipo de entidad NGSI  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `fields`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Este modelo de datos procede de los datos originales sin fricción que pueden encontrarse en https://frictionlessdata.io/. Hay varios cambios. 1) el id y el tipo se han hecho obligatorios siempre que sean obligatorios para el estándar NGSI 2)la estructura del esquema json se ha adaptado al formato oficial de los modelos de datos inteligentes. Véase el manual de contribución [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual)  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
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
## Ejemplo de carga útil  
#### TableSchemaFrictionlessData NGSI-v2 key-values Ejemplo  
He aquí un ejemplo de TableSchemaFrictionlessData en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### TableSchemaFrictionlessData NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de TableSchemaFrictionlessData en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TableSchemaFrictionlessData:XVFE:0034",  
  "type": "TableSchemaFrictionlessData",  
  "fields": {  
    "type": "array",  
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
    "type": "array",  
    "value": [  
      "name"  
    ]  
  }  
}  
```  
</details>  
#### TableSchemaFrictionlessData NGSI-LD key-values Ejemplo  
He aquí un ejemplo de TableSchemaFrictionlessData en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### TableSchemaFrictionlessData NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de TableSchemaFrictionlessData en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
