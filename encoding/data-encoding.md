# Data Encoding/Decoding

## Why data encoding is needed

Programs interact with data in two main forms:

1. **In memory** - data is kept in data structures such as objects, structs, arrays, hash tables, etc. These data structures are optimized for efficient access/manipulation by the CPU.

1. **Transmitted across the network or stored in a file** - in memory data structures don't make sense to other processes, so data needs to be encoded into a sequence of bytes that are self-contained.

We need a way to translate the in-memory representation to a byte sequence.

- **encoding** (aka. serialization, marshalling) = in-memory representation -> bytes
- **decoding** (aka. parsing, deserialization, unmarshalling) = bytes -> in-memory representation

## Types of Encoding Formats

### Language-dependent formats

*eg. Java's `java.io.Serializable`, Ruby's `Marshal`, Python's `pickle`, Go's [gob](https://blog.golang.org/gob).*

Some languages have their own encoding formats. They're convenient if used only for storing/transmitting data to programs in the same language.

#### Cons

- Tied directly to the specific language
- Versioning, effiency are usually afterthoughts
- Some security risks

### Text formats (human-readable)

eg. JSON, XML, CSV

#### Pros
- Popular, often good enough; efficiency isn't that crucial in many cases

#### Cons

- Ambiguity around numbers. Large numbers become inaccurate when parsed in certain languages.
  - JSON doesn't distinguish between integers (whole numbers) and floats (7-bit precision decimals)
  - XML/CSV can't distinguish between a number and string that consists of digits
- Doesn't support binary strings. Need to encode binary data with something like base64.

### Binary formats

There are binary encodings for JSON/XML (eg. MessagePack, BSON, Smile), but they keep the JSON/XML data model unchanged (field names are encoded in data)

#### Other binary formats**

- Thrift's BinaryProtocol = 59 bytes
- Thrift's CompactProtocol = 34 bytes
- Protobuf = 33 bytes
- Avro = 32 bytes

#### Pros
- simpler to implement, simpler to use
- have strict valiation rules
- more compact (field names are omitted)
- schema = required documentation

#### Protobuf & Thrift

**Similarities**

- requires schema
- uses codegen to translate schema definition to language-specific classes (less useful for dynamically typed languages)
- encoded data contains field tags, numbers that map to field names in schema

**Schema evolution (forwards/backwards compability)**

- field names can change, since they're not encded in the data
- field tags can't change
- can add new fields w/ new tag numbers; but new fields must be optional or have a default value or would break old clients
- can only remove optional fields (but can't reuse the removed tag number again)
- field types may be changeable, but may lose precision

#### Avro

- also use schemas (two types: Avro IDL, JSON-based), but schema is included with Avro file (avro files are 'self-describing')
- no field tags or types encoded in data
- to parse: check schema for type/order of fields

**Schema evolution**

- "writer's" schema - the schema version that the encoding application uses (which could be compiled into the app)
- "reader's schema" - the schema version that the decoding application uses (could be generated from the schema during app build process)
- these two schemas don't have to be the same, just need to be compatible.
- Avro lib resolves diffs by translating the writer's schema data into the reader's schema.
  - eg. field that's only in the writer's schema is ignored by the decoding app
  - eg. if decoding app is expecting a field not in the writer's schema, it fills it with a default value from the reader's schema.
- can only add/remove a field that has a default value
- can change field type; changing field name is trickier

**Pros**
- good for dynamically generated schemas; an Avro schema can be generated from a DB schema. If DB schema changes, can just generate a new Avro schema from the updated DB schema.