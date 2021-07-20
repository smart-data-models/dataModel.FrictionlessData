Entity: DataPackageFrictionlessData  
===================================  
[Open License](https://github.com/smart-data-models//dataModel.FrictionlessData/blob/master/DataPackageFrictionlessData/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  

## List of properties  

Required properties  
- No required properties  ## Data Model description of properties  
Sorted alphabetically (click for details)  
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
## Example payloads    
#### DataPackageFrictionlessData NGSI-v2 key-values Example    
Here is an example of a DataPackageFrictionlessData in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
#### DataPackageFrictionlessData NGSI-v2 normalized Example    
Here is an example of a DataPackageFrictionlessData in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
#### DataPackageFrictionlessData NGSI-LD key-values Example    
Here is an example of a DataPackageFrictionlessData in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### DataPackageFrictionlessData NGSI-LD normalized Example    
Here is an example of a DataPackageFrictionlessData in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
