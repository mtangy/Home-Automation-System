<p>	
    <?php 
	$command = escapeshellcmd('./usr/local/bin/kill.sh');   
	$command = escapeshellcmd('sudo python /usr/local/bin/relayToggle.py'); 
	$acState = shell_exec($command); 
    echo $acState; 
    ?>
</p>
