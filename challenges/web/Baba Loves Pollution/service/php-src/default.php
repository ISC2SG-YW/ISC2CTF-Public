<?php
class MyDatabase extends SQLite3 {
    function __construct($db_file) {
        $this->open($db_file);
    }
}

$db_file = 'pollution.db';

// Create or open the database
$db = new MyDatabase($db_file);