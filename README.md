### YakTrak ###
A collection of scripts for collecting YikYak data.

#### Database Setup ####
1) To create MySQL databases, run `ddl.sql` script within the data directory.
2) For each location you wish to retrieve yaks from, insert a row into the
`locations` table. Populate the latitude and longitude fields for the desired
location. You should use the `name` field to give a textual identifier to the
location. You'll pass this name as an argument to the script to collect yaks for
that location.

##### Configuration File #####

Rename `database.cfg.example` to `database.cfg`. Update the fields within that
file to point to your MySQL database.

#### Example Usage ####
Run `yaktrak.py` passing in the name of a location in your `locations` table to
retrieve the last 100 yaks for that location and save them to your database.

    python yaktrak.py utaustin

assumes you have a row in your `locations` table with the `name` field set to
'utaustin'.

#### Sensitive Data ####

Each yak comes across the wire with an associated latitude and longitude of
where it was posted.  YakTrak does not store this information. While we
associate a yak with a particular location in the `locations` table, we do not
store the specific latitude/longitude it was posted from with the yak itself.

#### Acknowledgements ####
The bulk of the work here is done by `pyak`, a script built as a sort of API
around Yik Yak.  The initial pyak repository has been removed from GitHub,
though some forks are floating around both on here as well as pastebin, and a
small community of people having discussions around the internet to keep that
script functioning. Without having a more formal way of thanking them, they
saved me from a lot of headaches.
