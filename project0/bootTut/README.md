# Bootstrap Tutorial
Source: https://www.w3schools.com/bootstrap4/

## What is Bootstrap?
- Bootstrap is a free front-end framework for faster and easier web development
- Bootstrap includes HTML and CSS based design templates for typography, forms, buttons, tables, navigation, modals, image carousels and many other, as well as optional JavaScript plugins
- Bootstrap also gives you the ability to easily create responsive designs

- Bootstrap 4 use jQuery and Popper.js for JavaScript components (like modals, tooltips, popovers etc). However, if you just use the CSS part of Bootstrap, you don't need them.

```
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

<!-- Popper JS -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
```

## Containers
1. The `.container` class provides a responsive fixed width container
2. The `.container-fluid` class provides a full width container, spanning the entire width of the viewport
3. By default, containers have 15px left and right padding, with no top or bottom padding. Therefore, we often use spacing utilities, such as extra padding and margins to make them look even better. For example, .pt-3 means "add a top padding of 16px"
```
<div class="container pt-3"></div>
```
4. Other utilities, such as borders and colors, are also often used together with containers:
```
<div class="container p-3 my-3 border"></div>

<div class="container p-3 my-3 bg-dark text-white"></div>

<div class="container p-3 my-3 bg-primary text-white"></div>
```
5. You can also use the `.container-sm|md|lg|xl` classes to create responsive containers. The `max-width` of the container will change on different screen sizes/viewports:
```
<div class="container-sm">.container-sm</div>
<div class="container-md">.container-md</div>
<div class="container-lg">.container-lg</div>
<div class="container-xl">.container-xl</div>
```

## Grid Systems
1. Bootstrap's grid system is built with flexbox and allows up to 12 columns across the page.
2. The Bootstrap 4 grid system has five classes:
- `.col-` (extra small devices - screen width less than 576px)
- `.col-sm-` (small devices - screen width equal to or greater than 576px)
- `.col-md-` (medium devices - screen width equal to or greater than 768px)
- `.col-lg-` (large devices - screen width equal to or greater than 992px)
- `.col-xl-` (xlarge devices - screen width equal to or greater than 1200px)
3. Three Equal Columns - The following example shows how to create three equal-width columns, on all devices and screen widths:
```
<div class="row">
  <div class="col">.col</div>
  <div class="col">.col</div>
  <div class="col">.col</div>
</div>
```
4. Responsive Columns - The following example shows how to create four equal-width columns starting at tablets and scaling to extra large desktops. **On mobile phones or screens that are less than 576px wide, the columns will automatically stack on top of each other**:
```
<div class="row">
  <div class="col-sm-3">.col-sm-3</div>
  <div class="col-sm-3">.col-sm-3</div>
  <div class="col-sm-3">.col-sm-3</div>
  <div class="col-sm-3">.col-sm-3</div>
</div>
```

## Default Settings
1. Bootstrap 4 uses a default `font-size` of 16px, and its line-height is 1.5. The default `font-family` is "Helvetica Neue", Helvetica, Arial, sans-serif.
2. Display headings are used to stand out more than normal headings (larger font-size and lighter font-weight), and there are four classes to choose from: `.display-1`, `.display-2`, `.display-3`, `.display-4`
3. In Bootstrap 4 the HTML `<small>` element is used to create a lighter, secondary text in any heading
4. Bootstrap 4 will style the HTML `<mark>` element with a yellow background color and some padding:
5. All classes here: https://www.w3schools.com/bootstrap4/bootstrap_ref_all_classes.asp
