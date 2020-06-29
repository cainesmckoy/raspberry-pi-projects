<?php

exec("sudo /home/pi/humidity2.py");

exec("pkill -9 python");

echo "<html><body><table>\n\n";
$f = fopen("/home/pi/humidity.csv", "r");
while (($line = fgetcsv($f)) !== false) {
        echo "<tr>";
        foreach ($line as $cell) {
                echo "<td>" . htmlspecialchars($cell) . "</td>";
        }
        echo "</tr>\n";
}
fclose($f);
echo "\n</table></body></html>";

header("Refresh:60");

?>
