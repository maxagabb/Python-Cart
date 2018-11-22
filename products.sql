--SET ECHO ON;
drop table  PRODUCTS;
drop table CATEGORY;
CREATE TABLE  PRODUCTS (Product_ID INTEGER, Category_ID INTEGER, Pname VARCHAR(15), price DECIMAL, discountPercent INTEGER, img VARCHAR, PRIMARY KEY (Product_ID), FOREIGN KEY (Category_ID) REFERENCES CATEGORY);
CREATE TABLE  CATEGORY (Category_ID INTEGER, Cname VARCHAR(15), PRIMARY KEY (Category_ID));
DELETE FROM PRODUCTS;
DELETE FROM CATEGORY;
insert into     CATEGORY    (Cname, Category_ID) values( 'DVD', 1);
insert into     CATEGORY    (Cname, Category_ID) values( 'XBOX', 2);
insert into     CATEGORY    (Cname, Category_ID) values( 'PS4', 3);
insert into     CATEGORY    (Cname, Category_ID) values( 'PC', 4);
insert into     CATEGORY    (Cname, Category_ID) values( 'Blu-ray', 5);
insert into     PRODUCTS    (Pname, price, discountPercent, Category_ID, Product_ID, img) values( 'The Holy Grail (DVD)', 4.75, 30, 1, 1, 'holyGrail.jpg');
insert into     PRODUCTS    (Pname, price, discountPercent, Category_ID, Product_ID, img) values( 'Life of Brian (DVD)', 8.97, 20, 1, 2,'lifeOfBrian.jpg');
insert into     PRODUCTS    (Pname, price, discountPercent, Category_ID, Product_ID, img) values( 'The Meaning of Life (DVD)', 6.50, 15, 1, 3,'meaningOfLife.jpg');
insert into     PRODUCTS    (Pname, price, discountPercent, Category_ID, Product_ID, img) values( 'Halo 3 (XBOX)', 6.50, 15, 2, 4,'halo3.jpg');
insert into     PRODUCTS    (Pname, price, discountPercent, Category_ID, Product_ID, img) values( 'Bloodborne (PS4)', 6.50, 15, 3, 5,'bloodborne.jpg');
insert into     PRODUCTS    (Pname, price, discountPercent, Category_ID, Product_ID, img) values( 'Dark Souls (PC)', 6.50, 15, 4, 6,'darkSouls.jpg');
insert into     PRODUCTS    (Pname, price, discountPercent, Category_ID, Product_ID, img) values( 'Fullmetal Alchemist:[Blu]', 294.95, 1, 5, 7,'fmab.jpg');
-- COMMIT and save data
COMMIT;
--SPOOL OFF
