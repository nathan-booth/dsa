# Schemas

- [ ] Define

## Fact Tables

- [ ] Define
- [ ] Write example

## Dimension Tables

- [ ] Define
- [ ] Write example

## An Example

![example](https://s3.amazonaws.com/video.udacity-data.com/topher/2019/March/5c81772b_dimension-fact-tables/dimension-fact-tables.png)

The fact table `fact_sales` is organized around a business metric `units_sold`. This answers the most important metric for this process - how much was sold? The other columns reference primary keys of the dimension tables.

The dimension tables provide supporting information about the business metric.

- `dim_store` answers where the product was purchased
- `dim_product` answers what product was purchased
- `dim_date` answer when the product was purchased

## Star Schema

[This diagram](https://dbdiagram.io/d/5cae939ff7c5bb70c72f9731) shows a basic star schema. `transactions` is the fact table. `items_purchased`, `customers` and `stores` are dimension tables. The dimensions add information about main metric we care about - how much money is spent?

## Snowflake Schema

- [ ] Create a diagram

## Data Definition Language (DDL)

Tables are made more consistent through the use of constraints. Constraints control what kinds of data can be inserted into the various columns of a table.

Common contraints include:

- NOT NULL
- UNIQUE
- PRIMARY KEY

## Resources
- [ERDs](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model)
- [star schema](https://en.wikipedia.org/wiki/Star_schema)
- [snowflake schema](https://en.wikipedia.org/wiki/Snowflake_schema)
- [data warehousing](https://medium.com/@BluePi_In/deep-diving-in-the-world-of-data-warehousing-78c0d52f49a)
- [dimension table](https://en.wikipedia.org/wiki/Dimension_(data_warehouse))
- [fact table](https://en.wikipedia.org/wiki/Fact_table)