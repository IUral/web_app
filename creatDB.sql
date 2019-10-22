create user ownerapp with password 'pass';
create user guestApp with password '__pass__'
alter role ownerapp set client_encoding to 'utf8';
alter role ownerapp set default_transaction_isolation to 'read committed';
alter role ownerapp set timezone to 'Europe/Moscow';

create database django_db owner ownerapp;

grant all privileges on database django_db to ownerapp;
grant all privileges on database django_db to guestApp;
