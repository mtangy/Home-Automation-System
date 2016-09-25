<!DOCTYPE html>
<html>
	<head>
		<title>Temperature Database Interface</title>
	</head>
	<body>
		<H1><U><font color="black"><font color="blue">Temperature Database Interface</font></font></U></H1>
		<H2>Current temperature in my room:
			<p>
				<?php
					$command = escapeshellcmd('sudo python /usr/local/bin/temp.py');
					$temperature = shell_exec($command);
					echo $temperature;
					
					
					$mysqli = mysqli_connect("localhost", "mtangy", "**password**", "roomTemps");
					
					if (mysqli_connect_errno()) {
						printf("Connect failed: %s\n", mysqli_connect_error());
						exit();
					} else {
						$sql = "SELECT * FROM temps";
						$sqlMIN = "select MIN(temp) min from temps";
						$sqlMAX = "select MAX(temp) max from temps";
						$sqlAVG = "select (AVG(temp)) avg from temps";
						
						$res = mysqli_query($mysqli, $sql);
						$resMAX = mysqli_query($mysqli, $sqlMAX);
						$resMIN= mysqli_query($mysqli, $sqlMIN);
						$resAVG= mysqli_query($mysqli, $sqlAVG);
						
						//echo "<br/><br/>Max temperature: ".$resMAX." Min temperature: ".$resMIN."<br/><br/>";
						
						if ($res and $resMAX and $resMIN and $resAVG) {
							$number_of_rows = mysqli_num_rows($res);
							$maxArray = mysqli_fetch_array($resMAX, MYSQLI_ASSOC);
							$minArray = mysqli_fetch_array($resMIN, MYSQLI_ASSOC);
							$avgArray = mysqli_fetch_array($resAVG, MYSQLI_ASSOC);
							
							echo "<br/><br/>Number of entries in the database:      ".$number_of_rows;
							echo "<br/><br/>Average temperature in the database:      ".$avgArray['avg']."F";
							echo "<br/><br/>Max temperature in the database:      ".$maxArray['max']."F";
							echo "<br/><br/>Min temperature in the database:      ".$minArray['min']."F<br/>";
						} else {
							printf("Could not retrieve records: %s\n", mysqli_error($mysqli));
						}
						
						mysqli_free_result($resAVG);
						mysqli_free_result($resMAX);
						mysqli_free_result($resMIN);
						mysqli_free_result($res);
						mysqli_close($mysqli);
					}
               
				?>				
			</p>
		
		</H2>
		<H3>
			<form method= "post" action = "tInter.php">
			<p>
			    <label for="date">Specify a date (YYYY-MM-DD) to be displayed:</label><br/>
                <input type="text" id="date" name="date">
				<label for="limit"><br/><br/>Please specify a number of enteries to show:</label><br/>
                <input type="text" id="limit" name="limit">
			</p>
            <button type="submit" name="submit" value="send">Get Temps</button>
            </form>
			<p><strong>
			    <?php 
			        $mysqli = mysqli_connect("localhost", "mtangy", "**password**", "roomTemps");
					$date = $_POST['date'];
					$limit = $_POST['limit'];
		            if($_POST['date']){
						if (mysqli_connect_errno()) {
							printf("Connect failed: %s\n", mysqli_connect_error());
							exit();
						} else {
							if($_POST['limit']){
								$limit = $_POST['limit'];
							}else{
								$limit = 1;
							}
							$sql = "SELECT * FROM temps where tdate='".$date."' limit 0,".$limit;
							$sql2 = "SELECT * FROM temps where tdate='".$date."'";
							$res = mysqli_query($mysqli, $sql);
                            $res2 = mysqli_query($mysqli, $sql2);
							if ($res) {
								$number_of_rows = mysqli_num_rows($res2);
								echo "<br/>There were ".$number_of_rows." entries found ".$limit." are displayed<br/><br/>";
								echo "-------------------------------------<br/>";
								while ($newArray = mysqli_fetch_array($res, MYSQLI_ASSOC)) {
									$time  = $newArray['ttime'];
									$temp = $newArray['temp'];
									
									echo "|Time: ".$time."  |  Temp:  ".$temp."|<br/>";
									echo "------------------------------------<br/>";
								}
							} else {
								printf("Could not retrieve records: %s\n", mysqli_error($mysqli));
							}
							mysqli_free_result($res);
							mysqli_free_result($res2);
							mysqli_close($mysqli);
						}
				    }
				?>
			</strong></p>
	
		</H3>
	</body>
</html>

