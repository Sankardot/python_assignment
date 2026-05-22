-- sql --- stands for structured query language 

-- invented by ibm in 1970

-- 1974 accepted for the rdms

-- invented by raymond boyee and donald chamberlin 

-- it is used to manage and manipulate data both data base sql are interconnecged each other



-- order of excecution:
-- from - where - group by - having - select - order by - limit - offset 

-- this is excecution of the query 



-- features of sql 

-- popular demand techonolgy 
-- manages and retrives the data from datasets 

-- efficency for handling  high volume data 







-- unstructure data : data doesnot have predefined data models or  structure 
-- it lacks for formal and organisezed frame work  it is more challenging for traditional data base to handle 
-- images , mails, photos 


-- -- structured data : the data is organisezed and formatted in the way that us easily readable by humans and machines 
-- -- it follows a fixed schema or database 
-- tables , csv, excel



-- data base: it is structured collection of data that can be accesees amd managed easily store and retreive the 
-- information efficinetly 





-- traditinal file sysytem :A traditional database is a system used to store and manage structured data in tables.

-- characterstics of traditinal file system 


-- horitoanl- rows
-- vertical- columns 


-- data redudancy: it occurs when piece of data stored multiple places with in data base  or across database


-- -- data isolation: the ability of data base system to allow multiple transaction to acces the same data without 
--        interfering each other 



-- data acces: it becomes diffult to  acces important data if multiple users are searching at the same time 



-- ACID

-- A: Atomicity------------Atomicity means a transaction is completed fully or not completed at all.


-- C: consistency--------consistency ensures the database remains correct and valid before and after a transaction.

-- I: isolation-------Isolation ensures multiple transactions do not interfere with each other.


-- D: durability-------Durability ensures committed data is permanently saved even if system crashes.




-- NUT SHELL: IT IS USED To communicate with database system to retrive the information from db 





-- COMMANDS: IN THE SQL THEY ARE 5 COMMANDS

-- DDL DML DCL TCL DQL


-- DDL: data defintion language 
-- it is used create and modify table structure of database

-- create , alter , drop, truncate

-- create: a new table , db


-- Alter: it is used to modify the existing table by adding unique attributes

-- drop: it used drop the table from the data base 


-- truncate: it is used delete the rows in the table 




-- DML: Data manipluation language 
-- it is used manipulate the data the present db it used to maniplute adb and data accesees
--  , insert, update, delete



-- insert : insert the new values in the table 


-- update : it is used to modify existing record in the table 


-- delete: the delete commad used to delete specific row or even all the rows from  tables of syntax 
-- deletes from table name


-- lock command : is used to control acces to data in db especially when multiples users are trying to read or write 
-- data at the same time 






-- DCL: DATA CONTROL LANGUAGE 
--  it is used for mainting the security which gives acces and permisson of db  commands the comes under DCL
-- priviliges----------> permisiion


-- grant: it user  to acees tje data bases


-- revoke: this commad withdraw the user acces priviliges supplied by using the grant command 





-- DQL :Stands For data query language 

-- DQL stands for Data Query Language.

-- select- It is used to retrieve or fetch data from a databas






-- TCL:transaction control language 
--  it is used genrally for manging the databse to maintain consistency
--  a group of tasks combines into single excecution unit using transaction 
--  each transaction start with particular task and it is completd once 


-- commit: it is used to permantly save a tranaction 

-- roll back: it is used to restore the tranaction is not  saved 


-- savepoint :
-- it used to hold the tranaction temporarily can be rolled backed its  previos state at any point 





























-- 5 Important Points: DELETE vs TRUNCATE vs DROP


-- Point	                   DELETE	                TRUNCATE	                     DROP
-- 1. Purpose    	Removes selected rows	         Removes all rows	            Removes entire table

-- 2. WHERE       Clause Supports WHERE	     Does not support WHERE	            Does not support WHERE

-- 3. Table         Structure	Table remains	   Table remains	                    Table deleted

-- 4. Speed	            Slower	                     Faster	                            Fastest

-- 5. Type	             DML Command	               DDL Command	                         DDL Command










-- -- rdbms is relational database managemnt system 
-- --  data stores in table fromat 
-- --  handles large amount of data 
-- --  supoort multiple users ata time 
-- --  security is more rdbms 
-- -- supoort a distributed data base where u can  manage and have the acces fir multiple data base same time 



-- -- dbms : data base managemnet system 
-- -- stores data in xml , json 
-- --  handles less amount of data 
-- --  supoort sigle user only 
-- -- no supoort distrribute data base






-- data models : data models defines how the data is interconnected to each other and how proccesed 
-- and stored each other inside system  also defines logical structes desgin 


-- hierarchial model : it wasthe first model in dbms models ever used in this model daa organisezed in tree
-- like structure connected to  each other  by links 



-- network models :
-- it is represents comples data relationship uisng graph like structure 
-- where data can have many to manty realtionships 



-- entity models :
-- it is mall and well represnted models in apictorial form in the differant shapes 
 
--  pictorial represents  the data that describes how data is communicated and related each other 








-- sql data types: the sql data types specfices  which type of values  is stored in the database 

  


-- numeric data type ------------. int, float, boolean

-- character-----------------------> char, varchar


-- binary------------------------> binary , image

-- data&time---------------------> data , data time, time stamp

--           miscellaneous--------------------> xml, json
--              |
--              | 
--     consistency of various nixture of various things that are not usally connected with each other 





-- numeric data types--holds a intger value  and whokle number and withpout the decimal point 
-- float---stores the decimal point 


-- string data types: it used for character data text

-- char(n)---it is fixed leght of character thaat can cantian number of letters speical charcters 
-- its size can be 0 to 255 charcters


-- varchar: it is similar to char but it stored varible length string size is also more than char data 
-- range to 0 to 60,000



-- data and time :used for storing data and time info 

-- data time: the data time tupe is used for storing the values that can cantian both data s well as the time format 


-- time &stamp:
-- it is also simalr to data and time it can covert current time into various time zones 

-- UTC---universal time coordinated 
-- GMT--- green which time 






-- boolean data type :
-- it is used for true are false values o is consider falase non zero conider true 

-- binary----stores the fixed length of a vaiable 

-- varbinary---stores the varible length of a variable 






-- sql operators: are used to specify certain conditions in an sql statemnet sql operators classfied into 5 

-- Arithmetic Operators
-- +
-- -
-- *
-- /
-- %


-- Comparison Operators
-- =
-- >
-- <
-- >=
-- <=
-- !=
-- <>



-- Logical Operators
-- AND
-- OR
-- NOT
-- Special Operators
-- IN
-- BETWEEN
-- LIKE
-- IS NULL
-- EXISTS






-- -- Normalization:Normalization is a database design technique used to minimize redundancy and maintain
-- --data consistency by organizing data into multiple related tables






-- sql expersiion : is combination of one more values operators and
--  sql function that are same all evaluated to a value 






