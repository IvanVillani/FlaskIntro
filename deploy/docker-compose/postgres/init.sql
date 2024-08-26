-- Drop the pilot table if it exists
DROP TABLE IF EXISTS pilot;

-- Create the pilot table
CREATE TABLE pilot (
    id character varying(50) NOT NULL,
    created timestamp with time zone,
    updated timestamp with time zone,
    email character varying(100) NOT NULL,
    username character varying(100) NOT NULL,
    dob date,
    country character varying(100),
    phone_number character varying(20),
    CONSTRAINT pilot_pkey PRIMARY KEY (id),
    CONSTRAINT pilot_email_key UNIQUE (email)
);

-- Create the primary key index
CREATE INDEX pilot_pkey ON pilot (id);

-- Create the unique constraint for the email column
CREATE UNIQUE INDEX pilot_email_key ON pilot (email);