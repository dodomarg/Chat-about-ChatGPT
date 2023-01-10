// Create the enclosure
difference(){
    cube([68.6 + 2*3, 53.4 + 2*3, 3], center = true);

// Cut out the USB port
  translate([68.6/2 - 12/2, -53.4/2 + 12/2, 3/2])
    rotate([0,90,0])cylinder(h = 3, r = 12/2, center = true);

// Cut out the DC power jack
  translate([68.6/2 - 10/2, 53.4/2 - 10/2, 3/2]) 
    cylinder(h = 3, r = 10/2, center = true);

// Cut out the reset button
    translate([68.6/2 - 5/2, 0, 3/2])
    cylinder(h = 3, r = 5/2, center = true);

// Cut out the headers

  translate([-68.6/2 + 20/2, 0, 3/2])
    cube([20, 10, 3], center = true);
// Cut out the display

  translate([68.6/2 - 35/2, 53.4/2 - 15/2, 3/2])
    cube([35, 15, 3], center = true);
}
// Render the enclosure
render();
