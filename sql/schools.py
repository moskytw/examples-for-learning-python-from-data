#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv
import sqlite3

def _perform(db_path, executer):

    conn = sqlite3.connect(db_path)
    # Let SQLite accept 8-bit string.
    # After add it, it is more convenient for saving the csv data into db.
    conn.text_factory = str
    cur = conn.cursor()

    try:
        executer(cur)
    except:
        conn.rollback()
        raise
    else:
        conn.commit()

    cur.close()
    conn.close()

def perform(db_path, *args, **kargs):
    _perform(db_path, lambda cur: cur.execute(*args, **kargs))

def perform_many(db_path, *args, **kargs):
    _perform(db_path, lambda cur: cur.executemany(*args, **kargs))

def drop_table(db_path='schools.db'):
    perform(db_path, 'DROP TABLE schools')

def create_table(db_path='schools.db'):
    perform(db_path, '''\
CREATE TABLE schools (
        id      TEXT PRIMARY KEY NOT NULL,
        name    TEXT NOT NULL,
        county  TEXT NOT NULL,
        address TEXT NOT NULL,
        phone   TEXT NOT NULL,
        url     TEXT NOT NULL,
        type    TEXT NOT NULL
)''')

def load_csv(csv_path='schools.csv', db_path='schools.db'):
    with open(csv_path) as f:
        rows = list(csv.reader(f))[3:-2]
        perform_many(db_path, 'INSERT INTO schools VALUES (?, ?, ?, ?, ?, ?, ?)', rows)

if __name__ == '__main__':
    import clime.now
