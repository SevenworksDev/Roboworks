<?php
$api = '';

function generateUUID() {
    $UUID = '';
    $chars = 'abcdef0123456789';
    for ($i = 0; $i < 32; $i++) {
        $charIndex = mt_rand(0, strlen($chars) - 1);
        $UUID .= $chars[$charIndex];
        if ($i === 7 || $i === 11 || $i === 15 || $i === 19) {
            $UUID .= '-';
        }
    }
    return $UUID;
}

function ai($uuid, $message) {
    $url = $api."/{$uuid}?q=".urlencode($message);

    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $response = curl_exec($ch);
    curl_close($ch);
    $data = json_decode($response, true);

    if ($data && isset($data[0]['response'][count($data[0]['response']) - 1]['content']['response'])) {
        $rwresponse = $data[0]['response'][count($data[0]['response']) - 1]['content']['response'];
        echo $rwresponse;
    } else {
        echo '[Roboworks]: Failed to retrieve response.';
    }
}

$uuid = generateUUID();
$message = $_POST['q'];

ai($uuid, $message);
?>
