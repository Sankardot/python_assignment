sql --- stands for structured query language 

invented by ibm in 1970

1974 accepted for the rdms

invented by raymond boyee and donald chamberlin 

it is used to manage and manipulate data both data base sql are interconnecged each other



order of excecution:
from - where - group by - having - select - order by - limit - offset 

this is excecution of the query 



features of sql 

popular demand techonolgy 
manages and retrives the data from datasets 

efficency for handling  high volume data 







unstructure data : data doesnot have predefined data models or  structure 
it lacks for formal and organisezed frame work  it is more challenging for traditional data baseto handle 



structured data : the data is organisezed and formatted in the waythat us easily readable by humans and machines 
it follows a fixed schema or database 




data base: it is structured collection of data that can be accesees amd managed easily store and retreive the information efficinetly 





traditinal file sysytem :A traditional database is a system used to store and manage structured data in tables.

characterstics of traditinal file system 


horitoanl- rows
vertical- columns 


data redudancy: it occurs when piece of data stored multiple places with in data base  or across database


data isolation: the ability of data base system to allow multiple transaction to acces the same data without interfering each other 

data acces: it becomes diffult to  acces important data if multiple users are searching at the same time 



ACID

A: Atomicity
C: consistency
I: isolation
D: durability





NUT SHELL: IT IS USED To communicate with database system to retrive the information from db 





COMMANDS: IN THE SQL THEY ARE 5 COMMANDS

DDL DML DCL TCL DQL


DDL: data defintion language 
it is used create and modify table structure of database

create , alter , drop, truncate

create: a new table , db


Alter: it is used to modify the existing table by adding unique attributes

drop: it used drop the table from the data base 


truncate: it is used delete the rows in the table 




DML: Data manipluation language 
it is used manipulate the data the present db it used to maniplute adb and data accesees
select , insert, update, delete

select: this select command it is used to fetch the data from db


insert : insert the new values in the table 


update : it is used to modify existing record in the table 


delete: the delete commad used to delete specific row or even all the rows from  tables of syntax deletes from table name


lock command : is used to control acces to data in db especially when multiples users are trying to read or write data at the same time 






DCL: DATA CONTROL LANGUAGE 
 it is used for mainting the security which gives acces and permisson of db  commands the comes under DCL
priviliges----------> permisiion


grant: it user  to acees tje data bases


revoke: this commad withdraw the user acces priviliges supplied by using the grant command 





TCL:transaction control language 
 it is used genrally for manging the databse to maintain consistency
 a group of tasks combines into single excecution unit suing transaction 
 each transaction start with particular task and it is completd once 


commit: it is used to permantly save a tranaction 

roll back: it is used to restore the tranaction is not  saved 


savepoint :
it used to hold the tranaction temporarily can be rolled backed its  previos state at any point 

