<p>	
    <?php 
	$command = escapeshellcmd('sudo python /usr/local/bin/relayToggle.py'); 
	$acState = shell_exec($command); 
    echo $acState; 
    ?>
</p>