<?php
$listsDirectory = 'https://ec30-88-201-206-206.ngrok-free.app/';
$data = file_get_contents($listsDirectory);

$doc = new DOMDocument();
$doc->loadHTML($data);
$liList = $doc->getElementsByTagName('li');
$liValues = array();
foreach ($liList as $li) {
    $liValues[] = $li->nodeValue;
}

function getRequiredFileContent($listDir, $listValues,$requiredFile){
	foreach ($listValues as $li){
	if ($li == $requiredFile){
		$competitionList = file_get_contents($listDir.$li);
		echo $competitionList;
		}
	}
}

getRequiredFileContent($listsDirectory,$liValues,'testToCopy222.txt');
?>