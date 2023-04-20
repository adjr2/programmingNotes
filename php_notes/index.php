<?php
#variable defination
// $name = "Dhiraj";
#echo $name;

# defining constant
// define('NAME', 'Dhiraj');
// $NAME = 'ALEX';
########################################
# STRINGS #
########################################
// $stringone = 'slim ';
// $stringtwo = 'shady';

# concatation
// echo  $stringone . $stringtwo;

# difference between single and double quotes
// echo 'my name is $stringone.$stringtwo';
// echo "my name is $stringone $stringtwo";
// echo 'the ninja screamed "whaa!"';
// echo "the ninja screamed \"whaa!\"";

# string length
// echo strlen($stringone);
// echo str_replace('s', 'f', $stringone);

############################
# INTEGERS AND FLOAT
############################
// $radius = 23;
// echo $radius++; //does not increment here 
// echo $radius; //increment here

#############################
# INDEXED ARRAY
#############################
// $firstname = ['dhiraj ', 'john ', 'slim '];
// $secondname = array('kumar', 'wick', 'shady'); //another way to create array
// echo $firstname[1];
// echo $secondname[1];
// print_r($firstname); //prints the readable version the array. 
//echo doesn't print array. It prints string variable or variables that can be converted to string.

// $firstname[] = 'james'; // this will add a new element to the end of the array
// print_r($firstname);

// another way to add values at the end of an array
// array_push($firstname, 'babu');
// print_r($firstname);

// counting the number of elements in an array
// echo count($firstname);
// $merged_array = array_merge($firstname, $secondname);
// print_r($merged_array);

#############################
# ASSOCIATIVE ARRAY
#############################
// key value pair
// $name_array = ['dhiraj' => 'kumar', 'slim' => 'shady', 'john' => 'wick'];
// echo $name_array['slim'];
// $name_array2 = array('james' => 'bond');
// print_r($name_array2);
// $name_array['james'] = 'bond'; // we can update the value this way as well.

// rest of the functions are similar to indexed array.
// $popped = array_pop($name_array);
// print_r($popped);

#############################
# LOOPS
#############################
// $firstname = ['dhiraj ', 'john ', 'slim '];
/*for ($i = 0; $i < count($firstname); $i++) {
    echo $firstname[$i] . '<br />';
}*/

/*foreach ($firstname as $i) {
    echo $i . '<br />';
}*/
// $products = [
//     ['name' => 'shiny star', 'price' => 20],
//     ['name' => 'green shell', 'price' => 10],
//     ['name' => 'red shell', 'price' => 15],
//     ['name' => 'gold coin', 'price' => 5],
//     ['name' => 'lightning bolt', 'price' => 40],
//     ['name' => 'banana skin', 'price' => 2]
// ];

/*$i = 0;
while ($i < count($firstname)) {
    echo $firstname[$i];
    echo '<br />';
    $i++;
}*/

#############################
# COMPARISON
#############################
// echo true; # it is converted as "1".
// echo false; #it is converted as "".

// numbers
// echo 1 == 2; #will print blank
// echo 1 == 1;

// strings
// echo 'slim' < 'thady';

// loose comparison: it doesn't take into consideration the data type while comparing
// echo 5 == '5'; # this will print true
// echo true == "1";
// echo false == "";

// strong comparison: it takes the data type into consideration
// echo 5 === '5'; # this will be false

#############################
# CONDITIONAL STATEMENT
#############################

/*$price = 20;
if ($price < 10) {
    echo 'condition met';
} elseif ($price < 30) {
    echo 'elseif condition met';
} else {
    echo 'condition not met';
}*/

// foreach ($products as $product) {
//     if ($product['price'] < 20 && $product['price'] > 3) {
//         echo $product['name'];
//         echo '<br />';
//     }
// }

#############################
# BREAK AND CONTINUE
#############################

// foreach ($products as $product) {
//     if ($product['name'] == 'gold coin') {
//         break;
//     }
//     echo $product['price'] . '<br />';
// }

#############################
# FUNCTION
#############################

// function hello($name = "Babu Rao")
// {
//     echo "I am $name!";
// }

// hello("John Wick");

// function format_product($product)
// { // two ways to print the output
//     // echo "{$product['name']} costs \${$product['price']} to buy. <br />";
//     // echo $product['name'] . " costs $" . $product['price'] . " to buy.";
//     return "{$product['name']} costs \${$product['price']} to buy. <br />";
// }

// $formatted = format_product(['name' => 'blackberry', 'price' => 12]);
// echo $formatted;

###############################
# VARIABLE SCOPE
###############################

//global variable
// $name = 'John';
// function say_hello()
// {
//     global $name;
//     $name = 'John Wick'; //this will change the variable value.
//     echo "hello $name";
// }

// say_hello();
// echo $name;

//this will not change the original $name variable
// function say_bye($name)
// {
//     $name = "John Wick";
//     echo "bye $name";
// }
// say_bye($name);
// echo $name;

//this will change the original $name variable
// function say_bye(&$name) // passing by reference
// {
//     $name = "John Wick";
//     echo "bye $name";
// }
// say_bye($name);
// echo $name;


###########################
# INCLUDE AND REQUIRED
###########################

// difference between include and require is that the code will continue if the file does not exist.
// therefore, the echo, after include, will execute.
// echo, after require, will not get executed.

// include('ninja.php'); // or include 'ninja.php';
// echo "end of include";

require('ninja.php'); // or require 'ninja.php';
echo "end of require";

?>
<!DOCTYPE html>
<html>

<head>
    <title>Tutorial</title>
</head>

<body>
    <h1>
        Products
    </h1>
    <div>
        <!-- <?php foreach ($products as $product) { ?> 
            <h3><?php echo $product['name']; ?></h3>
            <p>£<?php echo $product['price']; ?></p>
        <?php } ?>
        -->
        <!-- <?php
                echo $name; #this will print in the html part of the webpage -->
                echo $NAME;
                ?>
        -->
        <!--<ul>
            <?php foreach ($products as $product) { ?> 
                <?php if ($product['price'] > 15) { ?>
                    <li><?php echo $product['name'] ?></li>
                <?php } ?>
            <?php } ?>
            
        </ul>-->
    </div>
</body>

</html>