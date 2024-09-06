<?php
require_once 'default.php';

$uuid = $_GET['uuid'];
$sql = "SELECT token FROM tokens WHERE uuid = ?";
$stmt = $db->prepare($sql);
$stmt->bindValue(1, $uuid, SQLITE3_TEXT);
$result = $stmt->execute();
$row = $result->fetchArray();
if ($row) {
    echo $row['token'];
    $db->close();
    exit();
} 

$sql = "INSERT OR IGNORE INTO users (uuid) VALUES (?)";
$stmt = $db->prepare($sql);
$stmt->bindValue(1, $uuid, SQLITE3_TEXT);
$stmt->execute();

$sql = "INSERT OR IGNORE INTO tokens (uuid, token) VALUES (?, ?)";
$token = bin2hex(random_bytes(32));
$stmt = $db->prepare($sql);
$stmt->bindValue(1, $uuid, SQLITE3_TEXT);
$stmt->bindValue(2, $token, SQLITE3_TEXT);
$stmt->execute();
$db->close();

echo $token;

