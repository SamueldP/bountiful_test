for file in blog.html resources.html; do
    sed -i 's/<div class="banner">/<div class="banner">\n        <div class="word-slide">FAITH<\/div>\n        <div class="word-slide">FOOD<\/div>\n        <div class="word-slide">FAMILY<\/div>\n        <div class="word-slide">FELLOWSHIP<\/div>/g' $file
    sed -i 's/FAITH - FOOD - FAMILY - FELLOWSHIP//g' $file
done
