/* (Beta) Export of data model CSVDialectFrictionlessData of the subject dataModel.FrictionlessData for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE CSVDialectFrictionlessData_type AS ENUM ('CSVDialectFrictionlessData');
CREATE TABLE CSVDialectFrictionlessData (alternateName TEXT, caseSensitiveHeader BOOLEAN, commentChar TEXT, csvddfVersion NUMERIC, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, delimiter TEXT, description TEXT, doubleQuote BOOLEAN, escapeChar TEXT, header BOOLEAN, id TEXT PRIMARY KEY, lineTerminator TEXT, name TEXT, nullSequence TEXT, owner JSON, quoteChar TEXT, seeAlso JSON, skipInitialSpace BOOLEAN, source TEXT, type CSVDialectFrictionlessData_type);