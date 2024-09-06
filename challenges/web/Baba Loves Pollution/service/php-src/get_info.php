<?php
require_once 'default.php';
header('Content-Type: application/json');

$uuid = $_GET['uuid'];
$sql = "INSERT OR IGNORE INTO users (uuid) VALUES (?)";
$stmt = $db->prepare($sql);
$stmt->bindValue(1, $uuid, SQLITE3_TEXT);
$stmt->execute();

$sql = "SELECT pollution_count FROM users WHERE uuid = ?";
$stmt = $db->prepare($sql);
$stmt->bindValue(1, $uuid, SQLITE3_TEXT);
$result = $stmt->execute();
$row = $result->fetchArray();
$pollution_count = $row['pollution_count'];

$sql = "SELECT SUM(pollution_count) as total FROM users";
$stmt = $db->prepare($sql);
$result = $stmt->execute();
$row = $result->fetchArray();
$total_pollution = $row['total'];

$db->close();

echo json_encode(['pollution_count' => $pollution_count, 'total_pollution' => $total_pollution]);

