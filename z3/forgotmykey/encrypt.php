function my_encrypt($flag, $key) {
  $key = md5($key);
  $message = $flag . "|" . $key;

  $encrypted = chr(rand(0, 126));
  for($i=0;$i<strlen($message);$i++) {
    $encrypted .= chr((ord($message[$i]) + ord($key[$i % strlen($key)]) + ord($encrypted[$i])) % 126);
  }
  $hexstr = unpack('h*', $encrypted);
  return array_shift($hexstr);
}
