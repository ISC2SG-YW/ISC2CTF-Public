<?php
require_once 'default.php';
header('Content-Type: application/json');

$uuid = $_POST['uuid'];
$token = $_POST['token'];
$amount = $_POST['amount'];
if (!is_numeric($amount)) {
    echo json_encode(["success"=>false,"message"=>"Invalid amount"]);
    exit();
}
if ($amount < 0 || $amount > 10000) {
    echo json_encode(["success"=>false,"message"=>"Invalid amount"]);
    exit();
}

$sql = "SELECT token FROM tokens WHERE uuid = ? AND token = ?";
$stmt = $db->prepare($sql);
$stmt->bindValue(1, $uuid, SQLITE3_TEXT);
$stmt->bindValue(2, $token, SQLITE3_TEXT);
$result = $stmt->execute();
$row = $result->fetchArray();
if (!$row) {
    echo json_encode(["success"=>false,"error"=>"Invalid token"]);
    exit();
}

$sql = "DELETE FROM tokens WHERE uuid = ? AND token = ?";
$stmt = $db->prepare($sql);
$stmt->bindValue(1, $uuid, SQLITE3_TEXT);
$stmt->bindValue(2, $token, SQLITE3_TEXT);
$stmt->execute();

$sql = "INSERT OR IGNORE INTO users (uuid) VALUES (?)";
$stmt = $db->prepare($sql);
$stmt->bindValue(1, $uuid, SQLITE3_TEXT);
$stmt->execute();

$sql = "UPDATE users SET pollution_count = pollution_count + ? WHERE uuid = ?";
$stmt = $db->prepare($sql);
$stmt->bindValue(1, $amount, SQLITE3_INTEGER);
$stmt->bindValue(2, $uuid, SQLITE3_TEXT);
$stmt->execute();

$sql = "SELECT pollution_count FROM users WHERE uuid = ?";
$stmt = $db->prepare($sql);
$stmt->bindValue(1, $uuid, SQLITE3_TEXT);
$result = $stmt->execute();
$row = $result->fetchArray();
if ($row['pollution_count']>=30000){
    $flag = $_ENV['FLAG']??'flag{this_is_a_fake_flag}';
    echo json_encode(["success"=>true,"pollution_count" => $row['pollution_count'],"flag"=>$flag]);
}
else{
    echo json_encode(["success"=>true,"pollution_count" => $row['pollution_count']]);
}

$db->close();
