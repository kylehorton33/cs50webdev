# Notes for Lecture 1
YouTube: https://www.youtube.com/watch?v=XQs5KcUj-Do&list=PLhQjrBD2T382hIW-IsOVuXP1uMzEvmcE5

## Git
### how to create/push branches
`git branch` to list features
`git branch feature` create a new branch named "feature"
`git checkout feature` switch branch to feature. add and commit changes here
`git checkout master` get back to main branch. see that no changes were made
`git merge feature` from master, merge changes from feature
`git push --set-upstream origin feature` to create a new branch on github

### remote repository
`git fetch` downloads origin/master
`git merge` fast forward remote/master branch to origin/master
`git pull` does both of previous steps

### forks
one version of the repository that is the original, changes made on separate branches, pull request made to master to merge changes
On Github: >Pull Request

## HTML
### links
`<a href='insert_link_address_here'>Hyperlink<\a>`
`href='#id_name_here`

### HTML4 vs HTML5
`<div class="header">` HTML4
`<header>`

### New HTML5
<audio>
<video>
<datalist>

## CSS
Cascading Style Sheets

### Selectors
`h1, h2 { color: red; }` select both headers
`ol li { color: red; }` select all descedents (all li within ol)
`ol > li { color: red; }` select immediate descedents/children ( li immediately one level down from ol)
`a + b` adjacent sibling
`[a=b]` attribute selector
`a:b` pseudoclass
`a::b` pseudoelement

### Responsive Design
Bootstrap
Each row divided into 12 columns

### Sass
make variables in .scss files
`$color: red;` create a variable called color and set to red
compile .scss file to a .css and .map.css file
`sass --watch variables.scss:variables.css`
*Github has built in support for Sass
nesting
inheritance

