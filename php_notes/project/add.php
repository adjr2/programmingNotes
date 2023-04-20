<?php

// if(isset($_GET['submit'])){
// 	echo $_GET['email'] . '<br />';
// 	echo $_GET['title'] . '<br />';
// 	echo $_GET['ingredients'] . '<br />';
// }
$email = $title = $ingredients = ''; // in Lecture 21.
$errors = array('email' => '', 'title' => '', 'ingredients' => ''); // in Lecture 21.

// Lecture 18 START
if (isset($_POST['submit'])) {
    // echo htmlspecialchars($_POST['email']) . '<br />'; //adding htmlspecialchars with help against XSS (lecture 18)
    // echo htmlspecialchars($_POST['title']) . '<br />';
    // echo htmlspecialchars($_POST['ingredients']) . '<br />';

    //lecture 18 END


    // lecure 19 START
    // check email
    // if (empty($_POST['email'])) {
    //     echo 'An email is required <br />';
    // } else {
    //     echo htmlspecialchars($_POST['email']) . '<br />';
    // }

    // // check title
    // if (empty($_POST['title'])) {
    //     echo 'A title is required <br />';
    // } else {
    //     echo htmlspecialchars($_POST['title']) . '<br />';
    // }

    // // check ingredients
    // if (empty($_POST['ingredients'])) {
    //     echo 'At least one ingredient is required <br />';
    // } else {
    //     echo htmlspecialchars($_POST['ingredients']) . '<br />';
    // }
    // // lecture 19 END

    // // lecture 20 START

    // $email = $title = $ingredients = ''; // in Lecture 21.
    // // check email
    // if (empty($_POST['email'])) {
    //     echo 'An email is required <br />';
    // } else {
    //     $email = $_POST['email'];
    //     if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    //         echo 'Email must be a valid email address';
    //     }
    // }

    // // check title
    // if (empty($_POST['title'])) {
    //     echo 'A title is required <br />';
    // } else {
    //     $title = $_POST['title'];
    //     if (!preg_match('/^[a-zA-Z\s]+$/', $title)) {
    //         echo 'Title must be letters and spaces only';
    //     }
    // }

    // // check ingredients
    // if (empty($_POST['ingredients'])) {
    //     echo 'At least one ingredient is required <br />';
    // } else {
    //     $ingredients = $_POST['ingredients'];
    //     if (!preg_match('/^([a-zA-Z\s]+)(,\s*[a-zA-Z\s]*)*$/', $ingredients)) {
    //         echo 'Ingredients must be a comma separated list';
    //     }
    // }
    // // Lecture 20 END

    // Lecture 21 START
    // check email
    if (empty($_POST['email'])) {
        $errors['email'] = 'An email is required';
    } else {
        $email = $_POST['email'];
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $errors['email'] = 'Email must be a valid email address';
        }
    }

    // check title
    if (empty($_POST['title'])) {
        $errors['title'] = 'A title is required';
    } else {
        $title = $_POST['title'];
        if (!preg_match('/^[a-zA-Z\s]+$/', $title)) {
            $errors['title'] = 'Title must be letters and spaces only';
        }
    }

    // check ingredients
    if (empty($_POST['ingredients'])) {
        $errors['ingredients'] = 'At least one ingredient is required';
    } else {
        $ingredients = $_POST['ingredients'];
        if (!preg_match('/^([a-zA-Z\s]+)(,\s*[a-zA-Z\s]*)*$/', $ingredients)) {
            $errors['ingredients'] = 'Ingredients must be a comma separated list';
        }
    }
    // Lecture 21 END

    // Lecture 22 START
    if (array_filter($errors)) {
        //echo 'errors in form';
    } else {
        //echo 'form is valid';
        header('Location: index.php');
    }
    // Lecture 22 END
} // end POST check

?>

<!DOCTYPE html>
<html>

<?php include('templates/header.php'); ?>

<section class="container grey-text">
    <h4 class="center">Add a Pizza</h4>
    <form class="white" action="add.php" method="POST">
        <label>Your Email</label>
        <input type="text" name="email" value="<?php echo htmlspecialchars($email) ?>">
        <div class="red-text"><?php echo $errors['email']; ?></div>
        <label>Pizza Title</label>
        <input type="text" name="title" value="<?php echo htmlspecialchars($title) ?>">
        <div class="red-text"><?php echo $errors['title']; ?></div>
        <label>Ingredients (comma separated)</label>
        <input type="text" name="ingredients" value="<?php echo htmlspecialchars($ingredients) ?>">
        <div class="red-text"><?php echo $errors['ingredients']; ?></div>
        <div class="center">
            <input type="submit" name="submit" value="Submit" class="btn brand z-depth-0">
        </div>
    </form>
</section>

<?php include('templates/footer.php'); ?>

</html>