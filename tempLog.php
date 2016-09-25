
<HTML>
	<TITLE>Temp Log</TITLE>
	<BODY>
		<H1>Temperature Log</H1>
		This shows all the enteries that are currently in my temperature database 
		
		<H3>
			<p>	
				Temperature data base: 
				<?php 
				$command = escapeshellcmd('sudo python /usr/local/bin/tLog.py'); 
				$temperature = shell_exec($command); 

				echo $temperature; 
				?>
		
 			</p>
		</H3>
	</BODY>
</HTML>

