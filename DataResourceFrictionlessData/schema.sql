/* (Beta) Export of data model DataResourceFrictionlessData of the subject dataModel.FrictionlessData for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE DataResourceFrictionlessData_type AS ENUM ('DataResourceFrictionlessData');
CREATE TABLE DataResourceFrictionlessData (address JSON, areaServed TEXT, bytes NUMERIC, data JSON, description TEXT, encoding TEXT, format TEXT, hash TEXT, homepage TEXT, licenses JSON, mediatype TEXT, name TEXT, path JSON, profile TEXT, schema JSON, sources JSON, title TEXT, type DataResourceFrictionlessData_type);