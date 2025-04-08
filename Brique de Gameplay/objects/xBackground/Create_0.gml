var_room_w = view_wport[0];
var_room_h = view_hport[0];

view_wport[0]= display_get_width();
view_hport[0]= display_get_height();

window_set_size(view_wport[0],view_hport[0]);

window_set_position(0,0);

if view_wport[0] != surface_get_width(application_surface) || var_room_h != surface_get_height(application_surface)
{
	surface_resize(application_surface, view_wport[0], view_hport[0]);
}