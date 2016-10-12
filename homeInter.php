<HTML>
	<TITLE>Home Automation Interface</TITLE>
	<BODY>
		<H1>Home Automation Interface</H1> 
		<H2>Turn AC On/Off</H2>
		<H3>
		        <p>	
			    <form action="relayToggle.php" method="get"> <!--PHP get method AC power button button calls relayToggle.php-->
			    <input type="submit" value="AC Power">
			    </form>
 			</p>
			<form method= "post" action = "homeInter.php">      
			<p>
			    <label for="acTemp">AC temperature (F):</label><br/>
                            <input type="text" id="temp" name="temp">
			</p>
                 <button type="submit" name="submit" value="send">Change Temperature</button>
                 </form>
			<p><strong>
			    <?php 			           //PHP to write user's desired temperature to file to be read by tempLog.py     
		                if (!empty($_POST['temp'])) {
				     $temp = $_POST['temp'];
				     $result = file_put_contents('/var/www/html/temp.txt', $temp);
				     if($result !== false) {
					echo "Temperature set to $temp F";
				      }
			          }	
			    ?>
			</strong>
			</p>
		<H4>
                    <p><strong>
                            <?php  
                        $command = escapeshellcmd('sudo python /usr/local/bin/temp.py');
		        $temperature = shell_exec($command);
		        echo "Current Temperature: ",$temperature;
                            ?>
                       </strong>
                    </p>
		</H4>
	</BODY>
</HTML>
