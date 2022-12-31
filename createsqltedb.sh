#!/usr/bin/env sh
sqlite3 -batch "$PWD/static/db.sqlite3" < "$PWD/static/sqlite3Db.sql"