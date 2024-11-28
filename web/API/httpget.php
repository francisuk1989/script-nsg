<?php
try {
    // Open the SQLite database file
    $db = new PDO('sqlite:/database.db');

    // Get the country and operator from the query parameters
    $country = isset($_GET['country']) ? $_GET['country'] : '';
    $operator = isset($_GET['operator']) ? $_GET['isp'] : '';

    // Prepare and execute a query with the country and operator parameters
    $stmt = $db->prepare('SELECT * FROM your_table WHERE country_code = :country AND isp = :isp');
    $stmt->bindParam(':country', $country);
    $stmt->bindParam(':isp', $isp);
    $stmt->execute();

    // Fetch all results as an associative array
    $results = $stmt->fetchAll(PDO::FETCH_ASSOC);

    // XML template
    $xmlTemplate = '<?xml version="1.0" encoding="UTF-8"?>
<test>
    <cases>
    </cases>
</test>';

    // Create a new SimpleXMLElement object
    $xml = new SimpleXMLElement($xmlTemplate);

    // Iterate over the results and add them to the XML template
    foreach ($results as $row) {
        $case = $xml->cases->addChild('case');
        $case->addChild('name', htmlspecialchars($row['name']));
        $case->addChild('url', htmlspecialchars($row['url']));
        $case->addChild('repeat', htmlspecialchars($row['repetition']));
        $case->addChild('duration', htmlspecialchars($row['duree']));
        $case->addChild('pause', htmlspecialchars($row['pause']));
        $case->addChild('concurrence', htmlspecialchars($row['multi']));
    }

    // Set the content type to XML
    header('Content-Type: application/xml');
    header('Content-Disposition: attachment; filename="output.xml"');

    // Output the XML
    echo $xml->asXML();

} catch (PDOException $e) {
    // If there is an error, output it as XML
    header('Content-Type: application/xml');
    $errorXml = new SimpleXMLElement('<error/>');
    $errorXml->addChild('message', htmlspecialchars($e->getMessage()));
    echo $errorXml->asXML();
}