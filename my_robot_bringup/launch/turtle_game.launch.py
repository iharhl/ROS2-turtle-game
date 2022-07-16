from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description(): # exact name!
    ld = LaunchDescription()

    turtlesim = Node(
        package="turtlesim",
        executable="turtlesim_node",
    )

    turtle_spawner_node = Node(
        package="turtle_game",
        executable="turtle_spawner",
        parameters=[
            {"spawn_frequency": 0.5}
        ]
    )

    turtle_controller_node = Node(
        package="turtle_game",
        executable="turtle_controller",
        parameters=[
            {"catch_closest_turtle": True}
        ]
    )

    ld.add_action(turtlesim)
    ld.add_action(turtle_spawner_node)
    ld.add_action(turtle_controller_node)

    return ld