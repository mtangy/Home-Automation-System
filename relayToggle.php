<p>	
    <?php 
	$command = escapeshellcmd('sudo python /usr/local/bin/relayToggle.py'); //PHP to execute the python script that toggles relay
	$acState = shell_exec($command);         //Output of script gets assigned to varable in orger to indicate if AC is on or off
        echo $acState; 
    ?>
</p>
