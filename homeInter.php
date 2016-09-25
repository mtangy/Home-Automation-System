<HTML>
	<TITLE>Home Automation Interface</TITLE>
	<BODY>
		<H1>Air Conditioning Power(Relay 1)</H1>
		<H2>Turn AC On/Off</H2>
		<H3>
		     <p>	
		<form action="relayToggle.php" method="get">
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
			    <?php 			        
			       $temp= $_POST['temp'];
                               $tempFile = fopen('/usr/local/bin/temp.txt','w');
			       fwrite($tempFile,$temp);
                               fclose($tempFile);	
			    ?>
			</strong>
			</p>
		</H3>
	</BODY>
</HTML>
