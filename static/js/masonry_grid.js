
/**
 * Set appropriate spanning to any masonry item
 *
 * Get different properties we already set for the masonry, calculate
 * height or spanning for any cell of the masonry grid based on its
 * content-wrapper's height, the (row) gap of the grid, and the size
 * of the implicit row tracks.
 *
 * @param item Object A brick/tile/cell inside the masonry
 */
function resizeMasonryItem(item){
  /* Get the grid object, its row-gap, and the size of its implicit rows */
  var grid = document.getElementsByClassName('masonry')[0],
      rowGap = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-row-gap')),
      rowHeight = parseInt(window.getComputedStyle(grid).getPropertyValue('grid-auto-rows'));
  /*
   * Spanning for any brick = S
   * Grid's row-gap = G
   * Size of grid's implicitly create row-track = R
   * Height of item content = H
   * Net height of the item = H1 = H + G
   * Net height of the implicit row-track = T = G + R
   * S = H1 / T
   */
  var rowSpan = Math.ceil((item.querySelector('.masonry-content').getBoundingClientRect().height+rowGap)/(rowHeight+rowGap) + 4);

  item.style.gridRowEnd = 'span '+rowSpan;
  var footer_time = document.getElementsByClassName("masonry-item__footer")[0];


  footer_time.style.margin = "0px 10px 0px 0px";
}
/**
 * Apply spanning to all the masonry items
 *
 * Loop through all the items and apply the spanning to them using
 * `resizeMasonryItem()` function.
 *
 * @uses resizeMasonryItem
 */
function resizeAllMasonryItems(){
  // Get all item class objects in one list
  var allItems = document.getElementsByClassName('masonry-item');

  /*
   * Loop through the above list and execute the spanning function to
   * each list-item (i.e. each masonry item)
   */
  for(var i=0;i<allItems.length;i++){
    resizeMasonryItem(allItems[i]);
  }
}
/**
 * Resize the items when all the images inside the masonry grid
 * finish loading. This will ensure that all the content inside our
 * masonry items is visible.
 *
 * @uses ImagesLoaded
 * @uses resizeMasonryItem
 */
function waitForImages() {
  var allItems = document.getElementsByClassName('masonry-item');
  for(var i=0;i<allItems.length;i++){
    imagesLoaded( allItems[i], function(instance) {
      var item = instance.elements[0];
      resizeMasonryItem(item);
    } );
  }
}
var masonryEvents = ['load', 'resize'];
masonryEvents.forEach( function(event) {
  window.addEventListener(event, resizeAllMasonryItems);
} );