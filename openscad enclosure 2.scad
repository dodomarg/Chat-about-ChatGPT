// Parameters for the enclosure
module arduino_uno_enclosure(width, height, depth, wall_thickness) {
  // Calculate the inner dimensions of the enclosure
  width_inner = width - 2 * wall_thickness;
  height_inner = height - 2 * wall_thickness;
  depth_inner = depth - 2 * wall_thickness;

  // Create the bottom of the enclosure
  translate([0, 0, 0])
    cube([width, depth, wall_thickness], center = true);

  // Create the top of the enclosure
  translate([0, 0, height])
    cube([width, depth, wall_thickness], center = true);

  // Create the sides of the enclosure
  translate([0, depth/2, wall_thickness])
    cube([width, wall_thickness, height_inner], center = true);
  translate([0, -depth/2, wall_thickness])
    cube([width, wall_thickness, height_inner], center = true);

  // Create the front and back of the enclosure
  translate([width/2, 0, wall_thickness])
    cube([wall_thickness, depth, height_inner], center = true);
  translate([-width/2, 0, wall_thickness])
    cube([wall_thickness, depth, height_inner], center = true);
}

// Render the enclosure with default parameters
arduino_uno_enclosure(width = 54, height = 101, depth = 62, wall_thickness = 3);
