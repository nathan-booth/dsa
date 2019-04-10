# Denormalization

## The Tables

|transaction_id|customer_name|cashier_id|year
|---|---|---|---|
| 1 | Amanda | 2000 | 1 |
| 2 | Toby | 2000 | 1 |
| 3 | Max | 2018 | 2 |

| album_id | album_name | transaction_id |
|---|---|---|
| 1 | Rubber Soul | 1 |
| 2 | Let It Be | 1 |
| 3 | My Generation | 2 |
| 4 | Meet the Beatles | 3 |
| 5 | Help! | 3 |

| employee_id | name |
|---|---|---|
| 1 | Sam |
| 2 | Bob |

| transaction_id | amount_spent |
|---|---|---|
| 1 | 40 |
| 2 | 19 |
| 3 | 45 |

## Complexity

```sql
SELECT 
    t2.transaction_id,
    t2.customer_name,
    e.employee_name,
    t2.year,
    a.album_name,
    s.amount_spent
FROM transactions2 AS t2
JOIN employees AS e
    ON t2.cashier_id = e.employee_id
JOIN albums_sold AS a
USING(transaction_id)
JOIN sales AS s
USING(transaction_id);
```

As you can see, this is a pain to write. If you know you will be doing this join a lot, then maybe you should denormalize to increase the read spead of the query. Recall that joins are slow in terms of performance.

## Denormalizing

Denormalizing basically means adding some redundancy back in so that you can have fewer joins and run queries faster.

If we know we want to know the amount spent on each transaction on a real-time bases for an application, then we might create a table that specifically allows us to query without any joins.

|transaction_id|customer_name|cashier_id|year|amount_spent|
|---|---|---|---|---|
| 1 | Amanda | 2000 | 1 | 40
| 2 | Toby | 2000 | 1 | 19
| 3 | Max | 2018 | 2 | 45

This table allows us to write this simple query that answers the business question above "how much is being spent on each sale?"
```sql
SELECT 
    transaction_id, 
    customer_name, 
    amount_spent 
FROM transactions;
```

If we want to know how cashiers are "performing" in a naive way, we might be interested in total sales by cashier. Perhaps, we're using this as a noisy proxy for their checkout rate.

| transaction_id | amount_spent | cashier_name | cashier_id
|---|---|---|---|
| 1 | 40 | Sam | 1
| 2 | 19 | Sam | 1
| 3 | 45 | Bob | 2

Allowing us to write the following simple query:

```sql
SELECT 
    cashier_name, 
    SUM(amount_spent) as total 
FROM cashier_sales GROUP BY cashier_name;
```