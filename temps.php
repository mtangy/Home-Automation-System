
<HTML>
	<TITLE>Room Temperature</TITLE>
	<BODY>
		<H1>Current Temperature in my room</H1>
		<H2>
			<p>	
				The temperature in my room is: 
				<?php 
				$command = escapeshellcmd('sudo python /usr/local/bin/temp.py'); 
				$temperature = shell_exec($command); 

				echo $temperature; 
				?>		
 			</p>
		</H2>
	</BODY>
</HTML>

