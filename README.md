# twolayerbuild

Basis of a python game project

Game objects should subclass Entity

To add behaviours to an object, use Components and Systems
A Component defines the fields and interaction behaviours
A System defines tick behaviours (such as rendering, picking, responding to user input)

To create a system , use game.world.system_manager.addSystem(MANAGE_STRING, SYSTEM_TYPE)
MANAGE_STRING determines when the system's update() method is called
Systems under MANAGE_STRING are updated using game.world.system_manager.update(MANAGE_STRING,TIME_SINCE_LAST_CALL)

To add a component to an Entity, use OWNING_ENTITY.addComponent(COMPONENT)
Each component will automatically be accessible from the relevant systems

The game hud is rendered into the region
    (0,0) -> (window.width, window.height)

The game world, by default, is rendered into the region
    (- window.width / 2, - window.height / 2) - > (window.width / 2, window.height / 2)
    Such that (0,0) is the center of the screen

    With the current camera setup, this actually only means that the camera centers onto (0,0) with the window size as the viewport


