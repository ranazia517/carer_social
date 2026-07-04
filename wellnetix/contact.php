<?php
// Wellnetix website contact handler — emails submissions to the team.
// Self-hosted (Hostinger PHP), no third-party service.

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');
header('Cache-Control: no-store, no-cache, must-revalidate, max-age=0');
header('Pragma: no-cache');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok' => false, 'error' => 'Method not allowed.']);
    exit;
}

// Honeypot: real users never fill this hidden field. Bots do -> pretend success, send nothing.
if (!empty($_POST['company'])) {
    echo json_encode(['ok' => true]);
    exit;
}

function clean($v) { return trim((string)($v ?? '')); }
function oneline($v) { return str_replace(["\r", "\n", "%0a", "%0d"], ' ', $v); } // header-injection guard

$name    = oneline(clean($_POST['name'] ?? ''));
$email   = oneline(clean($_POST['email'] ?? ''));
$message = clean($_POST['message'] ?? '');

if ($name === '' || $message === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(422);
    echo json_encode(['ok' => false, 'error' => 'Please add your name, a valid email, and a message.']);
    exit;
}
if (mb_strlen($name) > 120)     $name = mb_substr($name, 0, 120);
if (mb_strlen($message) > 5000) $message = mb_substr($message, 0, 5000);

$to      = 'nimind@wellnetixltd.com';
$subject = 'Website enquiry from ' . $name;

$ip = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
$body  = "New enquiry from the Wellnetix website\n";
$body .= "----------------------------------------\n\n";
$body .= "Name:    $name\n";
$body .= "Email:   $email\n";
$body .= "Time:    " . gmdate('Y-m-d H:i:s') . " UTC\n";
$body .= "IP:      $ip\n\n";
$body .= "Message:\n$message\n";

$fromAddr = 'noreply@wellnetixltd.com';
$headers  = "From: Wellnetix Website <$fromAddr>\r\n";
$headers .= "Reply-To: $name <$email>\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
$headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";

$sent = @mail($to, $subject, $body, $headers, '-f' . $fromAddr);

if ($sent) {
    echo json_encode(['ok' => true]);
} else {
    http_response_code(500);
    echo json_encode(['ok' => false, 'error' => 'Could not send right now — please email us directly at nimind@wellnetixltd.com.']);
}
