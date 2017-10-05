#created by raymond octavious
#created in september, 2017
#created for isc3u

from scene import *
from Splash_scene import *
import ui

 


main_view = ui.View()
scene_view = SceneView(frame = main_view.bounds, flex = 'WH') 
main_view.add_subview(scene_view)
scene_view.scene = SplashScene() 
main_view.present(hide_title_bar = True, animated = False)
