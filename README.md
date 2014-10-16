### YakTrak ###
A collection of scripts for collecting YikYak data.

#### Database Setup ####
1) To create MySQL databases, run `ddl.sql` script within the data directory.
2) For each location you wish to retrieve yaks from, insert a row into the
`locations` table. Populate the latitude and longitude fields for the desired
location. You may use the `name` field to give a textual identifier to the
location.
