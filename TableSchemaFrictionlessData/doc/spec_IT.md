Entità: TableSchemaFrictionlessData  
===================================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/TableSchemaFrictionlessData/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Uno schema di tabella per questa risorsa, conforme alla specifica Table Schema. Convertito per l'iniziativa Smart Data Models dai dati originali frictionless**  
versione: 0.0.1  

## Elenco delle proprietà  

- `alternateName`: Un nome alternativo per questa voce  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `fields`: Un array di oggetti campo dello schema della tabella  - `foreignKeys`:   - `id`: Identificatore unico dell'entità  - `missingValues`: Molti set di dati arrivano con valori mancanti, o perché un valore non è stato raccolto o non è mai esistito. I valori mancanti possono essere indicati semplicemente dal fatto che il valore è vuoto, in altri casi può essere stato usato un valore speciale, ad esempio '-', 'NaN', '0', '-9999' ecc. La proprietà 'missingValues' fornisce un modo per indicare che questi valori dovrebbero essere interpretati come equivalenti a null. I 'missingValues' sono stringhe piuttosto che essere il tipo di dati del campo particolare. Questo permette il confronto prima del casting e permette ai campi di avere valori mancanti che non sono del loro tipo, per esempio un campo 'number' ha valori mancanti indicati da '-'. Il valore predefinito di 'missingValue' per un campo non di tipo stringa è la stringa vuota ''. Per i campi di tipo stringa non c'è un valore predefinito per 'missingValue' (per i campi stringa la stringa vuota '' è un valore valido e non deve necessariamente indicare null). Valori che, quando incontrati nel sorgente, dovrebbero essere considerati come valori 'null', 'not present', o 'blank  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `primaryKey`: Il nome del campo nella chiave primaria "DEVE" essere unico e "DEVE" corrispondere al nome di un campo nella tabella associata. È accettabile avere un array con un singolo valore, indicando che il valore di un singolo campo è la chiave primaria. Una chiave primaria è un nome di campo o un array di nomi di campi, i cui valori "DEVONO" identificare in modo univoco ogni riga della tabella  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `type`: deve essere TableSchemaFrictionlessData. Tipo di entità NGSI    
Proprietà richieste  
- `fields`  - `id`  - `type`    
Questo modello di dati proviene dai dati originali di frictionless che possono essere trovati su https://frictionlessdata.io/. Ci sono diversi cambiamenti. 1) id e type sono stati resi obbligatori finché sono obbligatori per lo standard NGSI 2) la struttura dello schema json è stata adattata al formato ufficiale degli Smart Data Models. Vedere il manuale dei contributi [https://bit.ly/contribution_manual](https://bit.ly/contribution_manual)  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
TableSchemaFrictionlessData:    
  description: 'A Table Schema for this resource, compliant with the Table Schema specification. Converted for Smart Data Models initiative from original frictionless data'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
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
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    fields:    
      description: 'An array of Table Schema Field objects'    
      items:    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    foreignKeys:    
      description: ""    
      type: array    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &tableschemafrictionlessdata_-_properties_-_owner_-_items_-_anyof    
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
    missingValues:    
      description: 'Many datasets arrive with missing data values, either because a value was not collected or it never existed. Missing values may be indicated simply by the value being empty in other cases a special value may have been used e.g. ''-'', ''NaN'', ''0'', ''-9999'' etc.The ''missingValues'' property provides a way to indicate that these values should be interpreted as equivalent to null. The ''missingValues'' are strings rather than being the data type of the particular field. This allows for comparison prior to casting and for fields to have missing value which are not of their type, for example a ''number'' field to have missing values indicated by ''-''.The default value of ''missingValue'' for a non-string type field is the empty string ''''. For string type fields there is no default for ''missingValue'' (for string fields the empty string '''' is a valid value and need not indicate null). Values that when encountered in the source, should be considered as ''null'', ''not present'', or ''blank'' values'    
      type: array    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *tableschemafrictionlessdata_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'it has to be TableSchemaFrictionlessData. NGSI entity type'    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - fields    
    - id    
    - type    
  type: object    
  version: 0.0.1    
```  
</details>    
## Esempio di payloads  
#### TableSchemaFrictionlessData NGSI-v2 valori chiave Esempio  
Ecco un esempio di un TableSchemaFrictionlessData in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### TableSchemaFrictionlessData NGSI-v2 normalizzato Esempio  
Ecco un esempio di un TableSchemaFrictionlessData in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
#### TableSchemaFrictionlessData NGSI-LD valori-chiave Esempio  
Ecco un esempio di un TableSchemaFrictionlessData in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### TableSchemaFrictionlessData NGSI-LD normalizzato Esempio  
Ecco un esempio di un TableSchemaFrictionlessData in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
  }  
}  
```  
