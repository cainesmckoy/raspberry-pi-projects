<?php
exec("sudo /home/pi/sensor.py");

$con=mysqli_connect("localhost","user","password","sensor");
// Check connection
if (mysqli_connect_errno())
{
echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

$result = mysqli_query($con,"SELECT * FROM dhtsensor ORDER BY datetime DESC LIMIT 10");

echo "<table border='1'>
<tr>
<th>Date</th>
<th>temp</th>
<th>humidity</th>
</tr>";

while($row = mysqli_fetch_array($result))
{
echo "<tr>";
echo "<td>" . $row['datetime'] . "</td>";
echo "<td>" . $row['temperature'] . "</td>";
echo "<td>" . $row['humidity'] . "</td>";
echo "</tr>";
}
echo "</table>";

mysqli_close($con);

header("Refresh:60");
?>
