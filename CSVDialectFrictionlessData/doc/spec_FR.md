Entité : CSVDialectFrictionlessData  
===================================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/CSVDialectFrictionlessData/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Le descripteur du dialecte CSV, converti pour l'initiative Smart Data Models à partir des données originales de frictionless**.  
version : 0.0.1  

## Liste des propriétés  

- `alternateName`: Un nom alternatif pour cet élément  - `caseSensitiveHeader`: En-tête sensible à la casse. L'utilisation de la casse dans les fichiers CSV source n'est pas toujours une décision intentionnelle. Par exemple, est-ce que 'CAT' et 'Cat' doivent être considérés comme ayant la même signification. Spécifie si la casse des en-têtes est significative.  - `commentChar`: Caractère de commentaire. Spécifie que toute ligne commençant par cette chaîne d'un caractère, sans espace précédent, fait que la ligne entière est ignorée.  - `csvddfVersion`: Version du schéma de CSV Dialect. Un nombre pour indiquer la version du schéma de CSV Dialect. La version 1.0 s'appelait CSV Dialect Description Format et utilisait des noms de champs différents.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `delimiter`: Délimiteur. Une séquence de caractères à utiliser comme séparateur de champ.  - `description`: Une description de cet article  - `doubleQuote`: Double citation. Si la valeur Double Quote est définie sur true, deux guillemets consécutifs doivent être interprétés comme un seul. Spécifie le traitement des guillemets à l'intérieur des champs  - `escapeChar`: Caractère d'échappement. Spécifie une chaîne d'un caractère à utiliser comme caractère d'échappement.  - `header`: En-tête. Indique si le fichier comprend une ligne d'en-tête, toujours en tant que première ligne du fichier.  - `id`: Identifiant unique de l'entité  - `lineTerminator`: Terminateur de ligne. Spécifie la séquence de caractères qui doit être utilisée pour terminer les lignes.  - `name`: Le nom de cet élément.  - `nullSequence`: Séquence nulle. Spécifie la séquence nulle, par exemple, \ et ensuite 'N'.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `quoteChar`: Caractère de citation. Spécifie une chaîne d'un caractère à utiliser comme caractère de citation.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `skipInitialSpace`: Sauter l'espace initial. Spécifie l'interprétation des espaces blancs qui suivent immédiatement un délimiteur. Si elle est fausse, l'espace blanc qui suit immédiatement un délimiteur doit être traité comme faisant partie du champ suivant.  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Il doit s'agir de CSVDialectFrictionlessData. Type d'entité NGSI    
Propriétés requises  
- `delimiter`  - `doubleQuote`  - `id`  - `type`    
Ce modèle de données provient des données originales de frictionless que l'on peut trouver sur https://frictionlessdata.io/. Il y a plusieurs changements mineurs. 1) l'id et le type ont été rendus obligatoires 2) la structure du schéma json a été adaptée au format officiel des modèles de données intelligents. Voir le manuel de contribution [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual). 3) Quelques propriétés supplémentaires ont été ajoutées pour des raisons de compatibilité.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CSVDialectFrictionlessData:    
  description: 'The CSV dialect descriptor.Converted for Smart Data Models initiative from original frictionless data'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    caseSensitiveHeader:    
      description: 'Case Sensitive Header. Use of case in source CSV files is not always an intentional decision. For example, should ''CAT'' and ''Cat'' be considered to have the same meaning. Specifies if the case of headers is meaningful'    
      type: boolean    
      x-ngsi:    
        type: Property    
    commentChar:    
      description: 'Comment Character. Specifies that any row beginning with this one-character string, without preceding whitespace, causes the entire line to be ignored'    
      type: string    
      x-ngsi:    
        type: Property    
    csvddfVersion:    
      description: 'CSV Dialect schema version. A number to indicate the schema version of CSV Dialect. Version 1.0 was named CSV Dialect Description Format and used different field names'    
      type: number    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    delimiter:    
      description: 'Delimiter. A character sequence to use as the field separator'    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    doubleQuote:    
      description: 'Double Quote. If Double Quote is set to true, two consecutive quotes must be interpreted as one. Specifies the handling of quotes inside fields'    
      type: boolean    
      x-ngsi:    
        type: Property    
    escapeChar:    
      description: 'Escape Character. Specifies a one-character string to use as the escape character'    
      type: string    
      x-ngsi:    
        type: Property    
    header:    
      description: 'Header. Specifies if the file includes a header row, always as the first row in the file'    
      type: boolean    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &csvdialectfrictionlessdata_-_properties_-_owner_-_items_-_anyof    
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
    lineTerminator:    
      description: 'Line Terminator. Specifies the character sequence that must be used to terminate rows'    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    nullSequence:    
      description: 'Null Sequence. Specifies the null sequence, for example, \ and then ''N'''    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *csvdialectfrictionlessdata_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    quoteChar:    
      description: 'Quote Character. Specifies a one-character string to use as the quoting character'    
      type: string    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
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
    skipInitialSpace:    
      description: 'Skip Initial Space. Specifies the interpretation of whitespace immediately following a delimiter. If false, whitespace immediately after a delimiter should be treated as part of the subsequent field'    
      type: boolean    
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'It has to be CSVDialectFrictionlessData. NGSI entity type'    
      enum:    
        - CSVDialectFrictionlessData    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - delimiter    
    - doubleQuote    
    - type    
  type: object    
  version: 0.0.1    
```  
</details>    
## Exemples de charges utiles  
#### CSVDialectFrictionlessData Valeurs-clés NGSI-v2 Exemple  
Voici un exemple de CSVDialectFrictionlessData au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-v2 en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:CSVDialect:id:OAPS:03889914",  
  "type": "CSVDialectFrictionlessData",  
  "alternateName": "",  
  "caseSensitiveHeader": true,  
  "commentChar": "#",  
  "csvddfVersion": 1.2,  
  "dataProvider": "",  
  "dateCreated": "1986-03-01T17:11:28Z",  
  "dateModified": "2017-04-29T03:29:41Z",  
  "delimiter": ";",  
  "description": "",  
  "doubleQuote": true,  
  "escapeChar": "\\",  
  "header": false,  
  "name": "",  
  "owner": [  
    "urn:ngsi-ld:CSVDialect:items:YPBX:70706198",  
    "urn:ngsi-ld:CSVDialect:items:MABG:25535507"  
  ],  
  "quoteChar": "'",  
  "seeAlso": [  
    "urn:ngsi-ld:CSVDialect:items:YNLD:15120048",  
    "urn:ngsi-ld:CSVDialect:items:EFIZ:80683325"  
  ],  
  "skipInitialSpace": false,  
  "source": ""  
}  
```  
#### CSVDialectFrictionlessData NGSI-v2 normalisé Exemple  
Voici un exemple de CSVDialectFrictionlessData au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-v2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:CSVDialect:id:OAPS:03889914",  
  "type": "CSVDialectFrictionlessData",  
  "dateCreated": {  
    "type": "DateTime",  
    "value": "1986-03-01T17:11:28Z"  
  },  
  "dateModified": {  
    "type": "DateTime",  
    "value": "2017-04-29T03:29:41Z"  
  },  
  "source": {  
    "type": "Text",  
    "value": ""  
  },  
  "name": {  
    "type": "Text",  
    "value": ""  
  },  
  "alternateName": {  
    "type": "Text",  
    "value": ""  
  },  
  "description": {  
    "type": "Text",  
    "value": ""  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": ""  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:CSVDialect:items:YPBX:70706198",  
      "urn:ngsi-ld:CSVDialect:items:MABG:25535507"  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:CSVDialect:items:YNLD:15120048",  
      "urn:ngsi-ld:CSVDialect:items:EFIZ:80683325"  
    ]  
  },  
  "csvddfVersion": {  
    "type": "number",  
    "value": 1.2  
  },  
  "delimiter": {  
    "type": "Text",  
    "value": ";"  
  },  
  "doubleQuote": {  
    "type": "boolean",  
    "value": true  
  },  
  "lineTerminator": {  
    "type": "Text",  
    "value": "\\r\\n"  
  },  
  "nullSequence": {  
    "type": "Text",  
    "value": "\\N"  
  },  
  "quoteChar": {  
    "type": "Text",  
    "value": "'"  
  },  
  "escapeChar": {  
    "type": "Text",  
    "value": "\\\\"  
  },  
  "skipInitialSpace": {  
    "type": "boolean",  
    "value": false  
  },  
  "header": {  
    "type": "boolean",  
    "value": false  
  },  
  "commentChar": {  
    "type": "Text",  
    "value": "#"  
  },  
  "caseSensitiveHeader": {  
    "type": "boolean",  
    "value": true  
  }  
}  
```  
#### CSVDialectFrictionlessData Valeurs-clés NGSI-LD Exemple  
Voici un exemple de CSVDialectFrictionlessData au format JSON-LD comme valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et retourne les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:CSVDialect:id:OAPS:03889914",  
  "type": "CSVDialectFrictionlessData",  
  "alternateName": "",  
  "caseSensitiveHeader": true,  
  "commentChar": "#",  
  "csvddfVersion": 1.2,  
  "dataProvider": "",  
  "dateCreated": "1986-03-01T17:11:28Z",  
  "dateModified": "2017-04-29T03:29:41Z",  
  "delimiter": ";",  
  "description": "",  
  "doubleQuote": true,  
  "escapeChar": "\\",  
  "header": false,  
  "name": "",  
  "owner": [  
    "urn:ngsi-ld:CSVDialect:items:YPBX:70706198",  
    "urn:ngsi-ld:CSVDialect:items:MABG:25535507"  
  ],  
  "quoteChar": "'",  
  "seeAlso": [  
    "urn:ngsi-ld:CSVDialect:items:YNLD:15120048",  
    "urn:ngsi-ld:CSVDialect:items:EFIZ:80683325"  
  ],  
  "skipInitialSpace": false,  
  "source": "",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### CSVDialectFrictionlessData NGSI-LD normalisé Exemple  
Voici un exemple de CSVDialectFrictionlessData au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-LD lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:CSVDialect:id:OAPS:03889914",  
  "type": "CSVDialectFrictionlessData",  
  "dateCreated": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "1986-03-01T17:11:28Z"  
    }  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2017-04-29T03:29:41Z"  
    }  
  },  
  "source": {  
    "type": "Property",  
    "value": ""  
  },  
  "name": {  
    "type": "Property",  
    "value": ""  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": ""  
  },  
  "description": {  
    "type": "Property",  
    "value": ""  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": ""  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:CSVDialect:items:YPBX:70706198",  
      "urn:ngsi-ld:CSVDialect:items:MABG:25535507"  
    ]  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:CSVDialect:items:YNLD:15120048",  
      "urn:ngsi-ld:CSVDialect:items:EFIZ:80683325"  
    ]  
  },  
  "csvddfVersion": {  
    "type": "Property",  
    "value": 1.2  
  },  
  "delimiter": {  
    "type": "Property",  
    "value": ";"  
  },  
  "doubleQuote": {  
    "type": "Property",  
    "value": true  
  },  
  "lineTerminator": {  
    "type": "Property",  
    "value": ""  
  },  
  "nullSequence": {  
    "type": "Property",  
    "value": "\\N"  
  },  
  "quoteChar": {  
    "type": "Property",  
    "value": "'"  
  },  
  "escapeChar": {  
    "type": "Property",  
    "value": "\\"  
  },  
  "skipInitialSpace": {  
    "type": "Property",  
    "value": false  
  },  
  "header": {  
    "type": "Property",  
    "value": false  
  },  
  "commentChar": {  
    "type": "Property",  
    "value": "#"  
  },  
  "caseSensitiveHeader": {  
    "type": "Property",  
    "value": true  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude