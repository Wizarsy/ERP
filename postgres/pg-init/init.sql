CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE IF NOT EXISTS users_account (
  id VARCHAR(255) DEFAULT uuid_generate_v4(),
  username TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  passwh TEXT NOT NULL,
  email_confirmed BOOLEAN DEFAULT False,
  PRIMARY KEY(id, email)
);