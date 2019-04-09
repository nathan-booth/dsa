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

```
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

