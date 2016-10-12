<p>	
    <?php 
	$command = escapeshellcmd('./usr/local/bin/kill.sh');   <!--kill previous instance of relayToggle.php-->
	$command = escapeshellcmd('sudo python /usr/local/bin/relayToggle.py'); <!--execute relayToggle.php-->
	$acState = shell_exec($command); <!--display state of AC-->
    echo $acState; 
    ?>
</p>
