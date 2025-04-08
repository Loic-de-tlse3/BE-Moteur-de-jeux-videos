if (!drag) {
 if (mouse_check_button_pressed(mb_left)) {
  drag = true;
  mx = x - mouse_x;
  my = y - mouse_y;
 }
}

// Drag instance here. You will need to ADD your depth code here. //
else {
  x = mouse_x + mx;
  y = mouse_y + my;
 
// This allows us to snap to a grid if needed. If not remove it. //
  move_snap(2, 2);
 
// Until button left is released //
  if ( mouse_check_button_released(mb_left)) {
  drag = false;
 }
 
  if (xGenerer.button_check){
  object_set_visible(xDistance1, true)
  }else{
  object_set_visible(xDistance1, false)
  }
}