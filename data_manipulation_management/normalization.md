
## starting table
The `transactions` table:
| transaction_id | customer_name | cashier_name | year | albums_purchased |
|---|---|---|---|---|
| 1 | Amanda | Sam | 2000 | Rubber Soul, Let It Be |
| 2 | Toby | Sam | 2000 | My Generation | 
| 3 | Max | Bob | 2018 | Meet the Beatles, Help! |

## 1NF

Atomicity: one value per cell

The `transactions` table:
| transaction_id | customer_name | cashier_name | year | album_purchased |
|---|---|---|---|---|
| 1 | Amanda | Sam | 2000 | Rubber Soul |
| 1 | Amanda | Sam | 2000 | Let It Be |
| 2 | Toby | Sam | 2000 | My Generation |
| 3 | Max | Bob | 2018 | Meet the Beatles, |
| 3 | Max | Bob | 2018 | Help! |

## 2NF

1NF + a primary key for each table

Note that these tables are the end result of conceptual and logical data modeling steps.
Note the one-to-many (1:N) relationship between transaction ID and albums sold ID (alternatively, the N:1 relation between albums sold and transactions).

The `transactions` table:
| transaction_id | customer_name | cashier_name | year |
|---|---|---|---|
| 1 | Amanda | Sam | 2000 |
| 2 | Toby | Sam | 2000 |
| 3 | Max | Bob | 2018 |

The `albums_sold` table:
| album_id | album_name | transaction_id |
|---|---|---|---|---|
| 1 | Rubber Soul | 1 |
| 2 | Let It Be | 1 |
| 3 | My Generation | 2 |
| 4 | Meet the Beatles | 3 |
| 5 | Help! | 3 |

Recreate the original table with joins.

```sql 
SELECT * 
FROM transactions 
JOIN albums_sold 
  ON transactions.transaction_id = albums_sold.transaction_id;
```

## 3NF

2NF + absence of transitive dependencies

What are [transitive dependencies](https://en.wikipedia.org/wiki/Transitive_dependency#Database_Management_Systems)? It basically means that two attributes are indrectly related. Above, `customer_name` and `cashier_name` are indirectly related because what really associates them is the particular transaction. Therefore, the cashiers should get their own table and the transaction table should reference the appropriate cashier ID.

The `transactions` table:
| transaction_id | customer_name | year | cashier_id |
|---|---|---|---|
| 1 | Amanda | 2000 | 1 |
| 2 | Toby | 2000 | 1 |
| 3 | Max | 2018 | 2 |

The `cashiers` table:
| cashier_id | name |
|---|---|---|
| 1 | Sam |
| 2 | Bob |

The `albums_sold` table:
| album_id | album_name | transaction_id |
|---|---|---|
| 1 | Rubber Soul | 1 |
| 2 | Let It Be | 1 |
| 3 | My Generation | 2 |
| 4 | Meet the Beatles | 3 |
| 5 | Help! | 3 |

Recreate the original table with joins.

```sql
SELECT * 
FROM transactions 
JOIN albums_sold 
  ON transactions.transaction_id = albums_sold.transaction_id
JOIN cashiers
  ON transactions.cashier_id = cashiers.id;
```
