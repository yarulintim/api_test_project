import pytest
import imaplib


@pytest.fixture(scope="session")
def conn_email_admin():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    email = {"email": "softeqpcs@gmail.com", "password": "Softeq@12345"}
    password = email['password']
    mail.login(email['email'], password)
    return mail


@pytest.fixture(scope="session")
def conn_email_sc():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    email = {"email": "softeqpcs2@gmail.com", "password": "Softeq@12345"}
    password = email['password']
    mail.login(email['email'], password)
    return mail


@pytest.fixture(scope="session")
def conn_email_cm():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    email = {"email": "softeqpcs3@gmail.com", "password": "password@54321"}
    password = email['password']
    mail.login(email['email'], password)
    return mail


@pytest.fixture(scope="session")
def conn_email_cm_2():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    email = {"email": "softeqpcs4@gmail.com", "password": "password@54321"}
    password = email['password']
    mail.login(email['email'], password)
    return mail
