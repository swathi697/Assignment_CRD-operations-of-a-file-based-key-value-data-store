# Assignment_CRD-operations-of-a-file-based-key-value-data-store
##### File based Key-Value datastore

   Supports basic CRD Operations (Create, Read, Delete)

**Functional Requirements:**
  1. It can be initialized using an optional file path. If one is not provided, it will reliably create itself using `uuid`.
  2. A new key-value pair can be added to the data store using the cresate operations. The Key is always string capped at 32 characters and Value must be a JSON object capped at 16KB.
  3. If Create is invoked for an existing key, an appropriate error must be returned.
  4. A Read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object.
  5. A Delete operation can be performed by providing the key.
  6. Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds the key must be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.
  7. Appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits
  8. The file size never exceeds 1GB
  9. The file is accessed by multi-threading

**NON-Functional Requirements:**
  1. The size of the file storing data must never exceed 1GB
  2. More than one client process cannot be allowed to use the same file as a data store at any given time.
  3. A client process is allowed to access the data store using multiple threads, if it desires to. The data store must therefore be thread safe
  


