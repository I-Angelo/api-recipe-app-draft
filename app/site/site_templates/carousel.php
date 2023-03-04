<?php
$images_dir = '/static/images_carrousel';
$images = glob($images_dir . '/*.{jpg,jpeg,png,gif}', GLOB_BRACE);
?>

<div class="carousel-container">
  <div class="carousel">
    <?php foreach ($images as $image) { ?>
      <div class="carousel-item">
        <img src="<?php echo $image ?>" alt="Image">
      </div>
    <?php } ?>
  </div>
</div>

