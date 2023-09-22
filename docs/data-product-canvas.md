# Data Product Canvas - Berlin LOR daycare centers

## Input Ports

**Input ports define the format and protocol in which data can be read (database, file, API, visualizations)**

This data product uses LOR geodata provided by [Open Lifeworlds](https://github.com/open-lifeworlds) available under the
following URLs

* [berlin-lor-daycare-centers-2013-00/berlin-lor-daycare-centers-2023-10-details](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-daycare-centers/main/data/berlin-lor-daycare-centers-2013-00/berlin-lor-daycare-centers-2023-10-details.csv)
* [berlin-lor-districts/berlin-lor-districts.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-districts/berlin-lor-districts.geojson)
* [berlin-lor-forecast-areas-until-2020/berlin-lor-forecast-areas-until-2020.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-forecast-areas-until-2020/berlin-lor-forecast-areas-until-2020.geojson)
* [berlin-lor-forecast-areas-from-2021/berlin-lor-forecast-areas-from-2021.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-forecast-areas-from-2021/berlin-lor-forecast-areas-from-2021.geojson)
* [berlin-lor-district-regions-until-2020/berlin-lor-district-regions-until-2020.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-district-regions-until-2020/berlin-lor-district-regions-until-2020.geojson)
* [berlin-lor-district-regions-from-2021/berlin-lor-district-regions-from-2021.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-district-regions-from-2021/berlin-lor-district-regions-from-2021.geojson)
* [berlin-lor-planning-areas-until-2020/berlin-lor-planning-areas-until-2020.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-planning-areas-until-2020/berlin-lor-planning-areas-until-2020.geojson)
* [berlin-lor-planning-areas-from-2021/berlin-lor-planning-areas-from-2021.geojson](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-geodata/main/data/berlin-lor-planning-areas-from-2021/berlin-lor-planning-areas-from-2021.geojson)

and detailed daycare center data provided by [Senatsverwaltung für Bildung, Jugend und Familie Berlin](https://www.berlin.de/sen/bildung/service/daten/) available under the following
URLs

* [kitaliste_aktuell.xlsx](https://www.berlin.de/sen/jugend/traegerservice/kitaliste_aktuell.xlsx)

## Data Product Design

**Describe everything you need to design a data product on a conceptual level.**
**Ingestion, storage, transport, wrangling, cleaning, transformations, enrichment, augmentation, analytics, SQL
statements, or used data platform services.**

* [filters data that matches Gesobau areas](../lib/transform/data_filterer.py)

## Output Ports

**Output ports define the format and protocol in which data can be exposed (db, file, API, visualizations)**

Data blended into geojson is available under the following URLs

* [berlin-lor-daycare-centers-2013-10/berlin-lor-daycare-centers-2013-10-details.geojson](../data/berlin-gesobau-lor-daycare-centers-geojson/berlin-lor-daycare-centers-2023-10-details.geojson)
* [berlin-lor-daycare-centers-2013-11/berlin-lor-daycare-centers-2013-11-details.geojson](../data/berlin-gesobau-lor-daycare-centers-geojson/berlin-lor-daycare-centers-2023-10-details.geojson)

## Metadata

### Ownership

**Domain, data product owner, organizational unit, license, version and expiration date**

* ownership: Open Lifeworlds
* domain: geodata
* license: CC-BY-4.0

### Schema

**Attributes, data types, constraints, and relationships to other elements**

### Semantics

**Description, logical model**

### Security

**Security rules applied to the data product usage e.g. public org, internal, personally identifiable information (PII)
attributes**

## Observability

### Quality metrics

**Requirements and metrics such as accuracy, completeness, integrity, or compliance to Data Governance policies**

### Operational metrics

**Interval of change, freshness, usage statistics, availability, number of users, data versioning, etc.**

### SLOs

**Thresholds for service level objectives to up alerting**

## Consumer

**Who is the consumer of the Data Product?**

Consumers of this data product may include

* projects that display data related to Gesobau (buildings, points-of-interest) on a map

## Use Case

**We believe that ...**
**We help achieving ...**
**We know, we are getting there based on ..., ..., ...**

We believe that this data product can be used to display buildings and points-of-interest on an interactive map.

## Classification

**The nature of the exposed data (source-aligned, aggregate, consumer-aligned)**

This data product is consumer-aligned since it is meant to be used for display on maps or graphs.

## Ubiquitous Language

**Context-specific domain terminology (relevant for Data Product), Data Product polysemes which are used to create the
current Data Product**

* **LOR**: (German: Lebensweltlich orientierte Räume) life-world oriented spaces
* **district**: (German: Bezirk)
* **forecast area**: (German: Prognoseraum)
* **district region**: (German: Bezirksregion)
* **planning area**: a spatial unit whose spatial development is planned by the public authorities

---
This data product canvas uses the template
of [datamesh-architecture.com](https://www.datamesh-architecture.com/data-product-canvas).
