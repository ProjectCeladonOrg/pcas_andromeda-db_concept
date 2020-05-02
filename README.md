# PCAS AndromedaDB (Concept)

This ~~is~~ was a proof-of-concept of a hypergraph database for storing data for and
relative to PCAS modules and entities.

## Status
This project is abandoned.  The vertex store turned out to be costly.  PCAS AndromedaDB peaked at around 300K transactions/second.  Project Celadon's GalaxyDB, which uses BSON and filesystem abstraction to store entities, is hosted in a mercurial repo on bitbucket, and has been tested on Linux and Plan 9.  GalaxyDB_PoC, in Python, sustains 1.5M transactions/second per host on CephFS (60 OSD's, single host) with SMR rotating disks and no caching.
The project is currently unreleased as we are translating to Rust.  We expect a 60x improvement on TPS.

Unlike AndromedaDB, GalaxyDB is general purpose, highly tunable, and supports several methods of data import including:
 * Text: CSV, JSON, YAML, TOML
 * Binary: BSON, SQLite3, Pickle
 * StdIn: All of the above
 * Socket/IP: SQL, Neo4J, Any system that can support Text and Binary formats

As always, this project will be released under AGPLv3.

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
