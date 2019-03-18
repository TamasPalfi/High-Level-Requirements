# High-Level-Requirements

As the database team, we are envisioning creating a relational database where there is a data table for every possible class in the system. This will allow us to abstract a lot of the functionality in our interface, where there will be a fundamental set of "getter" and "setter" methods that the backend development teams can use to access the database. From here, each class will extend from our fundamental interface class. This will allow each class to add methods that are specific to the data items that will be associated with each class. Overall, this will enhance organization because we will not have to deal with having cumbersome amounts of data associated with each class, thus allowing us to simplify the process of accessing and altering data with each object in the system. 

As an overarching example, the fundamental methods of our interface will be something like:
 - get_id
 - set_id
 - remove_item
 
Then, each subsequent class will inherit these methods and then define class specific ones. An example for the User object would be:
 - get_id
 - set_id
 - remove_item
 - get_email
 - set_email
 - get_pw
 - set_pw
 - get_cc_num
 - set_cc_num
 - get_cvv
 - set_cvv
 - get_is_admin
 - set_is_admin
 - get_is_idol
 - set_is_idol

<details>
  <summary> Data Tables </summary>
  
  ### User
  | ID | Email | Password | CC Number | CVV | isAdmin | isIdol |
  | :- | :---: | :------: | :-------: | :-: | :-----: | :----: |
  | Integer | String | String | Integer | Integer | Boolean | Boolean |
  
  ### URL
  | ID | Text/Link | Password | Shortened URL Key | User Key | Associated Website |
  | :- | :---: | :------: | :-------: | :-: | :-----: |
  | Integer | String | Integer | Integer | Date & Time Field | String |
  
  ### Shortened URL
  | ID | Text/Link | Password | Shortened URL Key | User Key | Associated Website |
  | :- | :---: | :------: | :-------: | :-: | :-----: |
  | Integer | String | Integer | Integer | Date & Time Field | String |
  
  ### Sponsored Items
  | ID | Company | Points Given | Description | Size | Times Used |
  | :- | :---: | :------: | :-------: | :-: | :-----: |
  | Integer | String | Integer | String | Int x Int | Integer |
  
  ### Original Posted Image
  | ID | Associated User | Image Format | Timestamp | Associated Website (if applicable) | is_Flagged() | Assoc. Filtered Photo Key (if applicable) |
  | :- | :---: | :------: | :-------: | :-: | :-----: | :----: |
  | Integer | String | String | Date & Time Field | String | Boolean | Integer Key | 
  
  
</details>
  
