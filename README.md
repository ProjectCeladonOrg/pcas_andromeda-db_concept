# PCAS AndromedaDB (Concept)

This ~~is~~ was a proof-of-concept of a hypergraph database for storing data for and
relative to PCAS modules and entities.

## Status
This project is abandoned, and is left here as a record of our humble beginning.  The vertex store turned out to be costly.  PCAS AndromedaDB (python) peaked at around 300K transactions/second (TPS).  We found that ZODB could achieve 600K TPS so that number was set as our milestone since the datastores of both databases was similar.  AndromedaDB failed to achieve that milestone.  

Project Celadon's GalaxyDB, which uses BSON and filesystem abstraction via 9P to store entities, is hosted in an internal mercurial repo. It will remain hosted internally until 2020.5 because I am now the only contributor.  GalaxyDB_PoC, in Python, sustains 1.1M transactions/second (read/write/append) on CephFS (20 OSD's, three hosts) with SMR rotating disks with SATA SSD caching.
The project is currently being translated to Rust.  A 60x improvement on TPS with the same storage backend is expected.

Unlike AndromedaDB, GalaxyDB is general purpose, highly tunable, and supports several methods of data import including:
 * Text: CSV, JSON, YAML, TOML
 * Binary: BSON, SQLite3, Pickle
 * StdIn: All of the above
 * Socket/IP: SQL, Neo4J, Any system that can support the Text and Binary formats

As always, this project will be released under GPLv3 or AGPLv3, as appropriate.

## Getting Started

This code is for stand-alone testing of concepts, and is designed to "plug-in"
as a module to the larger PCAS Django site as an app.  The production version
will be a binary coded in Rust and the relevant pcas_andromeda-db module will
automatically be installed by the pcas_core module.

### Prerequisites

* Linux (3.18+)
* GNU coreutils 8.2+
* Python 3.6+
* Curiosity
* Patience

### Installing

As this is currently a stand-alone module for importing this PoC DB, there are
no specific instructions.  Either place in you python3 site packages location
```
python3 -m site
```
or in the same folder as the source you are importing into.

## Running the tests

The code and documentation in this repo should be sufficient to elucidate what
can (and should) be tested against.

## Contributing

Contributions can be initiated via gists and issues within GitHub.

## Versioning

We use a form of date versioning.  Versions are in the format Y.p-s, where:
Y = the full year
p = the development period (we have 5, every 73 days)
s = status (e.g. alpha1, beta2, rc1, stable)
For example:
AndromedaDB 2020.2-concept1 would be a valid version within this repo.

## License

This project is licensed under the AGPLv3 License - see the [LICENSE](LICENSE) file for details.  This license has been selected intentionally and with great thought,
and is non-negotiable.
