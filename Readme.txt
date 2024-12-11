Blender add-on for importing .bin files created with km2 City Builder with the Midtown Madness 2 core

Requirements:
  This add-on has been tested with Blender 2.91 and Blender 3.1, it may not work with older versions

Installation:
  - Clone this repository with: git clone https://github.com/wilkovatch/km2cb-to-blender-mm2-plugin
  - zip the "io_scene_km2cb_MidtownMadness2" directory in a file named "io_scene_km2cb_MidtownMadness2.zip"
  - Open Blender, go to the preferences menu (Edit->Preferences) and go to the "Add-ons" tab
  - Click the "Install..." button (in the top right corner, to left of the "Refresh" button)
  - Select the addon .zip file you created earlier (io_scene_km2cb_MidtownMadness2.zip)
  - Enable it

Usage:
  - Create your city in km2 City Builder with the Midtown Madness 2 core
  - Export the city to .bin format (Export->PSDL, check the "bin only" flag, then export)
  - Import it in Blender with this plugin (File->Export->Angel Studios PSDL)
  - Export the city with the PSDL plugin (https://github.com/wilkovatch/mm2-blender-psdl-plugin)
